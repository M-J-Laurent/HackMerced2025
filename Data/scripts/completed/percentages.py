import pandas as pd
# import shutil

path = "Data\FinalCleaned\merged_data.csv"
df = pd.read_csv(path)

counter = 0

store = False
years = ["totRevenue_12", "totRevenue_13", "totRevenue_14", "totRevenue_15", "totRevenue_16", "totRevenue_17", "totRevenue_18", "totRevenue_19", "totRevenue_20", "totRevenue_21", "totRevenue_22", "totRevenue_23"]

for index, row in df.iterrows():
    for col in row.index:
        if not pd.isnull(df.at[index,col]) and (col in years):
            if not store:
                store = df.at[index,col]
                df.at[index,col] = 100
            else:
                value = df.at[index,col] 
                ratio = 100 * (value / store)
                df.at[index,col] = ratio
    store = False

for i in range(12,24):
    df=df.rename(columns={f"tot_revenue_{str(i)}" : f"percent_{str(i)}"})

df=df[df['F9_03_PZ_MISSION'] != 'None']
df.to_csv(f"Data/Percentages/fixedPercentages.csv", index=False)
df.to_csv("ML\Data\Raw\percentages.csv", index=False)

























# year1=int(input("Input start year: "))
# year2=int(input("Input end year: "))

                # shutil.copy("Data\FinalCleaned\merged_data.csv", "Data\Percentages\percentages.csv")


# year1=str(year1+1)
# path="Data\Percentages\percentages.csv"
# df=pd.read_csv(path)
# for year in range(int(year1),int(year2)+1):
    
#     previousYear=str(int(year)-1)
#     df[f"percent_{previousYear}-{year}"] = ((df[f'totRevenue_{year}'] - df[f'totRevenue_{previousYear}']) / (df[f'totRevenue_{previousYear}']+1))*100

# for revenue in range(int(year1)-1,int(year2)+1):
#     df=df.drop(f"totRevenue_{revenue}", axis=1)


# df=df[df['F9_03_PZ_MISSION'] != 'None']
# df.to_csv("Data\Percentages\percentages.csv", index=False)
# df.to_csv("ML\Data\Raw\percentages.csv", index=False)

