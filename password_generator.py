import string
import random

taille=random.randint(12,20)
possibilities=string.ascii_letters+string.digits+string.punctuation
pass_word=''
for i in range(taille):
    pass_word+=random.choice(possibilities)
print(pass_word)