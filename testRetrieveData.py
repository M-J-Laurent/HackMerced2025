import pandas as pd
URL = "https://github.com/Nonprofit-Open-Data-Collective/machine_learning_mission_codes/blob/master/DATA/MISSION.csv?raw=true"
df = pd.read_csv(URL)
df.to_csv("test.csv",index=False)
print(df.head(200))