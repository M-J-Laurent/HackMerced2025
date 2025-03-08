import pandas as pd
# must run script in project root directory

year=input("Input year: ")
path990 = f".\Data\YearlyReports\Raw\{year}eofinextract990.dat"
pathEZ = f".\Data\YearlyReports\Raw\{year}eofinextractez.dat"

db990=pd.read_csv(path990, delimiter="\s+")
dbEZ=pd.read_csv(pathEZ, delimiter="\s+")

columns_to_keep_990=["EIN","totrevenue"]
columns_to_keep_EZ=["EIN","totrevnue"]

cleanData990 = db990[columns_to_keep_990]
cleanDataEZ = dbEZ[columns_to_keep_EZ]

cleanData990 = cleanData990.rename(columns={"totrevenue": f"totrevenue_{year}_990"})
cleanDataEZ = cleanDataEZ.rename(columns={"totrevnue": f"totrevenue_{year}_ez"})

new_rows = cleanDataEZ[~cleanDataEZ["EIN"].isin(cleanData990["EIN"])]

cleanData990 = pd.concat([cleanData990, new_rows], ignore_index=True)
cleanData990[f"totRevenue_{year}"] = cleanData990[f"totrevenue_{year}_990"].fillna(0) + cleanData990[f"totrevenue_{year}_ez"].fillna(0)
cleanData990=cleanData990.drop([f"totrevenue_{year}_990", f"totrevenue_{year}_ez"], axis=1)


cleanData990.to_csv(f"./Data/YearlyReports/Cleaned/{year}.csv", index=False)

print("done!!!")