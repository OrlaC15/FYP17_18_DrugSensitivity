
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
line = plt.figure()

np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")


# draw vertical line from (70,100) to (70, 250)
plt.plot([70, 70], [100, 250], 'k-', lw=2)

# draw diagonal line from (70, 90) to (90, 200)
plt.plot([70, 90], [90, 200], 'k-')

plt.show()
filepath="resources/output.csv"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df= pd.read_csv(filepath)

#rename column
df.rename(columns={'Unnamed: 0': 'Target'})


df.set_index([df.index.values,df['Target'].tolist()])
idx=df.index[df['EC50_(uM)']].value
ec=df.loc(['EC50_(uM)'].values)
#stats= df.Dataframe(['EC50_(uM)','IC50_(uM)','Amax', 'ActArea'],['ZR7530_BREAST.6','143B_BONE','1321N1_CENTRAL_NERVOUS_SYSTEM','22RV1_PROSTATE','42MGBA_CENTRAL_NERVOUS_SYSTEM'])
print(ec)

stats.to_frame
columns = pd.Series(['ZR7530_BREAST.6','143B_BONE','1321N1_CENTRAL_NERVOUS_SYSTEM','22RV1_PROSTATE','42MGBA_CENTRAL_NERVOUS_SYSTEM'])
target=pd.Series([0,1,515,1730,12511],['ZR7530_BREAST.6','143B_BONE','1321N1_CENTRAL_NERVOUS_SYSTEM','22RV1_PROSTATE','42MGBA_CENTRAL_NERVOUS_SYSTEM'])


df.corr(method='pearson', min_periods=1)