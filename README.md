# kredswallet Python API [![Build Status](https://travis-ci.org/MustyMouse/kredswallet.svg?branch=master)](https://travis-ci.org/MustyMouse/kredswallet)
Python implementation of [WebWalletAPIClient](https://kredswallet.com/wallet/apidocs)

### Install
`pip install kredswallet`  

OR  

```
git clone git@github.com:mustymouse/kredswallet
python setup.py
```

### Use
```python
from kredswallet.kredswallet import *
kreds=KredsAPI(KREDS_API,KREDS_SECRET) # Use environment variable or replace with your key and secret
print(kreds.status())
```
