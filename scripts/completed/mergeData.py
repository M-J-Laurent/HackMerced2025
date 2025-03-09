from multiprocessing import freeze_support
import os
os.environ["MODIN_ENGINE"] = "dask"
from dask.distributed import Client
import modin.pandas as pd


# import pandas as pd

import shutil
import traceback

# must run script in project root directory




def mergeYearwithfinal(year):
    mergePath="Data\FinalCleaned\merged_data.csv"
    currentMerge = pd.read_csv(f"{mergePath}")
    cleanedRevenue = pd.read_csv(f"Data\YearlyReports\Cleaned\{year}.csv")

    MergedData = currentMerge.merge(cleanedRevenue, left_on=['EIN'],right_on=["EIN"], how="left")
    MergedData.to_csv(f"{mergePath}", index=False)



if __name__ == '__main__':
    freeze_support()
    client = Client()

    year1=input("Input start year: ")
    year2=input("Input end year: ")

    numComplete=0
    # returnStatements=[]
    for year in range(int(year1),int(year2)+1):
        mergeYearwithfinal(str(year))