from random import randint #heltal slumptalsgenerator

##skapar en lista av de förbjudna bokstav kombinationer för användning
#https://www.transportstyrelsen.se/sv/vagtrafik/Fordon/Om-registreringsskylt/Byte-av-registreringsnummer/Sparrade-bokstavskombinationer/
file_forbidden = open('FORBID.txt')
forbidden_combinations = []
for line in file_forbidden:
    line_clean = line.strip()#tar bort alla vita mellanrum ('\n')
    forbidden_combinations.append(line_clean)

file_forbidden.close()

## Funktion som ger 3 random bokstäver    
alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ThreeRandomChars():
    length = len(alfa)-1 # index börjar från 0, därav 26-1
    first_rand = alfa[randint(0, length)] # tar en bokstav från Alfa enligt någon random tal av ordningen 0 till 25
    second_rand = alfa[randint(0, length)]
    third_rand = alfa[randint(0, length)]
    
    return first_rand + second_rand + third_rand


## Funktion som returnerar bara de kombinationer som är lämpliga genom boolean
def CheckCombinations(checkWord):
    if checkWord in forbidden_combinations: #jämför random bokstäverna med de förbjudna kombinationerna i listan
        return False
    else:
        return True

def ThreeRandomNumb():
    number_combination = str(randint(0,999))#gör till sträng så man kan använda zfill()
    number_combination = number_combination.zfill(3) #lägger till 0 i vänster. vid 99 fås 099, dvs tot bredden är alltid 3
    return number_combination
        

## funktion som generarar random 3 siffror och returnerar checkad bokstavs kombination
def GenerateCharAndNumberCombionation():
    while True:                                 #loopar igenom Nontype, hoppar över det som ger false ovan
        combination = ThreeRandomChars()
        threeNumbers = ThreeRandomNumb()
        if CheckCombinations(combination):      #Kommer enbart ta det som är True från funktionen
            return (combination + ' ' + threeNumbers)

  
##Frågar och sparar infot som variabler

def genPlates():        
    print('Välkommen till bilnummerprogrammet!')

    number_regPlate = int(input('Hur många bilnummer vill du generera? '))#skrivaren kommer skriva en siffra, därav krävs int för strängen

    fil_name = input('Vilken fil ska numren skriva ut på? ')


##genererar antal regg plåtar och ej dubbletter och lägger in regList
    regList = []
    while len(regList) < number_regPlate: 
        regPlates = GenerateCharAndNumberCombionation()
        if regPlates not in regList: #den kollar att inte en dublett förekommer i regList
            regList.append(regPlates) #lägger till regg plåt en i taget i regList tills den eftersökta antalet uppnåts = längden av listan
    #return regList
        
##sparar i en fil, öppnar filen och läser. Tar ut från regList och lägger in filen
    with open(fil_name, 'w+') as file:#'w' en mode hur filen öppnas, vill overwrita med samma namn, a appendar i samma namn, där första item är först i filen, gör en ny fil om igen
        for j in regList:
            file.write( j + '\n' )# skriver in i filen i ny rad

        
## ger respons av svaren
    print('...Nu har ' + str(number_regPlate) + ' bilnummer genererats och skrivits ut på filen ' + fil_name)
    print('Välkommen åter!')


