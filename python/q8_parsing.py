# The football.csv file contains the results from the English Premier League.
# The colums labeled 'Goals and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in 'for' and 'against' goals.


import csv
"""
def read_data(data):
	with open(data) as csvfile:
		reader = csv.DictReader(csvfile)
		table = dict()
		for row in reader:
			print row['Team'], row['Games'], row['Wins'], row['Losses'], row['Draws'],row['Goals'], row['Goals Allowed'], row['Points']
			#reader['Goal Difference'] = float(row['Goals']) - float(row['Goals Allowed'])
			#print table[1]
		#print table[1]
		print reader['Team']
			#row['Goal Difference'] = row['Goals'] - row['Goals Allowed']
		#reader.get('Arsenal',1)
"""
"""
def read_data(data):
	with open(data) as f:
		reader = csv.reader(f, firstrow = 2)
		for row in reader:
			print int(row[5]) - int(row[6])
"""
def read_data(data):
	reader = csv.DictReader(open(data))
	print reader['Arsenal']

# COMPLETE THIS FUNCTION

football = read_data('football.csv')

print football

#def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

#def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
