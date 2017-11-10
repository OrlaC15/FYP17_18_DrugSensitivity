import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
pd.set_option('display.max_columns', None) #unlimit display of col
CCLE="resources/CCLE_NP24.2009_Drug_data_2015.02.24.csv" #Cancer Cell Line Encyclopedia data
drugs="resources/ExpandedGeneZSolsCleaned.csv" #Big Data Set
data= pd.read_csv(CCLE)
data.head()
##print(data.describe())
dataZ= pd.read_csv(drugs)
##print(dataZ)
print(data.dtypes)## prints object types