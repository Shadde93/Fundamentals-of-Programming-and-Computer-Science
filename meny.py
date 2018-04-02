#!/usr/bin/env python
# -*- coding: utf-8 -*-
from KonBilTan import checkByType
from GenBil import genPlates
from KonBilFil import checkFile

def menu():
    
    print ('1. Generera bilnummer, välj 1 \n2. Kontrollera bilnummer från tangentbordet, välj 2 \n3. Kontrollera bilnummer från fil, välj 3')
    val = int(input('Val: '))

    if val == 1:
        genPlates()
        print()
        menu()
        

    if val == 2:
        checkByType()
        print()
        menu()
               
        
    if val == 3:
        checkFile()
        print()
        menu() 

menu()

