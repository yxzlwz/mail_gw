# mail_gw

## Description

This is a Pypi package provide a simple way to get a temp email address, and receive the email. In fact, it is a simple wrapper of [mail.gw](https://mail.gw/en/).

The project is released on [pypi.org](https://pypi.org/), you can view it at [https://pypi.org/project/mail-gw/](https://pypi.org/project/mail-gw/).

## Install

Just install it with pip as usual.

```bash
pip3 install mail_gw
```

## Usage

```python
# Import the module
from mail_gw import Account

# Create a account
a = Account(address='test@bluebasketbooks.com.au', password='123456')  # Use the domain listed on the website
b = Account(address='test', password='123456')  # Only prefix, it will randomly choose a domain
c = Account()  # Use both random address and password

# See the details of the account
print(a.json())

# While initializing, the account will be registered on mail.gw and the token will be gotten automatically.
# If it is necessary, you can run these codes to register and get the token manually.
# a.register()
# a.get_token()
# Both of the above steps will return the details of the account.

# Check the email's inbox
print(a.get_message(latest=0))
# latest: 0 means the latest email, 1 means the second latest email, and so on.
```

## Issues

Because of "the Great Wall of China's Internet", the API may not available in some areas of China.

## Contact

[mail@yixiangzhilv.com](mailto:mail@yixiangzhilv.com)
