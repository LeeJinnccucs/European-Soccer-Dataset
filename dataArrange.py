import sqlite3
import numpy as np
import pandas as pd


class dataArrange:

	def __init__(self):
		# get data from sqlite3 database
		path = "../euroSoccer/input/"
		#init dataframe object
		player_data = pd.DataFrame()
		player_attributes = pd.DataFrame()
		team_status = pd.DataFrame()
		team_attributes = pd.DataFrame()
		match_data = pd.DataFrame()

		database = self.path + 'database.sqlite'
		conn = sqlite3.connect(database) 
			
		self.player_data = pd.read_sql('SELECT * FROM Player;', conn)
		self.player_attributes = pd.read_sql('SELECT * FROM Player_Attributes', conn)
		self.team_status = pd.read_sql('SELECT * FROM Team', conn)
		self.team_attributes = pd.read_sql('SELECT * From Team_Attributes', conn)
		self.match_data = pd.read_sql('SELECT * FROM Match', conn)
	
		self.addOutcome()
	#	print self.match_data
	
	def find09team(self):  #test for getting data correctly
		for index,id in enumerate(self.team_attributes['team_api_id']):
			if id == 9930:
				print self.team_attributes['date'][index]

	def findWinner(self, scoreA, scoreB):  #finding game output for training
		if scoreA > scoreB:
			return 1.0
		elif scoreA < scoreB:
			return 0.0
		else:
			return 0.5

	def addOutcome(self): #add game outcome to list that would be used
		result = np.asarray([self.findWinner(a,b)  for a,b in zip(self.match_data["home_team_goal"],  self.match_data["away_team_goal"])])
		self.match_data['Outcome'] = result

def main():
	a = dataArrange()
if __name__ == '__main__':
	main()
