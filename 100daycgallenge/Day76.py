import random
from symtable import SymbolTableFactory
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYX'
number= '0987654321'
symbol = '[]{}#()*;._-'

all = lower + upper + number + symbol
length = 9
password = ''.join(random.sample(all,length))
print(" The Password You Generated is:", password)