import sys
import json
import pandas as pd
# import matplotlib.pyplot as plt

# from JsonParser import GetSemanticsFromJson
input_data = sys.stdin.read()
# print("hi")

# grab the key words
Json = json.loads(input_data)
# Json = {
#     "keywords":[
#         "poor",
#         "medical",
#         "ROOts",
#         "word4"
#     ]
# }

def AlgoOnPandas(df):
    datapoints=[]
    percentageSums=[]
    rowLengths=[]
    for i in range(12,24):
        percentageSums.append(df[f"totRevenue_{str(i)}"].sum(skipna=True))
        rowLengths.append(df[f"totRevenue_{str(i)}"].count())
    Y=[percentageSums[i]/rowLengths[i] for i in range(len(percentageSums))]
    # datapoints=[[2000+(i),float(Y[i-12])] for i in range(12,24)]
    data=[[str(2000+(i)),str(float(Y[i-12]))]  for i in range(12,24)]
    datapoints={"data": data}
    # cubicSplineOnData(datapoints)
    return datapoints

# process key words
def GetSemanticsFromJson(JsonData):
    keyWords = JsonData["keywords"]
    df = pd.read_csv("./percentages.csv")
    wordsToCheckFormat = "|".join(keyWords)
    df=df[df["F9_03_PZ_MISSION"].str.contains(f'{wordsToCheckFormat}', case=False, na=False)]
    return df

# linear recursion
dataPoints = AlgoOnPandas(GetSemanticsFromJson(Json))





# print(dataPoints)
# x_values = [pair[0] for pair in dataPoints["data"]]
# y_values = [pair[1] for pair in dataPoints["data"]]

# # Create the line plot
# plt.plot(x_values, y_values)

# # Label the axes and give the plot a title
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('Line Graph from Ordered Pairs')

# # Show the plot
# plt.show()

# # Read input from express server data
# data = sys.stdin.read()

# # Assuming it's JSON, you can parse and process it
# data = json.loads(input_data)


# print(x_values)
# print(y_values)
# print(input_data)
# print(f'{Json} @ ')
print(dataPoints)