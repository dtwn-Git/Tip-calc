welcome = "Welcome to the tip Calculator."
print(welcome)
total = input("What is the total?\n$")
tip = input("What percentage tip would you like to give?\n(Do not use % sign)\n10, 18, maybe even 25?\n")
squad = input("How many people to split bill?\n")
answer = ("Each person should pay\n$")


ntip = (float(tip) / 100) * float(total)
tt = float(total) + float(ntip)
guest = float(tt) / float(squad)
sguest = str(round(guest, 2))


print(answer + sguest)