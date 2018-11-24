from random import randint

print("Selamat Datang di game Tamagochi")
name = input("masukkan nama untuk monstermu? ")
monster = {
    "name" : name,
    "healt" : 300,
    "attack" : 100,
    "defend" : 100,
    "expresion" : 10,
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
    }
}

def startGame():
    print("1. Bermain => untuk menambah ekspresi")
    print("2. Olahraga => untuk menambah nyawa 50 per Olahraga")
    print("3. Makan => untuk menambah nyawa 30 per Makan")
    print("4. Train => untuk menambah attack 100 per Train")
    print("5. Latihan Defend => untuk menambah pertahanmu 100 per Latihan")
    print("6. Perang => untuk mengalahkan musuh")
    print("7. Status => untuk melihat status monstermu")
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

def startPerang():
    pass

def addExpresion():
    monster['expresion'] += 10
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def olahraga():
    if monster['healt'] > 450:
        print("maaf monster anda sudah terlalu lelah untuk olahraga")

        return startGame()
        pass
    monster['healt'] += 50
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def eat():
    if monster['healt'] > 390:
        print("maaf monster anda sudah kenyang")

        return startGame()
        pass
    monster['eat'] += 30
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def train():
    if monster['attack'] > 450:
        print("maaf monster anda sudah lelah untuk berlatih")

        return startGame()
        pass
    monster['attack'] += 100
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def latihanBertahan():
    if monster['defend'] > 450:
        print("maaf monster anda sudah lelah untuk berlatih")

        return startGame()
        pass
    monster['defend'] += 100
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def perang():
    startPerang()
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

def status():
    print(monster)
    main = input("ayo main? y/n : ")
    if main == 'y':
        startGame()
        pass
    pass

startGame()
