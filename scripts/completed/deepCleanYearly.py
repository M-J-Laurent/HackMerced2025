import pandas as pd

year1=input("Input start year: ")
year2=input("Input end year: ")


def fixDupes(year):
    path=f"Data\YearlyReports\Cleaned\{year}.csv"
    df=pd.read_csv(path)
    df=df.drop_duplicates(subset=["EIN"], keep="first")
    df=df[["EIN", f"totRevenue_{year}"]]
    df.to_csv(f"Data\YearlyReports\Cleaned\{year}.csv", index=False)

for year in range(int(year1),int(year2)+1):
    fixDupes(str(year))
