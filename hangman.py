#HANGMAN
from replit import clear
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
word=input("Enter the word: ").lower()
char_list=list(word)
display=[]

for i in range(len(char_list)):
    display.append("_")

print(display)
end_of_game=False

while not end_of_game:
    guess=input("guess: ")
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(len(char_list)):
        letter=char_list[i]
        if guess==letter:
            display[i]=guess
    

    if guess not in char_list:
        print("no match ")
        lives-=1
        print(stages[lives])
        if lives==0:
            end_of_game=True
            print(f"you lose word= {word}")
    


    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win.")


