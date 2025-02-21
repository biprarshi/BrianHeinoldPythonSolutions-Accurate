# Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.


from random import choice

user_score1 = 0
comp_score1 = 0
iter1 = 0

print('\tWelcome to Rock, Paper, Scissors game!')
print('*'*55+'\n')
while iter1 < 5:
    print(f'Round {iter1+1}:')
    user_choice1 = eval(input('Please enter your choice: Rock(1) Paper(2) or Scissors(3): '))
    if user_choice1 == 1 or user_choice1 == 2 or user_choice1 == 3:
        user_choice2 = 'Rock' if user_choice1 == 1 else 'Paper' if user_choice1 == 2 else 'Scissors'
        comp_choice1 = choice(('Rock', 'Paper', 'Scissors'))
        print(f'User choice is: {user_choice2}.\nComputer choice is: {comp_choice1}.')
        if user_choice2 == comp_choice1:
            print("Its a tie!\n")
            # user_score1 += 1
            # comp_score1 += 1
        elif (user_choice2 == 'Rock' and comp_choice1 == 'Paper') or (user_choice2 == 'Paper' and comp_choice1 == 'Scissors') or (user_choice2 == 'Scissors' and comp_choice1 == 'Rock'):
            comp_score1 += 1
            print("Computer Wins this round!\n")
        else:
            user_score1 += 1
            print('User wins this round!\n')
        iter1 += 1
    else:
        print('Please try again!')

print('\t\t\nFinal Result!')
if user_score1 > comp_score1:
    print(f'User Score: {user_score1}\nComputer Score: {comp_score1}')
    print('\n\t\tUser Wins!')
elif user_score1 < comp_score1:
    print(f'User Score: {user_score1}\nComputer Score: {comp_score1}')
    print('\n\t\tComputer Wins!')
else:
    print(f'User Score: {user_score1}\nComputer Score: {comp_score1}')
    print('\n\t\tIts a tie!')