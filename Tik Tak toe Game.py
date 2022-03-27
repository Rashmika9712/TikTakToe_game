inputs = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
print("\nPlayer 1 is X & Player 2 is O")

def view(board):
    print(' ----------------\n | ' + board['7'] + '  | ' + board['8'] + '  | ' + board['9'] + '  |')
    print(' ----------------\n | ' + board['4'] + '  | ' + board['5'] + '  | ' + board['6'] + '  |')
    print(' ----------------\n | ' + board['1'] + '  | ' + board['2'] + '  | ' + board['3'] + '  | \n ----------------')

numbers = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def game():
    player = 'X'
    count = 0
    name= "Player 1"


    for i in range(10):
        view(numbers)
        print("It's " + name + " turn. Type place number :")

        uInput = input()
        if uInput == ' ':
            if count ==9:
                print("\nGame Over !\n\n--- Draw ---!")
            else:
                print("Please type your place number !")
        else:
              if numbers[uInput] == ' ':
                 numbers[uInput] = player
                 count += 1
              else:
                 if count !=9:
                    print("Oooops !. This place is already filled.\nChoose another place !")
                 else:
                     print("\nGame Over !\nIt's Draw ---!")
                 continue

        if count >= 5:
            if numbers['7'] == numbers['8'] == numbers['9'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['4'] == numbers['5'] == numbers['6'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['1'] == numbers['2'] == numbers['3'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['1'] == numbers['4'] == numbers['7'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['2'] == numbers['5'] == numbers['8'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['3'] == numbers['6'] == numbers['9'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['7'] == numbers['5'] == numbers['3'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break
            elif numbers['1'] == numbers['5'] == numbers['9'] != ' ':
                view(numbers)
                print("\nGame Over !\n\n" + name + " is won !\n")
                break


        if player == 'X':
            name = "Player 2"
            player = 'O'
        else:
            name = "Player 1"
            player = 'X'

    def play_again():
        end = input("Play Again (y/n) ?")
        replay = end.upper()
        if replay == "Y":
            for solo in inputs:
                numbers[solo] = " "

            game()

    play_again()

game()