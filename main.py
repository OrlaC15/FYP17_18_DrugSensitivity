import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

CCLE = "resources/CCLE_NP24.2009_Drug_data_2015.02.24.csv"
GENEZ = "resources/ExpandedGeneZSolsCleaned.csv"
filepath = "resources/output.csv"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
data = pd.read_csv(CCLE)
gene = pd.read_csv(GENEZ)


#
# Replace all spaces in  the  Dataframe columns  with  an underscore
#


data.columns = data.columns.str.replace('\s+', '_')
# Make a dictionary of key,values  compound target
dictionary = data.set_index('Compound').to_dict('list')
# dictionary=dict(zip(data.CCLE_Cell_Line_Name, data.Target))
# print(dictionary)


# Drop Colums and Print

data = data.drop(
    ['Primary_Cell_Line_Name', 'Compound', 'Target', 'Doses_(uM)', 'Activity_Data_(median)', 'Activity_SD', 'Num_Data',
     'FitType'], axis=1)
data.set_index('CCLE_Cell_Line_Name', inplace=True)

# Transpose the dataset CCLE
data = data.transpose()

# data.head()
# print(data.header)

data.shape

# Rename the column and set the index


gene = gene.rename(columns={'Unnamed: 0': 'CCLE_Cell_Line_Name'})
gene.set_index('CCLE_Cell_Line_Name', inplace=True)
# gene.head(10)

names = list(data)
# print(names)


print(gene.shape)

print(data.shape)

df = pd.concat([data, gene], axis=1)


print("After concat")
print(df.shape)
del gene, data
df = df.dropna(axis=1, how='all', thresh=4)
print( "After drop 1")
print(df.shape)
df = df.dropna(axis=0, how='all')
print( "After drop 0")
print(df.shape)
# Write the new dataframe to a csv

df.to_csv(filepath, sep=',')
print( "Finished")
