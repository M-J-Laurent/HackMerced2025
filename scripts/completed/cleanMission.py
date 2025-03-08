import pandas as pd

# must run script in project root directory

db=pd.read_csv("test.csv")
columns_to_keep=['EIN','NAME','F9_03_PZ_MISSION']
cleanData=db[columns_to_keep]
cleanData = cleanData.drop_duplicates(subset="NAME", keep="first")
cleanData.to_csv("cleaned_Data.csv", index=False)