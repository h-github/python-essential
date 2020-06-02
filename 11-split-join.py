
s = 'This is a long string with a bunch of words in it.'
print(s)
print(s.split())


s2 = """

This is       a long                 string 


with a bunch           of 

words in it.


"""

print(s2)
print(s2.split())


print(s.split('i'))

l = s.split()
print(' | '.join(l))
