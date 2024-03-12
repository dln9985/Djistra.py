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

diccRel = {}

diccRel['A']={'B':5,'C':3}
diccRel['B']={'A':5,'C':2,'D':4}
diccRel['C']={'A':3,'B':2,'D':6,'E':7}
diccRel['D']={'B':4,'C':6,'E':8}
diccRel['E']={'C':7,'D':8}
diccRel['F']={}

printDicc(diccRel)

print("")