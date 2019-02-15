# -*-coding:utf-8-*-
import sys
import os
play = True
while play == True:
    def main():
        f = raw_input("Δώστε το όνομα του αρχείου: ")
        if os.path.isfile(f):
            infile = open(f, "r")
            outfile = open("newfile.txt", "w")
            UNI = raw_input("Περιλαμβάνει unicode χαρακτήρες το αρχείο σας; Y/N ").capitalize()
            if UNI == "Y":
                #Αν επιλέξει ο χρήστης κρατάει την πρώτη σειρά με # (συνήθως unicode)
                outfile.write(infile.readline())
            else:
                pass
            for line in infile:
                #για κάθε γραμμή κειμένου ελέγχει αν ξεκινάει απο #
                #αφου πρώτα αγνοεί τα κενά
                if not line.lstrip().startswith("#"):
                    outfile.write(line)
            infile.close()
            outfile.close()
            #σβήνει το αρχικό αρχείο και μετονομάζει το νέο στο όνομα του αρχικού
            os.remove(f)
            os.rename("newfile.txt", f)
            print "Τα σχόλια διαγράφηκαν επιτυχώς!"
        else:
            print "Το αρχείο που δώσατε δεν υπάρχει."
    main()
    stop = raw_input("Πατήστε R για επανάληψη ή X για έξοδο: ").capitalize()
    if stop == "R":
        play = True
    elif stop == "X":
        play = False
if stop == "X":
        print("Αντίο.")
        sys.exit(-1)
