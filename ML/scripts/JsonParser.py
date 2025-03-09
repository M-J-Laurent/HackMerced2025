# import json
# import pandas as pd

# def GetSemanticsFromJson(JsonData):
#     keyWords = JsonData["keywords"]
#     df = pd.read_csv(".\ML\Data\Raw\percentages.csv")
#     wordsToCheckFormat = "|".join(keyWords)
#     df=df[df["F9_03_PZ_MISSION"].str.contains(f'{wordsToCheckFormat}', case=False, na=False)]
#     return df
    # df.to_csv("ML\Data\Filtered\SemanticRelatedCharities.csv", index=False)


    #jsonData={"keywords":["word1","word2"]}
    #keywords=["word1","word2"]
    #wordsToCheckFormat="word1|word2"