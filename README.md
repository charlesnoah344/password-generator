🔐 Générateur de mot de passe sécurisé

Ce script Python permet de générer un mot de passe aléatoire et sécurisé, composé de lettres, chiffres et caractères spéciaux.
Il peut être utilisé pour renforcer la sécurité de vos comptes ou pour des applications nécessitant des identifiants temporaires forts.
📜 Fonctionnalités

    Génère un mot de passe aléatoire à chaque exécution.

    La longueur du mot de passe est choisie aléatoirement entre 12 et 20 caractères.

    Le mot de passe contient un mélange de :

        Lettres minuscules et majuscules (a-z, A-Z)

        Chiffres (0-9)

        Caractères spéciaux (ponctuation)

💡 Exemple d'utilisation

$ python generate_password.py
b@M6*WjYq5z$Lw

🧠 Fonction principale

def password():
    '''cette fonction retourne un mot de passe sécurisé'''

Elle utilise :

    random.randint pour déterminer la taille du mot de passe.

    string.ascii_letters, string.digits et string.punctuation pour les caractères possibles.

    random.choice pour choisir chaque caractère.

🔧 Prérequis

Ce script utilise uniquement des bibliothèques standards de Python, donc aucune installation supplémentaire n’est nécessaire.
📁 Fichier

    generate_password.py : contient le script principal.

📜 Licence

Ce script est libre d'utilisation à des fins personnelles ou éducatives.

✨ Auteur

Développé par Lesno (Charles Noah)
