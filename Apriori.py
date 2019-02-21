import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""dataset=pd.read_csv('A:\OutputCleaned.csv', header=None, engine='c')
print (dataset)
"""
import csv
with open('A:\OutputCleaned.csv', 'r') as f:
    reader = csv.reader(f)
    transactions = list (reader)
    #training apriori on dataset
    from apyori import apriori
    #rules=apriori(transactions, min_support=0.5, min_confidence=0.2, min_lift=3, min_length=2)
    rules=apriori(transactions)
    #Visualising the results
    results=list(rules)
    print (results)
"""
transactions=[]
for i in range(0, 88461):
    transactions.append([str(dataset.values[i,0])])

"""

"""
import csv
with open("A:\OutputCleaned.csv", header = None) as f:
    ncols = len(f.readline().split(','))
    nrows = sum(1 for row in f)
print (ncols)
print (nrows)
"""
