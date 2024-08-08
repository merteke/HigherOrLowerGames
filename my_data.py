import pandas as pd
import os

peak_players={}

df=pd.read_csv("C:\\Users\\PC\\OneDrive - Dokuz Eylül Üniversitesi\\Masaüstü\\python\\100DaysofCode\\HigherLowerGame\\steam_games_all_time_peak.csv",delimiter=",",encoding="utf-8")
count=0
for i in range(len(df["Name"])-1):
    peak_players[df["Name"][i]]=df["All-Time Peak"][i]


    


def random_key():
    import random
    keys=list(peak_players.keys())
    return random.choice(keys)
        
