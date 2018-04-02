
forbidden_file = open('FORBID.txt')
forbKomb = []

for line1 in forbidden_file:
    line_clean1 = line1.strip()
    forbKomb.append(line_clean1)

forbidden_file.close()    


def checkTasks(fil_list):
    
    checkRegList = []    

    for regPlate in fil_list:    
        if len(regPlate) == 7 and regPlate[3] == ' ':
            regNum = regPlate[4:7]
            regAlpha = regPlate[0:3]
            if regNum.isdigit() and regAlpha.isupper():
                if regAlpha in forbKomb:
                    checkRegList.append(regPlate + '  ' + 'Otillåten kombination')
                else:
                    checkRegList.append(regPlate + '  ' + 'OK')
            else:
                checkRegList.append(regPlate + '  ' + 'Otillåten kombination')
        else:
            checkRegList.append(regPlate + '  ' + 'Otillåten kombination')

    return checkRegList            



def checkFile():

    fil_name = input('Filens namn: ')
    fil = open(fil_name)

    fil_list = [] 
    for line in fil:
        line_clean = line.strip()
        fil_list.append(line_clean)
    
    fil_list = filter(None, fil_list) #ignorerar tom rad som None

    fil.close()

    checkedRegList = checkTasks(fil_list)    

    filResNam = input('Vilken fil ska resultatet skrivas ut på? ')

    with open(filResNam, 'w+') as filRes:
        for check in checkedRegList:
            filRes.write(str(check) + '\n' )

    print('...Nu har resultatet skrivits ut på filen ' + filResNam)        
