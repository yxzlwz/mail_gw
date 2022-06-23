import json
import random

from requests import get, post, delete

from mail_gw.utils import generate_random_string
from mail_gw.exceptions import EmailAlreadyUsed, EmailAlreadyUsedError

DOMAINS = ['bluebasketbooks.com.au']


def update_domain_list():
    ...


class Account:
    headers = {'Content-Type': 'application/json'}
    id: str = None
    address: str = None
    password: str = None
    token: str = None
    retention_at: int = None

    def __init__(self,
                 address: str = generate_random_string(),
                 password: str = generate_random_string(),
                 auto_register: bool = True):
        if '@' not in address:
            address += '@' + random.choice(DOMAINS)
        self.address = address
        self.password = password
        if auto_register:
            self.register()
            self.get_token()

    def register(self):
        r = post(
            'https://api.mail.gw/accounts',
            headers=self.headers,
            data=json.dumps({
                'address': self.address,
                'password': self.password
            }),
        ).json()
        if EmailAlreadyUsed in r.get('hydra:description', ''):
            raise EmailAlreadyUsedError(self.address)
        self.id = r['id']
        return self.json()

    def get_token(self):
        r = post(
            'https://api.mail.gw/token',
            headers=self.headers,
            data=json.dumps({
                'address': self.address,
                'password': self.password
            }),
        ).json()
        assert r.get('code') == 200, 'Authentication failed!'
        self.token = r['token']
        self.headers['Authorization'] = f'Bearer {r["token"]}'
        return self.json()

    def get_message(self, latest=0):
        assert latest >= 0, IndexError('latest must be >= 0')
        r = get(
            'https://api.mail.gw/messages',
            headers=self.headers,
            params={
                'page': 1
            },
        ).json()
        id = r['hydra:member']
        if len(id) <= latest:
            raise IndexError(
                f'No message found! There are only {len(id)} messages.')
        id = id[latest]['id']
        r = get(
            'https://api.mail.gw/messages/' + id,
            headers=self.headers,
        ).json()
        return r

    def destroy(self):
        delete(
            'https://api.mail.gw/accounts/' + self.id,
            headers=self.headers,
        )
        self.headers['Authorization'] = ''
        self.address = self.password = self.id = ''

    def json(self):
        return {
            'address': self.address,
            'password': self.password,
            'id': self.id,
            'token': self.token
        }

    def __str__(self):
        return f'{self.address}'


if __name__ == '__main__':
    ...
