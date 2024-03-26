def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
    return rez

for skaitlis in range(1, 11, 2):     #range - funkcija, kas skaita skaitļus
    print("mūsu skailis:", skaitlis, "rezultats", rezultats(4, skaitlis))


skaitlis1 = 4
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis:", skaitlis2)
print("rezultats", rezultats(skaitlis1,skaitlis2))

pirmais = "6"

print(pirmais)

vards2 = "ne"

print(pirmais, vards2)