import random

world_list = []
with open('wordle-allowed-guesses.txt') as file:
    for line in file:
        world_list.append(line)
file.close()

answer = random.choice(world_list)

in_word = []
correct_letter = '_____'

def Check_answer(x):
    return x == answer

def Check_correct_positions(x):
    position = 0
    for letter in x:
        if letter in answer:
            in_word.append(letter)
        if x[position] == answer[position]:
            correct_letter[position] = letter
        position += 1
    in_word_checked = []
    for letter in in_word:
        if letter not in in_word:
            in_word_checked.append(letter)
    in_word = in_word_checked
def Check_valid_answer(x):
    return x == world_list

Win = False
guess_count = 0
while guess_count <= 6 and Win == False:
    Guess = input('Enter first guess >> ')
    if Check_answer(Guess) == True:
        Win = True
    else:
        Check_correct_positions(Guess)
    print('Correct letters so far:' + correct_letter)
    print('Letters in word:' + in_word)
    guess_count +=1
if win == True:
    print ('You win.')
else:
    print ('You Lose. Answer was ' + answer + '.')



