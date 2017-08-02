import time
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "../euroSoccer/input/"
database = path + 'database.sqlite' 
conn = sqlite3.connect(database)

player_data = pd.read_sql('SELECT * FROM Player;', conn)
player_attributes = pd.read_sql('SELECT * FROM Player_Attributes', conn)
team_status = pd.read_sql('SELECT * FROM Team', conn)
team_attributes = pd.read_sql('SELECT * From Team_Attributes', conn)
match_data = pd.read_sql('SELECT * FROM Match', conn)

#gg = player_attributes[['overall_rating', 'potential', 'crossing']]
#print gg

print team_attributes['date'][0][3]
