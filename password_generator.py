import string
import random
def password():
    '''cette fonction retourne un mot de passe sécurisé'''
    taille=random.randint(12,20)
    possibilities=string.ascii_letters+string.digits+string.punctuation
    pass_word=''
    for i in range(taille):
        pass_word+=random.choice(possibilities)
    return pass_word
print(password())

    