from lib import *
import sys

print("")

#dicc={
#    'nom': "Diego",
#   'edad': 18,
#    'tel': {
#        'cel': 5,
#        'fij': 6
#    }
#}

#print( dicc['tel']['cel'] )

diccRel = {
    'A':{'B':5,'C':3},
    'B':{'A':5,'C':2,'D':4},
    'C':{'A':3,'B':2,'D':6,'E':7},
    'D':{'B':4,'C':6,'E':8},
    'E':{'C':7,'D':8},
} 

#diccRel['A']={'B':5,'C':3}
#diccRel['B']={'A':5,'C':2,'D':4}
#diccRel['C']={'A':3,'B':2,'D':6,'E':7}
#diccRel['D']={'B':4,'C':6,'E':8}
#diccRel['E']={'C':7,'D':8}

grafoTest = grafo( )
grafoTest.addArista('A','B',5)
grafoTest.addArista('A','C',3)

grafoTest.addArista('B','A',5)
grafoTest.addArista('B','C',2)
grafoTest.addArista('B','D',4)

grafoTest.addArista('C','A',3)
grafoTest.addArista('C','B',2)
grafoTest.addArista('C','D',6)
grafoTest.addArista('C','E',7)

grafoTest.addArista('D','B',4)
grafoTest.addArista('D','C',6)
grafoTest.addArista('D','E',8)

grafoTest.addArista('E','C',7)
grafoTest.addArista('E','D',8)

origenG = 'A'
destinoG = 'E'
path={}

path[ origenG ]={'-':0}
path[ 'B' ]={'A':5}
path[ 'C' ]={'A':3}

print(grafoTest.Aristas['A'])

print(path)
