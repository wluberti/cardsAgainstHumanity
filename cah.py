#! /usr/bin/env python3

"""
See the README.md for details!
"""

from os import listdir
from os.path import join, isdir
from random import sample, choice

DATA_DIRECTORY = './data/'
DEFAULT_LANGUAGE = 'EN'

class CardsAgainstHumanity(object):
    def __init__(self):
        print("Welcome to Card Against Humanity")

    def getLanguages(self):
        try:
            dirs = [directory for directory in listdir(DATA_DIRECTORY) if directory.isupper() and isdir(join(DATA_DIRECTORY, directory))]
            self.availableLanguages = dirs
            return dirs
        except OSError:
            exit("Could not read from 'data' directory!")
    
    def setLanguage(self, language):
        if language == '':
            language = 'EN'
        if language.upper() in self.availableLanguages:
            self.language = language.upper()
        else:
            exit('This language is not available')

    def loadFiles(self):
        try:
            with open (join(DATA_DIRECTORY + self.language, "questions.txt")) as questionfile:
                self.questions = questionfile.readlines()
            with open (join(DATA_DIRECTORY + self.language, "answers.txt")) as answersfile:
                self.answers = answersfile.readlines()
        except OSError:
            exit("Could not read the question and answer files for this language:")

    def getQuestion(self):
        return choice(self.questions).replace('_', '<.....>')

    def getAnswers(self, amount):
        return sample(self.answers, amount)


if __name__ == "__main__":
    game = CardsAgainstHumanity()
    game.getLanguages()

    if DEFAULT_LANGUAGE == '':
        language = input("Default language not set. In what language would you like to play? (Available: {},\nNo input will default to: EN) ".format(game.availableLanguages))
        game.setLanguage(language)
    else:
        game.setLanguage(DEFAULT_LANGUAGE)
    game.loadFiles()

    print("=" * 80, end='\n\n')

    print(game.getQuestion())
    for num, answer in enumerate(game.getAnswers(5)):
        print(num +1, ") ", answer.strip(), sep='')


