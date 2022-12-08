from PyQt5.QtWidgets import *
from view import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the gui and selects a random word from the list
        """
        super().__init__(*args, **kwargs)
        self.allowed_errors = 6
        self.setupUi(self)
        self.pushButton_reset.clicked.connect(lambda: self.reset())
        self.pushButton_submit.clicked.connect(lambda: self.submit())
        with open('wordlist.txt', 'r') as file:
            self.words = file.readlines()
        self.word = random.choice(self.words)[:-1]
        self.guesses = []
        self.word_temp = ''

    def submit(self) -> None:
        """
        Handles guesses sent to the game. Determines whether they are correct and whether the player has won
        :return:
        """
        self.label_message.setText('')
        if not self.entry_guess.text().isalpha() or len(self.entry_guess.text()) != 1:
            self.label_message.setText(f'Guesses must be single letters')
        else:
            self.guesses.append(self.entry_guess.text().lower())
            self.word_temp = ''
            for letter in self.word:
                if letter.lower() in self.guesses:
                    self.word_temp += f'{letter} '
                else:
                    self.word_temp += '_ '
            self.label_word.setText(self.word_temp)

            if self.entry_guess.text().lower() not in self.word.lower():
                self.label_picture.setPixmap(QtGui.QPixmap(f'Hangman{8 - self.allowed_errors}.png'))
                self.allowed_errors -= 1
                if self.allowed_errors == 0:
                    self.label_message.setText(f'Game over! The word was {self.word}')

            if '_' not in self.label_word.text():
                self.label_message.setText(f'You Win! The word was {self.word}')


    def reset(self) -> None:
        """
        Resets the picture and text boxes, selects a new word
        """
        self.word = random.choice(self.words)[:-1]
        self.allowed_errors = 6
        self.word_temp = ''
        self.guesses = []
        self.label_picture.setPixmap(QtGui.QPixmap(f'Hangman1.png'))
        self.label_message.setText('')
        self.label_word.setText('')
        self.entry_guess.setText('')


