import pandas as pd
# import requests
# import json
import matplotlib.pyplot as plt

# from JsonParser import GetSemanticsFromJson

# grab the key words
Json = {
    "keywords":[
        "poor",
        "medical",
        "ROOts",
        "word4"
    ]
}


def AlgoOnPandas(df):
    datapoints=[]
    percentageSums=[]
    rowLengths=[]
    for i in range(12,24):
        percentageSums.append(df[f"totRevenue_{str(i)}"].sum(skipna=True))
        rowLengths.append(df[f"totRevenue_{str(i)}"].count())
    Y=[percentageSums[i]/rowLengths[i] for i in range(len(percentageSums))]
    datapoints=[[2000+(i),Y[i-12]] for i in range(12,24)]
    # cubicSplineOnData(datapoints)
    return datapoints

# process key words
def GetSemanticsFromJson(JsonData):
    keyWords = JsonData["keywords"]
    df = pd.read_csv(".\ML\Data\Raw\percentages.csv")
    wordsToCheckFormat = "|".join(keyWords)
    df=df[df["F9_03_PZ_MISSION"].str.contains(f'{wordsToCheckFormat}', case=False, na=False)]
    return df

# linear recursion
dataPoints = AlgoOnPandas(GetSemanticsFromJson(Json))
x_values = [pair[0] for pair in dataPoints]
y_values = [pair[1] for pair in dataPoints]

# Create the line plot
plt.plot(x_values, y_values)

# Label the axes and give the plot a title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Line Graph from Ordered Pairs')

# Show the plot
plt.show()
# for i in range(len(dataPoints)):
#     print(dataPoints[i])
