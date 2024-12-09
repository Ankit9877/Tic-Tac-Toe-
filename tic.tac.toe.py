
import random

def check_winner(z):
    if ((z[0] == z[1] == z[2] == 'X') or
        (z[3] == z[4] == z[5] == 'X') or
        (z[6] == z[7] == z[8] == 'X') or
        (z[0] == z[3] == z[6] == 'X') or
        (z[1] == z[4] == z[7] == 'X') or
        (z[2] == z[5] == z[8] == 'X') or
        (z[0] == z[4] == z[8] == 'X') or
        (z[2] == z[4] == z[6] == 'X')):
        print("X wins!")
        return True
    elif ((z[0] == z[1] == z[2] == 'O') or
          (z[3] == z[4] == z[5] == 'O') or
          (z[6] == z[7] == z[8] == 'O') or
          (z[0] == z[3] == z[6] == 'O') or
          (z[1] == z[4] == z[7] == 'O') or
          (z[2] == z[5] == z[8] == 'O') or
          (z[0] == z[4] == z[8] == 'O') or
          (z[2] == z[4] == z[6] == 'O')):
        print("O wins!")
        return True
    return False

def check_place(z, n):
    return z[n] == ' '

def board(z):
    print(f"{z[0]} | {z[1]} | {z[2]}")
    print("--+---+--")
    print(f"{z[3]} | {z[4]} | {z[5]}")
    print("--+---+--")
    print(f"{z[6]} | {z[7]} | {z[8]}")

def computer_move(z):
    available_positions = [i for i, spot in enumerate(z) if spot == ' ']
    return random.choice(available_positions)

def tictactoe():
    z = [' ' for _ in range(9)]  
    turn = True  
    i = 0
    while i < 9:
        board(z)
        if turn:
            print("X's turn.")
            try:
                n = int(input("Enter your choice: "))
                if n < 0 or n > 8:
                    print("Invalid position. Choose a number between 0 and 8.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue

            if not check_place(z, n):
                print("Position already taken. Try again.")
                continue
        else:
            print("O's turn (Computer).")
            n = computer_move(z)

        z[n] = 'X' if turn else 'O'
        i += 1

        if check_winner(z):
            board(z)
            return

        turn = not turn

    board(z)
    print("It's a draw!")

tictactoe()
