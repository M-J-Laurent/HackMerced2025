import pandas as pd

# must run script in project root directory

cleanedMission = pd.read_csv("./Data/Mission/Cleaned/cleaned_Data.csv")
cleanedRevenue = pd.read_csv("./Data/YearlyReports/Cleaned/16_990.csv")


MergedData = cleanedMission.merge(cleanedRevenue, left_on=['EIN'],right_on=["EIN"], how="left")
MergedData.to_csv("Data\FinalCleaned\merged_Data_16.csv", index=False)