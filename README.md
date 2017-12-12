# RentShare Python Package

A python package for interfacing with the RentShare API

## Installation

To install from GitHub using [pip](http://www.pip-installer.org/en/latest/):

```bash
pip install git+https://github.com/rentshare/rentshare-python.git
```

If you don't have pip, it can be installed using the below command:

```bash
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

To manually install `rentshare-python`, you can [download the source](https://github.com/rentshare/rentshare-python/zipball/master) and run:

```bash
python setup.py install
```

## Basic usage

```python
import rentshare

# set your api key
rentshare.api_key = 'private_key_6fsMi3GDxXg1XXSluNx1sLEd'

# create an account
account = rentshare.Account.create(
    email='joe.schmoe@example.com',
    full_name='Joe Schmoe',
    user_type='payer'
)
```

## Documentation
Read the [docs](https://developer.rentshare.com/?python)
