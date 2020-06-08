import random
game = random.choice(['rock','paper','scissors'])
res = str(input('rock, paper or scissors (you can answer with 1,2,3)?: '))
winpc = 'The computer won!'
winplay = 'The player won!'
##decoder para 123
if res == '1':
    res = 'rock'
    print(res)
if res == '2':
    res = 'paper'
    print(res)
if res == '3':
    res = 'scissors'
    print(res)
##empates
if game == res:
    print("It's a draw!")
##pedra vence
if game == 'rock' and res == 'scissors':
    print(winpc)
if game == 'scissors' and res == 'rock':
    print(winplay)
##papel vence
if game == 'paper' and res == 'rock':
    print(winpc)
if game == 'rock' and res == 'paper':
    print(winplay)
##tesoura vence
if game == 'scissors' and res == 'paper':
    print(winpc)
if game == 'paper' and res == 'scissors':
    print(winplay)