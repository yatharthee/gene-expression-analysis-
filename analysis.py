import pandas as pd 
import matplotlib.pylot as plt 

data = pd.read_csv("gene_data.csv")

print(data.head())
print(data.describe())

data.iloc(:,0).plot(kind="hist", bins=20)
plt.title("Gene Expression Dsitribution")
plt.show()
