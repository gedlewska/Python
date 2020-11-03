x = 2; y = 3; #Drugi średnik jest niepotrzeby, można też zapisać jako: x, y = 2, 3 .
if (x > y): #Nawiasy nie są potrzebne,
    result = x;
else:
    result = y;

for i in "qwerty": if ord(i) < 100: print (i)   #Po : powinny być przejścia do nowych linijek i odpowiednie wcięcia.
                                                #Nie powinno być spacji między print a otwarciem nawiasu.

for i in "axby": print (ord(i) if ord(i) < 100 else i)  #Po : powinno być przejście do nowej linijki i odpowiednie wcięcie.
                                                        #Nie powinno być spacji między print a otwarciem nawiasu.