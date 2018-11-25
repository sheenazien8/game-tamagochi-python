from random import randint

print("Selamat Datang di game Tamagochi")
name = input("masukkan nama untuk monstermu? ")
monster = {
    "name" : name,
    "healt" : 300,
    "attack" : 100,
    "defend" : 100,
    "expression" : 10,
    "special" : 10,
    "weapon" : {
            'sword' : 50 ,
            'gun' : 30 ,
            'punch' : 10 ,
            'special' : 100
        }
}

musuh = {
    1:{
        "name" : "paul" ,
        "healt" : randint(200,500),
        "attack" : randint(200,500),
        "defend" : randint(200,500),
         "weapon" : {
            'sword' : randint(0,100) ,
            'gun' : randint(0,50) ,
            'punch' : randint(0,10) ,
            'special' : 100
        }
    },
    2:{
        "name" : "bobi" ,
        "healt" : randint(200,500),
        "attack" : randint(200,500),
        "defend" : randint(200,500),
         "weapon" : {
            'sword' : randint(0,100) ,
            'gun' : randint(0,50) ,
            'punch' : randint(0,10) ,
            'special' : 100
        }
    },
    3:{
        "name" : "zaky" ,
        "healt" : randint(200,500),
        "attack" : randint(200,500),
        "defend" : randint(200,500),
         "weapon" : {
            'sword' : randint(0,100) ,
            'gun' : randint(0,50) ,
            'punch' : randint(0,10),
            'special' : 100
        }
    }
}

def startGame():
    print("1. Menu => untuk mulai bermain")
    print("2. Status => untuk melihat status monstermu")
    list = input("silahkan pilih menu ")

    if list == '1':
        print("1. Bermain => untuk menambah ekspresi")
        print("2. Olahraga => untuk menambah nyawa 50 per Olahraga")
        print("3. Makan => untuk menambah nyawa 30 per Makan")
        print("4. Train => untuk menambah attack 100 per Train")
        print("5. Latihan Defend => untuk menambah pertahanmu 100 per Latihan")
        print("6. Perang => untuk mengalahkan musuh")
        print("7. Status => untuk melihat status monstermu")
    elif list == '2':
        status()
    else:
        print("maaf nggak ada menu yang anda pilih")
        startGame()
        pass
    menu = input("silahkan pilih menu " + name + " ")

    if menu == '1':
        addExpresion()
    elif menu == '2':
        olahraga()
    elif menu == '3':
        eat()
    elif menu == '4':
        train()
    elif menu == '5':
        latihanBertahan()
    elif menu == '6':
        perang()
    elif menu == '7':
        status()
        pass
def menyerang(attack, defend):
    print('kamu akan menyerang ', defend['name'])
    number = 1;
    for weap in monster['weapon']:
        print(number, weap)
        number += 1
        pass

    weapon = input("pilih senjata untuk menghancurkan "+ defend['name'] + " ")
    if weapon == '1':
        attack += monster['weapon']['sword']
    elif weapon == '2':
        attack += monster['weapon']['gun']
    elif weapon == '3':
        attack += monster['weapon']['punch']
    elif weapon == '4':
        attack += monster['weapon']['special']
        pass

    if monster['attack'] > defend['defend']:
        print(defend['name'] , ' = ' ,defend['healt'])
        print(monster['name'] , ' = ' ,monster['healt'])
        print("setelah melakukan penyerangan ini hasilnya")
        print("===============================================")
        defend['healt'] -= monster['attack'] - defend['defend']
        print(defend['name'] , ' = ' ,defend['healt'])
        print(monster['name'] , ' = ' ,monster['healt'])
        print('kamu menang dalam pertandingan ini', monster['name'])
    elif monster['attack'] < defend['defend']:
        print(defend['name'] , ' punya nyawa = ', + defend['healt'])
        print(monster['name'] , ' punya nyawa = ' , monster['healt'])
        print("setelah melakukan penyerangan ini hasilnya")
        print("===============================================")
        monster['healt'] -= defend['defend'] - monster['attack']
        print(defend['name'] , ' punya nyawa = ' , defend['healt'])
        print(monster['name'] , ' punya nyawa = ' , monster['healt'])
        print('kamu kalah dalam pertandingan ini', monster['name'])
    else:
        print('salah')
        pass

    if defend['healt'] > 0:
        print('nyawa ' + defend['name'] + ' masih tersisa ayo serang lagi')
        return
    else:
        print('kamu sudah mengalahkan '+ defend['name'])
        main = input("ayo main? y/n : ")
        if main == 'y':
            startGame()
        else:
            exit()
            pass
        pass
    pass


def startPerang():
    print("1. Menyerang")
    print("2. Bertahan")
    perang = input("bertahan atau menyerang? ")
    if perang == '1':
        menyerang(monster['attack'], musuh[randint(1,3)])
    elif perang == '2':
        bertahan(musuh[randint(1,3)], monster['defend'])
        pass
    pass

def addExpresion():
    if monster['expresion'] >= 100:
        print("maaf monster anda sudah terlalu senang")
        return startGame()
    monster['expresion'] += 10
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
    else:
        exit()
        pass
    pass

def olahraga():
    if monster['healt'] >= 450:
        print("maaf monster anda sudah terlalu lelah untuk olahraga")
        return startGame()
        pass
    monster['healt'] += 50
    lagi = input("olahraga lagi? y/n: ")
    if lagi == 'y':
        return olahraga()
        pass
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
    else:
        exit()
        pass
    pass

def eat():
    if monster['healt'] >= 390:
        print("maaf monster anda sudah kenyang")
        return startGame()
        pass
    monster['eat'] += 30
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
    else:
        exit()
        pass
    pass

def train():
    if monster['attack'] >= 450:
        print("maaf monster anda sudah lelah untuk berlatih")
        return startGame()
        pass
    monster['attack'] += 100
    lagi = input("train lagi? y/n: ")
    if lagi == 'y':
        return train()
        pass
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
    else:
        exit()
        pass
    pass

def latihanBertahan():
    if monster['defend'] >= 450:
        print("maaf monster anda sudah lelah untuk berlatih")
        return startGame()
    else:
        exit()
        pass
    monster['defend'] += 100
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def perang():
    startPerang()
    if perang == 'y':
        return startPerang()
    else:
        pass
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
    else:
        exit()
        pass
    pass

def status():
    print(monster)
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
    else:
        exit()
        pass
    pass

startGame()
