from character import character
from interface import interface
import json
from random import randint


## this is the controller that controls the whole game ##
class game:

	day = 0
	interface1 = None
	character1 = None
	choices = []

	def __init__(self, interface_1, character_1, choice_json):
		## init the class ##
		self.interface1 = interface_1
		self.character1 = character_1
		self.choices = choice_json

		## init the day ##
		self.day = 10

		## display the introduction ##
		self.interface1.introduction()
		return None



	## change character status ##
	def makeChoice(self):
		## load the question and display ##
		choice = randint(0,(len(self.choices)-1))
		print choice
		currentQuestion = self.choices[choice]
		self.interface1.displayQuestion(currentQuestion)

		## get user input ##
		#while(True):
		userDecision = raw_input("please enter your choice by its number:\n")
		userDecision = (userDecision.strip())

		## effect character ##
		effect_status = currentQuestion["effect_stats"][userDecision]
		print effect_status
		self.character1.effect(effect_status)
		
		## day -1 ##
		self.day = self.day - 1

	def ending(self):
		print("oh, I remember your goal is ... nvm")
		print("we do not really track your goal, but... did you reach it?")
		print("Your current status are: ")
		print("health: " + str(self.character1.health))
		print("defense: " + str(self.character1.defense))
		print("attack: " + str(self.character1.attack))
		print("sanity: " + str(self.character1.sanity))
		print("hentai: " + str(self.character1.hentai))
		print("So, you made it? we dont know, you can keep yourself!")


def main():

	## read the choices json ##
	data = []
	with open('choices.json') as data_file:
		data = json.load(data_file)

	interface_one = interface()
	character_one = character()

	game1 = game(interface_one, character_one, data)

	while(game1.day > 0):
		game1.makeChoice()

	game1.ending()
	
	## do some other stuff ##


## main function ##
if __name__ == "__main__":
	main()


