import json
import random

from requests import get, post, delete

from .utils import generate_random_string
from .exceptions import EmailAlreadyUsed, EmailAlreadyUsedError

DOMAINS = []
TIMEOUT = 5


def get_domain_list():
    global DOMAINS
    r = get('https://api.mail.gw/domains?page=1', timeout=TIMEOUT).json()
    for i in r['hydra:member']:
        DOMAINS.append(i['domain'])


class Account:
    headers = {'Content-Type': 'application/json'}
    id: str = None
    address: str = None
    password: str = None
    token: str = None
    retention_at: int = None

    def __init__(self,
                 address: str = None,
                 password: str = None,
                 auto_login: bool = True):
        if address is None:
            address = generate_random_string()
        if password is None:
            password = generate_random_string()
        if '@' not in address:
            if len(DOMAINS) == 0:
                get_domain_list()
            address += '@' + random.choice(DOMAINS)
        self.address = address
        self.password = password
        if auto_login:
            self.register(raise_error=False)
            self.get_token()

    def register(self, raise_error: bool = True):
        r = post(
            'https://api.mail.gw/accounts',
            headers=self.headers,
            data=json.dumps({
                'address': self.address,
                'password': self.password
            }),
            timeout=TIMEOUT,
        ).json()
        if EmailAlreadyUsed in r.get('hydra:description', ''):
            if raise_error:
                raise EmailAlreadyUsedError(self.address)
            else:
                return False
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
            timeout=TIMEOUT,
        )
        assert r.status_code == 200, 'Authentication failed!'
        r = r.json()
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
            timeout=TIMEOUT,
        ).json()
        id = r['hydra:member']
        if len(id) <= latest:
            raise IndexError(
                f'No message found! There are only {len(id)} messages.')
        id = id[latest]['id']
        r = get(
            'https://api.mail.gw/messages/' + id,
            headers=self.headers,
            timeout=TIMEOUT,
        ).json()
        return r

    def destroy(self):
        if self.id is None:
            r = get('https://api.mail.gw/me', headers=self.headers).json()
            self.id = r['id']
        delete(
            'https://api.mail.gw/accounts/' + self.id,
            headers=self.headers,
            timeout=TIMEOUT,
        )
        self.headers['Authorization'] = ''
        self.address = self.password = self.id = ''

    def json(self):
        return {
            'address': self.address,
            'password': self.password,
            'id': self.id,
            'token': self.token,
        }

    def __str__(self):
        return f'{self.address}'


if __name__ == '__main__':
    ...
