x = int(input("Минимальная сумма инвестиций:"))
M = int(input("Сумма долларов у Майка:"))
I = int(input("Сумма долларов Ивана:"))

if M + I >= x: print(1)
elif M >= x and I < x: print ("Mike")
if M < x and I < x: print(0)
if M >= x and I >= x: print(2)
if M < x and I >= x: print ("Иван")