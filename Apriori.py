import pandas as pd
from apyori import apriori
#importing the dataset
dataset=pd.read_excel('Invoice_Dataset_v2.xlsx')
doi=dataset[['BillingAddressErpId','ErpProductDesc']]
uniqerpids=doi.BillingAddressErpId.unique()
noofrows=len(doi.index)
transactions=[]
for i in uniqerpids:
    mylist=[]
    for j in range(noofrows):
        if i==int(doi.iloc[j,0]):
            mylist.append(doi.iloc[j,1])
    if len(mylist)>0:
        transactions.append(mylist)

#Traing data on Apriori Model
rules=apriori(transactions, min_support=0.02, min_confidence=0.3)
#Visualising the results
results=list(rules)
for item in results:
    pair = item[0]
    items = [x for x in pair]
    if len(items)>1:
        print("Rule: " + items[0] + "," + items[1],",Supp: " + str(item[1]),",Conf: " + str(item[2][0][2]),",Lf: " + str(item[2][0][3]))
