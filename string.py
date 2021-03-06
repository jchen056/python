# -*- coding: utf-8 -*-
"""string.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JqyS_SPoG8zJa7WbiIWx50j47iKSy4u2
"""

#source: http://justinbois.github.io/bootcamp/2020_fsri/lessons/l08_string_methods.html#The-format()-method
#Indexing and slicing of strings
print("Indexing and slicing of strings")
my_str = 'The Dude abides.'

print(my_str[5])
print(my_str[:6])
print(my_str[::2])
print(my_str[::-1])
#-------------------------

#counting .count() is a method on a string object
# The sequence we want to analyze
seq ='GACAGACUCCAUGCACGUGGGUAUCAUGUC'


# Initialize GC counter
n_gc = 0

# Initialize sequence length
len_seq = 0

# Loop through sequence and count G's and C's
for base in seq:
    len_seq += 1
    if base in 'GCgc':
        n_gc += 1
print("number of GCgc: ",n_gc)
print("total characters in the string: ", len_seq)    
print("length of string: ", len(seq))
# Count G's and C's
seq.count('G') + seq.count('C')

# Substrings of more than one characater
seq.count('GAC')

#-----------------------

#Finding the index of a start codon
#find() method gives the index where the substring argument first appears. 
#But, what if a substring is not in the string? return -1
#find() always returns positive indices if it finds a substring. 
a=seq.find('AUG')
if a>0:
  print("AUG found on the sequence and the index of the start codon is: ",a)
  print("last index of coden:(exclusive) ",a+len("AUG"))
else:
  print("AUG not found")
seq.find('nonsense')
if 'AUG' in seq:
  print("AUG found in sequence")

# find the last instance of the start codon. We basically want to search from the right. 
print(seq.rfind('AUG'))#return index of A

#----------------

#upper and lower cases
print('LeBron James'.lower())
print('Make me aLl caPS.'.upper())

def complement_base(base):
    """Returns the Watson-Crick complement of a base."""
    # Convert to lowercase
    base = base.lower()

    if base == 'a':
        return 'T'
    elif base == 't':
        return 'A'
    elif base == 'g':
        return 'C'
    else:
        return 'G'
#---------------------

print("string is immutable,replace(),upper()...return a new string")
print("RNA: ",seq)
DNA=seq.replace('U', 'T')
print("DNA: ",DNA)
#-----------------------

#join() method
word_tuple = ('The', 'Dude', 'abides.')
' '.join(word_tuple)
print(' '.join(word_tuple))
#list(' '.join(word_tuple))
'* '.join(word_tuple)
#----------------------

#The format() method
my_str = """
Let's do a Mad Lib!
During this bootcamp, I feel {adjective}.
The instructors give us {plural_noun}.
""".format(adjective='truculent', plural_noun='haircuts')
print(my_str)
#Within the string, the name of the kwargs are given in braces. 
#Then, the arguments in the format() method inserts the strings at the places delimited by braces.
print('There are {n:d} states in the US.'.format(n=50)) #d integer
print('Your file number is {n:04d}.'.format(n=23)) #04d:integer with four digits, possibly with leading zeros
print('?? is approximately {pi:f}.'.format(pi=3.14)) #f:float, default to six digits after decimal
print('e is approximately {e:.8f}.'.format(e=2.7182818284590451))
print("Avogadro's number is approximately {N_A:e}.".format(N_A=6.022e23))
print('????? is approximately {eps_0:.16e} F/m.'.format(eps_0=8.854187817e-12))
print('That {thing:s} really tied the room together.'.format(thing='rug'))
#----------------

print('f string')
n_states = 50
file_number = 23
pi = 3.14
e = 2.7182818284590451
N_A = 6.022e23
eps_0=8.854187817e-12
thing = 'rug'

print(f'There are {n_states} states in the US.')
print(f'Your file number is {file_number}.')
print(f'?? is approximately {pi}.')
print(f'e is approximately {e:.8f}.')
print(f"Avogadro's number is approximately {N_A}.")
print(f'????? is approximately {eps_0} F/m.')
print(f'That {thing} really tied the room together.')