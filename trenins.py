def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
    return rez

for skaitlis in range(1, 11, 2):     #range - funkcija, kas skaita skaitļus
    for otrs in range (2,11, 2):
      print("pirmais skailis:", skaitlis," otrais skaitlis:", otrs,  "rezultats", rezultats(skaitlis, otrs))

def zvaigznes(skaits):
    for rindasNr in range(1, skaits+1):
       for zvaigzne in range(rindasNr):
          print("*", end="")
          print("")



skaitlis1 = 4
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis:", skaitlis2)
print("rezultats", rezultats(skaitlis1,skaitlis2))

pirmais = "6"

print(pirmais)

vards2 = "ne"

print(pirmais, vards2)