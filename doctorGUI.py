"""
Program: doctorGUI.py
By: Stephanie | 4/30/2020
GUI-based version of nondirective psychotherapy doctor program from Chapter 5

dependancies: breezypythongui.py
"""

from breezypythongui import EasyFrame
import random

# Global variables and constants
hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours"}

class DoctorGUI(EasyFrame):
	"""Sets up the window and the widgets."""
	def __init__(self):
		EasyFrame.__init__(self, title = "Eliza 1967", width = 640, height = 200)
		self.addLabel(text = "Good morning. I hope you are well today.", row = 0, column = 0)
		self.addLabel(text = "What can I do for you?", row = 1, column = 0)
		self.userText = self.addTextField(text = "", row = 2, column = 0, sticky = "NSEW")
		# Bind the userText field to the ENTER key also
		self.userText.bind("<Return>", lambda event: self.reply())
		self.responseLabel = self.addLabel(text = "", row = 3, column = 0)
		self.addButton(text = "Submit", row = 4, column = 0, command = self.reply)

	def reply(self):
		sentence = self.userText.getText()
		probability = random.randint(1, 4)
		if probability == 1:
			self.responseLabel["text"] =  random.choice(hedges)
		else:
			self.responseLabel["text"] = random.choice(qualifiers) + changePerson(sentence)
		self.userText.setText("")

def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns."""
	# take the sentence and split it into a list of individual words
	words = sentence.split()
	replyWords = []
	# loop through the list of the words the user gave
	for word in words:
		# test the word as a key in the replacements dictionary.
		# if the word is there, the replacement is appended, if not, the original word is appended instead
		replyWords.append(replacements.get(word, word))
	# rebuild the replyWords list into a regular string to return
	return " ".join(replyWords)

def main():
	DoctorGUI().mainloop()

main()