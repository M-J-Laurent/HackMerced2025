# from multiprocessing import freeze_support
# from dask.distributed import Client

# client = Client()
# import modin.pandas as pd
import pandas as pd

import os
import traceback
# must run script in project root directory

def fastCleanYearlyReport(year):
    try:
        files= os.listdir(".\Data\YearlyReports\Raw")
        path990=''
        pathEZ=''
        db990=None
        dbEZ=None
        cleanData990=None
        cleanDataEZ=None

        # check file type
        type=''
        if f"{year}eofinextract990.dat" in files: 
            path990 = f".\Data\YearlyReports\Raw\{year}eofinextract990.dat"
            pathEZ = f".\Data\YearlyReports\Raw\{year}eofinextractez.dat"
            type="dat"
            db990=pd.read_csv(path990, delimiter="\s+", nrows=1)
            dbEZ=pd.read_csv(pathEZ, delimiter="\s+", nrows=1)
        elif f"{year}eofinextract990.xlsx" in files:
            path990 = f".\Data\YearlyReports\Raw\{year}eofinextract990.xlsx"
            pathEZ = f".\Data\YearlyReports\Raw\{year}eofinextractez.xlsx"
            type="excel"
            db990=pd.read_excel(path990, nrows=1)
            dbEZ=pd.read_excel(pathEZ,nrows=1)
        else:
            return [False,f"file type error {year}"]
    
        
        # check column case
        change990=False
        changeEZ=False
        if "ein" in db990.columns:
            change990=True
        elif "EIN" not in db990.columns:
            return [False,f"column error {year}"]

        if "ein" in dbEZ.columns:
            changeEZ=True
        elif "EIN" not in dbEZ.columns:
            return [False,f"column error {year}"]
        
        print(f"Found column case and file types for {year}")


        #store the data we need
        if change990 and changeEZ:
            if type=="excel":
                db990 = pd.read_excel(path990, usecols=["ein", "totrevenue"])
                dbEZ= pd.read_excel(pathEZ, usecols=["ein", "totrevnue"])
                db990 = db990.rename(columns={"ein": f"EIN"})
                dbEZ = dbEZ.rename(columns={"ein": f"EIN"})
            else:
                db990 = pd.csv(path990, delimiter="\s+", usecols=["ein", "totrevenue"])
                dbEZ= pd.csv(pathEZ, delimiter="\s+", usecols=["ein", "totrevnue"])
                db990 = db990.rename(columns={"ein": f"EIN"})
                dbEZ = dbEZ.rename(columns={"ein": f"EIN"})
        elif change990:
            if type=="excel":
                db990 = pd.read_excel(path990, usecols=["ein", "totrevenue"])
                dbEZ= pd.read_excel(pathEZ, usecols=["EIN", "totrevnue"])
                db990 = db990.rename(columns={"ein": f"EIN"})
            else:
                db990 = pd.csv(path990, delimiter="\s+", usecols=["ein", "totrevenue"])
                dbEZ= pd.csv(pathEZ, delimiter="\s+", usecols=["EIN", "totrevnue"])
                db990 = db990.rename(columns={"ein": f"EIN"})
        elif changeEZ:
            if type=="excel":
                db990 = pd.read_excel(path990, usecols=["EIN", "totrevenue"])
                dbEZ= pd.read_excel(pathEZ, usecols=["ein", "totrevnue"])
                dbEZ = dbEZ.rename(columns={"ein": f"EIN"})
            else:
                db990 = pd.csv(path990, delimiter="\s+", usecols=["EIN", "totrevenue"])
                dbEZ= pd.csv(pathEZ, delimiter="\s+", usecols=["ein", "totrevnue"])
                dbEZ = dbEZ.rename(columns={"ein": f"EIN"})
        else:
            if type=="excel":
                db990 = pd.read_excel(path990, usecols=["EIN", "totrevenue"])
                dbEZ= pd.read_excel(pathEZ, usecols=["EIN", "totrevnue"])
            else:
                db990 = pd.csv(path990, delimiter="\s+", usecols=["EIN", "totrevenue"])
                dbEZ= pd.csv(pathEZ, delimiter="\s+", usecols=["EIN", "totrevnue"])

        cleanData990=db990
        cleanDataEZ=dbEZ
        print(f"Stored data and renamed columns in pandas db for {year}")

        

        #handle data
        cleanData990 = cleanData990.rename(columns={"totrevenue": f"totrevenue_{year}_990"})
        cleanDataEZ = cleanDataEZ.rename(columns={"totrevnue": f"totrevenue_{year}_ez"})

        new_rows = cleanDataEZ[~cleanDataEZ["EIN"].isin(cleanData990["EIN"])]
        cleanData990 = pd.concat([cleanData990, new_rows], ignore_index=True)
        cleanData990[f"totRevenue_{year}"] = cleanData990[f"totrevenue_{year}_990"].fillna(0) + cleanData990[f"totrevenue_{year}_ez"].fillna(0)
        cleanData=cleanData990.drop([f"totrevenue_{year}_990", f"totrevenue_{year}_ez"], axis=1)

        print(f"Combined EZ and 990 columns for {year}")

        cleanData.to_csv(f"./Data/YearlyReports/Cleaned/{year}.csv", index=False)

        print(f"{year} done!!!")
        print()
        return [True,""]
    except Exception :
        return [False, traceback.format_exc()]


def cleanYearlyReport(year):
    try:
        files= os.listdir(".\Data\YearlyReports\Raw")
        path990=''
        pathEZ=''
        db990=None
        dbEZ=None
        # check file type
        if f"{year}eofinextract990.dat" in files: 
            path990 = f".\Data\YearlyReports\Raw\{year}eofinextract990.dat"
            pathEZ = f".\Data\YearlyReports\Raw\{year}eofinextractez.dat"
            db990=pd.read_csv(path990, delimiter="\s+")
            dbEZ=pd.read_csv(pathEZ, delimiter="\s+")
        elif f"{year}eofinextract990.xlsx" in files:
            path990 = f".\Data\YearlyReports\Raw\{year}eofinextract990.xlsx"
            pathEZ = f".\Data\YearlyReports\Raw\{year}eofinextractez.xlsx"
            db990=pd.read_excel(path990)
            dbEZ=pd.read_excel(pathEZ)
        elif f"{year}eofinextract990.csv" in files:
            path990 = f".\Data\YearlyReports\Raw\{year}eofinextract990.csv"
            pathEZ = f".\Data\YearlyReports\Raw\{year}eofinextractez.csv"
            db990=pd.read_csv(path990, delimiter="\s+")
            dbEZ=pd.read_csv(pathEZ, delimiter="\s+")
        else:
            return [False,f"file type error {year}"]
        print(f"Stored data in pandas db for {year}")

        # check column case
        if "ein" in db990.columns:
            db990 = db990.rename(columns={"ein": f"EIN"})
        elif "EIN" not in db990.columns:
            return [False,f"column error {year}"]

        if "ein" in dbEZ.columns:
            dbEZ = dbEZ.rename(columns={"ein": f"EIN"})
        elif "EIN" not in dbEZ.columns:
            return [False,f"column error {year}"]

        # handle the data
        columns_to_keep_990=["EIN","totrevenue"]
        columns_to_keep_EZ=["EIN","totrevnue"]

        cleanData990 = db990[columns_to_keep_990]
        cleanDataEZ = dbEZ[columns_to_keep_EZ]

        cleanData990 = cleanData990.rename(columns={"totrevenue": f"totrevenue_{year}_990"})
        cleanDataEZ = cleanDataEZ.rename(columns={"totrevnue": f"totrevenue_{year}_ez"})

        print(f"Renmed the columns for {year}")

        # cleanData990.to_csv(f"./Data/YearlyReports/intermediate/{year}_990.csv", index=False)
        # cleanDataEZ.to_csv(f"./Data/YearlyReports/intermediate/{year}_EZ.csv", index=False)

        new_rows = cleanDataEZ[~cleanDataEZ["EIN"].isin(cleanData990["EIN"])]
        cleanData990 = pd.concat([cleanData990, new_rows], ignore_index=True)
        cleanData990[f"totRevenue_{year}"] = cleanData990[f"totrevenue_{year}_990"].fillna(0) + cleanData990[f"totrevenue_{year}_ez"].fillna(0)
        cleanData=cleanData990.drop([f"totrevenue_{year}_990", f"totrevenue_{year}_ez"], axis=1)

        print(f"Combined EZ and 990 columns for {year}")

        cleanData.to_csv(f"./Data/YearlyReports/Cleaned/{year}.csv", index=False)

        print(f"{year} done!!!")
        print()
        return [True,""]
    except Exception :
        return [False, traceback.format_exc()]


if __name__ == "__main__":

    year1=input("Input start year: ")
    year2=input("Input end year: ")

    numComplete=0
    returnStatements=[]
    for year in range(int(year1),int(year2)+1):
        returnStatements.append(fastCleanYearlyReport(str(year)))
        if returnStatements[year-int(year1)][0]:
            numComplete+=1


    print(f"{numComplete} out of {int(year2)-int(year1)+1} got completed.")
    if numComplete<(int(year2)-int(year1)+1):
        for i in range(len(returnStatements)):
            print(f"20{i+int(year1)}: {returnStatements[i][1]}")
            print()