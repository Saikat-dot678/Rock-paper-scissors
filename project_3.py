import random
your_choise = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors\n"))
choise = random.randint(0,2) #Computer choise as rock-paper-scissor determined by number btw 0 to 2 randomly
Rock = '''
              _____
          ---' ____)___
                 (_____)
                (______)
               (______)
          ---.(_____)
          
          '''
Paper = '''
            _____
        ---' ____)____
              ________)
              __________)
              _________)
        -----.______)
          
          '''
Scissors = ''' 
               ______
            ---'   ___)____
                     ______)
                 __________)
                (_____)
            ---.(___)
            '''
if your_choise == 0:
    print(Rock)
elif your_choise == 1:
    print(Paper)
elif your_choise == 2:
    print(Scissors)
print("Computer choise")
if choise == 0:
    print(Rock)
elif choise == 1:
    print(Paper)
elif choise == 2:
    print(Scissors)
if choise == your_choise:
    print("It's a tie!")
elif choise == 0 and your_choise == 1 or choise == 1 and your_choise == 2 or choise == 2 and your_choise == 0:
    print("You Win!")
elif choise == 1 and your_choise == 0 or choise == 2 and your_choise == 1 or choise == 0 and your_choise == 2:
    print("You Lose!")
