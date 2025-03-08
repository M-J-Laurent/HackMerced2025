import pandas as pd
db=pd.read_csv("test.csv")
columns_to_keep=['EIN','NAME','F9_03_PZ_MISSION']
cleanData=db[columns_to_keep]
cleanData.to_csv("cleaned_Data.csv", index=False)