import pandas as pd

year=input("Input year: ")
path=f".\Data\YearlyReports\Raw\{year}eofinextract990.dat"
db=pd.read_csv(path, delimiter="\s+")

columns_to_keep=["EIN","totrevenue"]
cleanData=db[columns_to_keep]
cleanData.to_csv(f"./Data/YearlyReports/Cleaned/{year}_990.csv", index=False)

print("done!!!")