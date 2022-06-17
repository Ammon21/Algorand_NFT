from textwrap import indent
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import PaymentTxn

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print('My address: {}'.format(address))
    print('My private key: {}'.format(private_key))
    print('My passphrase: {}'.format(mnemonic.from_private_key(private_key)))


#generate_algorand_keypair()

My_address = 'VW27HXWEIEYOZ6SWTX3SMLVQLG2IGH5VZJBCFXHQ4EY2E2L4IVBSXOH4QU'
My_privatekey = '8zrRfaEPOsocfqmXCpWCh/kDZyp4qUcx8JwOtIiNCRKttfPexEEw7PpWnfcmLrBZtIMftcpCItzw4TGiaXxFQw=='
#My passphrase

def first_transaction(private_key, my_address):
    algod_address = 'http://localhost:4001'
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
    
    params = algod_client.suggested_params()
    params.flat_fee = True 
    params.fee = 1000
    receiver = 'DISPE57MNLYKOMOK3H5IMBAYOYW3YL2CSI6MDOG3RDXSMET35DG4W6SOTI'
    note = 'Hello World'.encode()

    unsigned_txn = PaymentTxn(my_address, params, receiver, 1000000, None, note ) 

    signed_txn = unsigned_txn.sign(private_key)

    txid = algod_client.send_transaction(signed_txn)
    print('Succesfully sent transaction with txid: {}'.format(txid))
    

first_transaction(My_privatekey, My_address)
