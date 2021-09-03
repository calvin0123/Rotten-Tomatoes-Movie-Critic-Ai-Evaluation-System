"""
File: interactive.py
Name: 
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""
import submission
import util

def main():
	# read weights inside
	weights = {}
	with open('weights', 'r') as f:
		for line in f:
			line = line.strip()
			weights_list = line.split()
			weights[weights_list[0]] = float(weights_list[1])

	# extract the words feature
	feature_extractor = submission.extractWordFeatures
	util.interactivePrompt(feature_extractor, weights)

	# use interactivePrompt


if __name__ == '__main__':
	main()