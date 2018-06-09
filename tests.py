import unittest,os,base64,time,requests,hashlib,json
from kredswallet.kredswallet import *

class TestKreds(unittest.TestCase):
	def setUp(self,KREDS_API=os.environ.get("KREDS_API"),KREDS_SECRET=os.environ.get("KREDS_SECRET")):
		self.kreds = KredsAPI(KREDS_API,KREDS_SECRET)

	def testStatus(self):
		return self.kreds.status()

	def testInfo(self):
		return self.kreds.info()

	def testGetAddresses(self):
		return self.kreds.getAddresses()

	def testNewAddress(self):
		return self.kreds.newAddress()

	def testBalance(self):
		return self.kreds.balance()

	def testDeposits(self):
		return self.kreds.deposits()

	def testSummary(self):
		return self.kreds.summary()

	def testTransactions(self):
		return self.kreds.transactions()

	def testTransaction(self,TXID=False): # Disabled in test
		pass
#		return self.kreds.transaction(TXID)

	def testWithdraws(self):
		return self.kreds.withdraws()

	def testWithdraw(self,ADDRESS=False,AMT=False,FEE=False): # Disabled in test
		pass
#		return self.kreds.withdraw()

	def testAccount(self): # Disabled in test
		pass
#		return self.kreds.account()

	def testCredit(self,ACCOUNT=False,AMT=False): # Disabled in test
		pass
#		return self.kreds.credit(ACCOUNT,AMT)

if __name__ == "__main__":
	unittest.main()
