import pandas as pd
year="23"
path=f"./Data/YearlyReports/Raw/{year}eoextract990.xlsx"
db=pd.read_excel(path)
columns_to_keep=['ein','tax_pd',"subseccd"]
cleanData=db[columns_to_keep]
# cleanData = cleanData.drop_duplicates(subset="eid", keep="first")
cleanData.to_csv(f"./Data/YearlyReports/Cleaned/{year}.csv", index=False)
print("done!!!")