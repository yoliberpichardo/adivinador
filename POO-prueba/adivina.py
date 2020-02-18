######## adivina ######
from os import system
class adivina:
    def __init__(self):
        self.lives = 5
        self.sentence = input("enter sentence: ")
        self.cifr_sentence = ""
        self.sentence_enter = self.sentence
        self.letter_array = []
        self.letter_result = ""
    
    def codificar_sentence(self):
        system('cls')
        for letter in self.sentence_enter:
            if letter != ' ':
                self.cifr_sentence += '*'
            else:
                self.cifr_sentence += ' '
        return self.cifr_sentence+"\n"    
        
    def veri_sentence(self):
        while self.lives > 1:
            print(self.lives * "❤ ")   
            enter_letter_comp = input("enter a letter: ")
            if enter_letter_comp in self.sentence:
                for letter in self.cifr_sentence:
                    self.letter_array.append(letter)
                
                
                for letter_inter in range(0,len(self.sentence_enter)):
                    if self.sentence_enter[letter_inter] == enter_letter_comp:
                        self.letter_array[letter_inter] = enter_letter_comp
                
                       
                        
                for lett in self.letter_array:
                    self.letter_result += lett
                
                
                if self.letter_result == self.sentence:
                    print('you win')
                    break
            else:
                self.lives -= 1
           
            print(self.letter_result)
            self.letter_result = ''
            self.cifr_sentence = ''

game = adivina()
system('cls')
print(game.codificar_sentence())
print(game.veri_sentence())