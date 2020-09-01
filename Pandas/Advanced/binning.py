import pandas as pd

# load height-weight dataset downloaded from kaggle
data = pd.read_csv("weight-height.csv")

# equal width binning
data["ewb"] = pd.cut(data["Height"], bins=10)
# equal frequency binning
data["efb"] = pd.qcut(data["Height"], q=10)

print(data["ewb"].value_counts())
print(data["efb"].value_counts())
