import pandas as pd

db=pd.read_csv(".\Data\Mission\Cleaned\cleaned_Data.csv")
db2=pd.read_csv("./Data/YearlyReports/Cleaned/23.csv")

columns_check=['ein']

MergedData = db.merge(db2, left_on=['EIN'],right_on=["ein"], how="left")
MergedData.to_csv("Data\Cleaned\merged_Data.csv", index=False)