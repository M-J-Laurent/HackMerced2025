import pandas as pd
db=pd.read_csv("cleaned_Data.csv")
db2=pd.read_csv("./YearlyReports/")
columns_check=['NAME']

MergedData = df1.merge(df2[[common_column]], on=common_column, how="inner")
cleanData = cleanData.drop_duplicates(subset="NAME", keep="first")
cleanData.to_csv("cleaned_Data.csv", index=False)