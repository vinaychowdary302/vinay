# trans_id
# trans_sender
# trans_receiver
# trans_amount
# trans_mode
# trans_date
# trans_time

transactions = [
    {'trans_id':'123','trans_sender':'teja','trans_receiver':'avi',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
{'trans_id':'123','trans_sender':'varma','trans_receiver':'avi',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
{'trans_id':'123','trans_sender':'avi','trans_receiver':'teja',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
{'trans_id':'123','trans_sender':'hari','trans_receiver':'teja',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
]
mytransaction = []
mytransaction_debit = []
mytransaction_credit = []
def transfer():  #Transaction creation
    pass

def debited():    #Debit details of account
    for trans in transactions:
        if trans['trans_sender']==='teja':
            mytransaction_debit.append(trans)

def credited():   #Credit details
    for trans in transactions:
        if trans['trans_receiver']==='teja':
            mytransaction_credit.append(trans)

def allTransactions():   #Credit details
    for trans in transactions:
        if trans['trans_sender']==='teja' or trans['trans_receiver']==='teja':
            mytransaction.append(trans)
