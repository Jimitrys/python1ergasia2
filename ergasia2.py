# -*-coding:utf-8-*-
import sys
#για την επανάληψη του προγράμματος
play = True
while play == True:
    import math
    num = 1000001
    #πλήθος φορών που ο αριθμός διαιρείται με το 2:
    pl2 = 0
    #έλεγχος
    while num > 1000000 or num < 1:
        num = int(raw_input("Δώστε έναν αριθμό απο το 1 μέχρι το 1000000: "))
    #Εκτυπώνει πόσες φορές ο αριθμός είναι διαιρέσιμος με το 2
    while num % 2 == 0:
            pl2 += 1
            num = num // 2
    if pl2 > 0:
        print "(2 ** %d)" % (pl2)
    #δημιουργία λίστας (ilist) στην οποία θα προσθέτονται οι αριθμοί που διαπιστώνουμε
    #οτι διαιρούν τέλεια τον num, οσο διαιρείται με αυτούς.
    ilist = [0]
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            ilist.append(i)
            num = num / i
    ilist.remove(0)
    i = 0
    #παραμετροποιούμε το μήκος της λίστας ωστε να λαμβάνουμε υπ΄οψιν το 0
    #σαν αρχή στην επανάληψη
    ilen = int(len(ilist)) - 1
    #για την εμφάνιση των αριθμών που βρίσκονται μία μόνο φορά στη λίστα
    while i < ilen:
        if ilist[i] <> ilist[i+1] and ilist[i] <> ilist[i-1]:
            print "(%d)" % (ilist[i])
            i = i + 1
        else:
            i = i + 1
    if ilen >= 2:
        if ilist[ilen] <> ilist[ilen-2]:
            print "(%d)" % (ilist[len(ilist)-1])
    #ελέγψει αν οποιοςδίποτε αριθμός υπάρχει στην λίστα τουλάχιστον δύο φορές
    #και τον εκτυπώνει κατάλληλα
    for x in range(1, 500000):
            if ilist.count(x) > 1:
                print "(%d ** %d)" % (x, ilist.count(x))
    #όταν δεν γίνεται παραπάνω απλοποίηση εκτυπώνει το "υπόλοιπο" του αρχικού αριθμού
    if num > 2:
        print num
    #για επανάληψη η παύση του προγράμματος
    stop = raw_input("Πατήστε R για επανάληψη ή X για έξοδο: ").capitalize()
    if stop == "R":
        play = True
    elif stop == "X":
        play = False
if stop == "X":
        print("Αντίο.")
        sys.exit(-1)
