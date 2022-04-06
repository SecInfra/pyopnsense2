# pyopnsense2

Automatically generated OPNSense library, from documentation
simple python interface

## Usage
In order to access your instance, each class connect individually through the params parameter.
The format is :

params = {
        'base_url' : 'https://blabla.bla/api',
        'auth' : (
            'xxx', # API Secret
            'xxx'), # API Key
        'proxy' : '',
        'verify_cert' : False,
        'timeout' : 60
    }