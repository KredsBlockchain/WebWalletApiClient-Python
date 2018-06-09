# kredswallet Python API
Python implementation of [WebWalletAPIClient](https://kredswallet.com/wallet/apidocs)

### Install
`pip install kredswallet`

```
git clone git@github.com:mustymouse/kredswallet
python setup.py
```

### Use
```python
from kredswallet import *
kreds=KredsAPI(KREDS_API,KREDS_SECRET) # Use environment variable or replace with your key and secret
print(kreds.status())
```
