# -*-coding:utf-8-*-
import sys
import os
#για επανάληψη
play = True
while play == True:
    
    def main():
        f = raw_input("Δώστε το όνομα του αρχείου: ")
        if os.path.isfile(f):
            #ανοιγμα αρχείου και διαβασμα γραμμων
            infile = open(f, "r")
            outfile = open("newfile.txt", "w")
            UNI = raw_input("Περιλαμβάνει unicode χαρακτήρες το αρχείο σας; Y/N ").capitalize()
            if UNI == "Y":
                #Αν επιλέξει ο χρήστης κρατάει την πρώτη σειρά με # (συνήθως unicode)
                outfile.write(infile.readline())
            else:
                pass

            lines=infile.readlines()

            for line in lines:
                #αν περιεχει #
                if "#" in line:
                    l=line.strip()
                    #για κάθε γραμμή κειμένου ελέγχει αν ξεκινάει απο #
                    #αφου πρώτα αγνοεί τα κενά
                    if not l.startswith("#"):
                        newline = line.split("#")[0]
                        no = "\n"
                        #μετραει τα αφτιά
                        a1=newline.count("'")
                        a2=newline.count('"')
                        #αν ειναι μονο το πληθος το # ειναι μεσα σε αλφαριθμητικο
                        if (a1%2)==1 or a2%2==1:
                        	outfile.write(line)
                        else:
                            #εκτυπώνει στο νέο αρχείο την σειρά χωρίς κενό και μια εξτρα κενή σειρά (no)
                            #για να εχει ακριβώς την ίδια μορφή με το αρχικό
                            outfile.write(newline)
                            outfile.write(no)
                else:
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
