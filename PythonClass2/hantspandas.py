import pandas as pd

supercooldata = pd.read_csv("fakedata.csv")
type(supercooldata)

supercooldata.info()
supercooldata.shape
supercooldata.size

supercooldata.describe()
supercooldata.columns

supercooldata['col3'].value_counts()





