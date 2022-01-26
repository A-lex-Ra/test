klass=dict()
subject={"Алгебра":[["","",0,0]],"Геометрия":[["","",0,0]]}

f=open("mat_dv.txt","r")
for i in f:
    s=i.split()
    s[3]=int(s[3])
    s[4]=int(s[4])
    if ((int(s[2]) not in klass) or (s[3]+s[4]>klass[int(s[2])][0][2])):
        klass[int(s[2])]=[[s[0],s[1],s[3]+s[4]]]
    elif (s[3]+s[4]==klass[int(s[2])][0][2]):
        klass[int(s[2])]+=[[s[0],s[1],s[3]+s[4]]]
    if (s[3]>subject["Алгебра"][0][3]):
        subject["Алгебра"]=[[s[0],s[1],s[2],s[3]]]
    elif (s[3]==subject["Алгебра"][0][3]):
        subject["Алгебра"]+=[[s[0],s[1],s[2],s[3]]]
    if (s[4]>subject["Геометрия"][0][3]):
        subject["Геометрия"]=[[s[0],s[1],s[2],s[4]]]
    elif (s[4]==subject["Геометрия"][0][3]):
        subject["Геометрия"]+=[[s[0],s[1],s[2],s[4]]]
for i in klass: print(i,":",klass[i])
for i in subject: print(i,":",subject[i])

