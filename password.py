"""
Ce programme est un générateur de mot de passe qui demande la longueur du mot de passe
et génère un mot de passe aléatoire contenant des chiffres, des alphabets et des caractères spéciaux.
"""


import string
import random


## characters to generate password from
caractère = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def password():

	print("""        ===================
	Générateur de mot de passe
	""")
	longueur = int(input("Entrez la longueur du votre mot de passe: "))

	random.shuffle(caractère)
	
	password = []
	for i in range(longueur):
		password.append(random.choice(caractère))

	random.shuffle(password)

	print("".join(password))



password()