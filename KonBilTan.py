forbidden_file = open('FORBID.txt')
forbComb = []

for line in forbidden_file :
    line_clean = line.strip()
    forbComb.append(line_clean)


def AlphaCheck(regAlpha):
    if regAlpha[0:3].isupper() and regAlpha[0:3] not in forbComb:
        return True
    else:
        return False
        
def NumberCheck(regNumber):
    if regNumber[4:7].isdigit() and regNumber[3] == ' ':
        return True
    else:
        return False

def checkByType():
    regPlate = input(('Skriv bilnummer, 3 bokstäver och 3 siffror: '))   

    if AlphaCheck(regPlate) and NumberCheck(regPlate) is True:
        print(regPlate + '  ' + 'OK')
        
    else:
        print(regPlate + '  ' + 'Otillåten kombination')
        
  
