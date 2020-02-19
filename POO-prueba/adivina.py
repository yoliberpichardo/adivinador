######## adivina ######
from os import system
class intro:
    def __init__(self):
        print('\n')
        print('################ Adivina ################')
        print("Bienvenidos, este es el juego adivinar una frase")
        print('el juego consiste en lo siguiente:')
        print('se juega de dos personas, en la cual el primer jugador ')
        print('introduce una frase y el segundo intentara adivinar esta frase.')
        print('#######################################'+'\n')
        print('###### introduce una oración para cifrarla ##########')
        print('###### para que otra persona trate de adivinar ######'+'\n')
        self.enter = input('           ### Presione enter###'+'\n')
    
    def enter_button(self):
        self.enter_butt = self.enter

class adivina:
    def __init__(self):
        self.sentence =  input("Enter sentence: ")
        self.comp_result = self.sentence
        self.cifr_sentence = ""
        self.sentence_enter = self.sentence.lower()
        self.letter_array = []
        self.letter_result = ""       
        self.lives = 5

    def codificar_sentence(self):
        for letter in self.sentence_enter:
            if letter != ' ':
                self.cifr_sentence += '*'
            else:
                self.cifr_sentence += ' '
        return self.cifr_sentence+"\n"    
        
    def veri_sentence(self):
        while self.lives > 0:
            print('Lives:',self.lives * "❤ ")  
            print(self.cifr_sentence)
            enter_letter_comp = input("Enter a letter: ")
            if len(enter_letter_comp) > 1:
                print('### Solo puedes introducir una letra, intenta de nuevo ###'+'\n')
                enter_letter_comp = input("enter a letter: ")
            if enter_letter_comp in self.sentence.lower():
                for letter in self.cifr_sentence:
                    self.letter_array.append(letter)

                for letter_inter in range(0,len(self.sentence_enter)):
                    if self.sentence_enter[letter_inter] == enter_letter_comp:
                        self.letter_array[letter_inter] = enter_letter_comp
                
                for lett in self.letter_array:
                    self.letter_result += lett
                
                if self.letter_result == self.sentence:
                    system('cls')
                    print('La frase era: ',self.letter_result)
                    print('################# you win ################')
                    break
            else:
                self.lives -= 1
            print(self.letter_result+'\n')
            self.letter_result = ''
            self.cifr_sentence = ''
        if self.lives < 1:
            system('cls')
            print('La frase era: ',self.comp_result)
            return '###### You lose ######'
        else:
            return '################# Genial ################'

button = intro()
game = adivina()
print(button.enter_button())
print(game.codificar_sentence()) 
system('cls')
print(game.veri_sentence())