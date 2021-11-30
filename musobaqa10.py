s = int(input("Nechta son kiritasiz.>>>"))
sonlar = []
for i in range(s):
    sonlar.append(input(f" {i+1}- sonni kiriting. "))
sonlar.reverse()
for son in sonlar:
    print(son)







