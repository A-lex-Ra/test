tick=0
elders=0
olds=list()
diad=list()
a=int(input("Введите год начала диапазона"))
b=int(input("Введите год конца диапазона(не включается)"))
with open("Perepis.txt","r") as f:
    for i in f:
        l=i.split()
        year=int(l[3][6:])
        if year<1978:
            olds.append(l[0])
            elders+=1
        if (year<max(a,b)) and (year>=min(a,b)):
            diad.append(" ".join(l))
        tick+=1
    print('--======== THE',elders,'OLDS ========--')
    for e in olds:
        print(e)
    print()
    print('--======== IN THE DIAPASON FINDED ========--')
    for e in diad:
        print(e)