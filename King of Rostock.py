from random import randrange
origin=['Cultist','Divine','Dusk','Elderwood','Enlightened','Fortune','Moonlight','Ninja','Spirit','Warlord']
classes=['Adept','Assassin','Brawler','Dazzler','Duelist','Hunter','Keeper','Mage','Mystic','Shade','Sharpshooter','Vanguard']
Spieler=['Buschi','Trichter','Timo','Morytz','kAi','JP','ToBIas','Jonathan']
olist=[100]
clist=[100]

def isin(array,value):
    for i in range(0,len(array)):
        if(array[i]==value):
            return True
    return False

def wo(array,value):
    for i in range(0,len(array)):
        if(array[i]==value):
            return i
    return False
        
flag=True
while(flag):
    print('Sind das die Spieler?')
    print(Spieler)
    print('Tippe delete zum Löschen, add zum Hinzufügen oder enter zum bestätigen')
    andern=input('')
    print('')
    if (andern=='add'):
        print('Wen Hinzufügen?')
        Name=input('')
        print('')
        Spieler.append(Name)
    elif(andern=='delete'):
        Flag2=True
        while(Flag2):
            print('Wen Löschen?')
            print(Spieler)
            Name=input('')
            print('')
            if(isin(Spieler,Name)):
                Spieler.pop(wo(Spieler,Name))
                Flag2=False
            else:
                print('Vertippt?')
                print('')
    else:
        flag=False
                             
print('Hier die Ergebnisse:')
print('')      
for i in range(0,len(Spieler)):
    print(Spieler[i]+':')
    
    o=randrange(len(origin))
    while (isin(olist,o)):
        o=randrange(len(origin))
    olist.append(o)
    print(origin[o])
    c=randrange(len(classes))
    while (isin(clist,c)):
        c=randrange(len(classes))
    clist.append(c)
    print(classes[c])
    print(' ')
print('')
print('')
print('Ps:Man kann hochscrollen')
input('Drücke enter zum schließen')