from dataArrange import dataArrange
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

class teamRating:

	def __init__(self):
		data = None
		team_data = None  #team attributes
		ability_data = None  #ability attributes
		tag_name = None
		game_outcome = None
		#training use data dataframe column name
		column_name = ['team_api_id', 'buildUpPlaySpeed', 'buildUpPlayPassing', 'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 'defencePressure', 'defenceAggression', 'defenceTeamWidth']
		match_dataName = ['date', 'home_team_api_id', 'away_team_api_id']

		self.data = dataArrange()
		self.team_data = self.data.team_attributes
		self.ability_data = self.team_data[self.column_name].astype(float) #get ability value from dataframe
		self.tag_name = self.ability_data.columns.values.tolist()
		self.ability_data['date'] = pd.Series(self.team_data['date'].values, index = self.ability_data.index) #add data column
		self.game_outcome = self.data.match_data['Outcome']
		self.match_teamId = self.data.match_data[self.match_dataName]

	def normalization(self, ability, dropped): #normalizing ability value
#		a = self.ability_data.values
		a = ability.values
		scaler = preprocessing.StandardScaler().fit(a)
		a = scaler.transform(a)
		"""for tag in self.tag_name:
			a = self.ability_data[tag].values
			scaler = preprocessing.StandardScaler().fit(a)
			print scaler.transform(a)"""
		temp = self.column_name[1:] # use [:] to duplicate old list, instead of using = to assign the same reference
		temp.remove(dropped)
		b = pd.DataFrame(a, columns = temp)
		b['date'] = self.team_data['date'].values
		b['team_api_id'] = self.team_data['team_api_id'].values
		return b

#		return  pd.DataFrame(a, columns = self.tag_name)
#	def getTeamAbility():

#	def findFeatureForm(self):
		
	def abilityModel(self, train): #build model *not done yet
#		trainArray = [[item[i] for item in train] for i in range(train[0].size)]
		clf = GaussianNB()
#		print trainArray
		match_len = len(self.match_teamId)
		outcome_len = len(self.game_outcome)
		clf.fit( (train[:train_len/2]), self.game_outcome[:outcome_len/2] )
		prediction = clf.predict(trainArray[train_len/2:])
		print prediction
		return prediction

	def modelArray(self, train): #combining data to the input dataframe needed
		result = []

		for index,row in enumerate(self.match_teamId.iterrows()):
			a = []
			b = []
			b.append(row[1]['date'])
			b.append(row[1]['home_team_api_id'])
			b.append(row[1]['away_team_api_id'])
			c = np.asarray(b).reshape((1,3))
			df = pd.DataFrame(np.asarray(c), columns = self.match_dataName)
#			print row
#			print train
#			print train.iloc[[index]]
			new1_df = pd.merge(df, train.iloc[[index]], how = 'left', left_on=['date', 'home_team_api_id'], right_on = ['date', 'team_api_id'])
#			new1_df = pd.merge(df, train.iloc[[index]], how = "left" ,left_on=['date', 'home_team_api_id'], right_on = ['date', 'team_api_id'])
			new2_df = pd.merge(train.iloc[[index]], df, left_on=['date', 'team_api_id'], right_on = ['date', 'away_team_api_id'])
			print new1_df
#			print new2_df
			new1_df = new1_df.drop(['date', 'team_api_id'], axis = 1)
			new2_df = new2_df.drop(['date', 'team_api_id'], axis = 1)
			a.append(new1_df.values)
			a.append(new2_df.values)
			result.append(a)
		return result

			
def main():
	a = teamRating()
#	for dropf in a.column_name[1:]:
#		c = a.ability_data.drop([dropf, 'date', 'team_api_id'], axis = 1)
#		print c
#		d = a.normalization(c, dropf)
#		print d
	b = []
	for dropC in a.column_name[1:]:
		normalized_data = a.normalization(a.ability_data.drop([dropC, 'date', 'team_api_id'], axis = 1), dropC)
		modelInput = a.modelArray(normalized_data)
#		print modelInput[0]

if __name__ == "__main__":
	main()
