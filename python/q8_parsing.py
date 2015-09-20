# The football.csv file contains the results from the English Premier League.
# The colums labeled 'Goals and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in 'for' and 'against' goals.


import csv

def read_data(data):
	with open(data) as csvfile:
		reader = csv.DictReader(csvfile)
		low_diff = 9999
		club = ''
		for row in reader:
			print row['Team'], row['Games'], row['Wins'], row['Losses'], row['Draws'],row['Goals'], row['Goals Allowed'], row['Points']
			goal_difference = int(row['Goals']) - int(row['Goals Allowed'])
			abs_goal_difference = abs(int(row['Goals']) - int(row['Goals Allowed']))
			print abs_goal_difference
			if abs_goal_difference < low_diff:
				club = row['Team']
				print club
				low_diff = abs_goal_difference
			else:
				low_diff = low_diff
				print club
# COMPLETE THIS FUNCTION

#def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

#def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION

read_data('football.csv')
