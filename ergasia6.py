# -*-coding:utf-8-*-
import sys
import random
#για την επανάληψη του προγράμματος
play = True
while play == True:
    
    def main():
        rows = input("Δώστε αριθμό σειρών: ")
        cols = input("Δώστε αριθμό στήλων: ")
        bombs = -1
        while bombs < 0 or bombs > (cols * rows):
            bombs = input("Δώστε αριθμό απο βόμβες: ")
        #Δημιουργία πίνακα απο 0
        board = []

        for x in range(rows):
            board.append(["O"] * cols)
        #Βάζει όσες βόμβες λεει ο χρήστης σε τυχαίες θέσεις
        #και τις απεικονίζει με "*"
        for i in range(0, bombs):
            bomb_row = random.randint(0, rows - 1)
            bomb_col = random.randint(0, cols - 1)
            while (board[bomb_row][bomb_col]) == "*" :
                bomb_row = random.randint(0, rows - 1)
                bomb_col = random.randint(0, cols - 1)
            board[bomb_row][bomb_col] = "*"

        #εμφανίζει τον πίνακα
        def print_board(board):
            for row in board:
                print " ".join(row) # Βάζει κενο ανάμεσα στα 0 και βγαζει τα κομμα.
        print_board(board)
        print "!!!Οι βόμβες είναι οι αστερίσκοι."
    main()
    stop = raw_input("Πατήστε R για επανάληψη ή X για έξοδο: ").capitalize()
    if stop == "R":
        play = True
    elif stop == "X":
        play = False
if stop == "X":
        print("Αντίο.")
        sys.exit(-1)
