import base64,time,requests,hashlib,json

class KredsAPI():
	def __init__(self,KREDS_API,KREDS_SECRET):
		self.url = "https://kredswallet.com/api"
		self.SIGNATURE = hashlib.sha512(json.dumps(KREDS_SECRET)).hexdigest()
		self.headers = {"context-type":"application/json","X-WWT-APIKEY":KREDS_API,"X-BFX-SIGNATURE":self.SIGNATURE}

	def status(self): # Returns status of the API
		return requests.get("{}/status".format(self.url)).json()

	def info(self): # Returns information on the kreds wallet
		return requests.get("{}/info".format(self.url)).json()

	def getAddresses(self): # Returns information on the addresses for your account
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/addresses".format(self.url),headers=self.headers).json()

	def newAddress(self): # Generates a fresh address for your users
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.post("{}/addresses".format(self.url),headers=self.headers).json()
		
	def balance(self): # Retrieves user's balance
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/balance".format(self.url),headers=self.headers).json()

	def deposits(self): # Fetches account deposits
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/deposits".format(self.url),headers=self.headers).json()

	def summary(self): # Gathers summary of the user's account
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/summary".format(self.url),headers=self.headers).json()

	def transactions(self): # Gather information on all transactions for a user's account
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/transactions".format(self.url),headers=self.headers).json()

	def transaction(self,TXID): # Gather details of provided TXID
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/transactions/{}".format(self.url,TXID),headers=self.headers).json()

	def withdraws(self): # Retrieve user's withdrawals
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.get("{}/withdraws".format(self.url),headers=self.headers).json()

	def withdraw(self,ADDRESS,AMT,FEE): # Generate a new withdrawal
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.post("{}/withdraws/{}/{}/{}".format(self.url,ADDRESS,AMT,FEE)).json()

	def account(self): # Creates new API information
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.post("{}/account".format(self.url),headers=self.headers).json()

	def credit(self,ACCOUNT,AMT): # Credits an account
		NONCE = str(time.time())
		params = {"nonce":NONCE}
		self.headers["X-BFX-PAYLOAD"] = base64.b64encode(json.dumps(params))
		return requests.post("{}/account/credit/{}/{}".format(self.url,ACCOUNT,AMT),headers=self.headers).json()
