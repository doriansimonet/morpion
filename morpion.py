from random import randint

def aligner(L=[]):
    if L[0][0] == L[0][1] and L[0][0] == L[0][2]:
        #print("horizontal1")
        return True
    if L[1][0] == L[1][1] and L[1][0] == L[1][2]:
        #print("horizontal2")
        return True
    if L[2][0] == L[2][1] and L[2][0] == L[2][2]:
        #print("horizontal3")
        return True
    if L[0][0] == L[1][0] and L[0][0] == L[2][0]:
        #print("vertical1")
        return True
    if L[0][1] == L[1][1] and L[0][1] == L[2][1]:
        #print("vertical2")
        return True
    if L[0][2] == L[1][2] and L[0][2] == L[2][2]:
        #print("vertical3")
        return True
    if L[0][0] == L[1][1] and L[0][0] == L[2][2]:
        #print("diagonale1")
        return True
    if L[0][2] == L[1][1] and L[0][2] == L[2][0]:
        #print("diagonale2")
        return True
    return False
            
#definir la fonction morpion
def morpion ():
    #initialiser un tableau de 3 par 3
    tableau = [['1','2','3'],['4','5','6'],['7','8','9']]
    #initialiser dans first une valeur aléatoire entre 0 ou 1
    first = randint(0,1)
    #si first est égale a 0
    if first == 0:
        #alors aficher "vous commencez, vous êtes les croix"
        print ("vous commencez, vous êtes les croix")
        #tant que trois coordonées alignés ne sont pas égale
        while aligner(tableau) == False:
            #initaliser dans coupJoueurY le retour de l'execution de la fonction input avec comme parametre "veuillez saisir sur quelle ligne vous souhaitez jouez pour ce tour entre 1, 2 et 3 : "
            coupJoueurY = int(input("veuillez saisir sur quelle ligne vous souhaitez jouez pour ce tour entre 0, 1 et 2 : "))
            #initaliser dans coupJoueurX le retour de l'execution de la fonction input avec comme parametre "veuillez saisir sur quelle colonne vous souhaitez jouez pour ce tour entre 1, 2 et 3 : "
            coupJoueurX = int(input("veuillez saisir sur quelle colonne vous souhaitez jouez pour ce tour entre 0, 1 et 2 : "))
            tableau[coupJoueurY][coupJoueurX] = 'X'
            print("tour du bot :")
            if tableau[0][0] == 'X':
                tableau[1][0] = 'O'
            if tableau[0][0] == tableau[0][1] :
                tableau[0][2] ='O'
            if tableau[0][0] == tableau[0][2]:
                tableau[0][1] = 'O'
            if tableau[1][0] == tableau[1][1]:
                tableau[1][2] = 'O'
            if tableau[1][0] == tableau[1][2]:
                tableau[1][1] = 'O'
            if tableau[2][0] == tableau[2][1] :
                tableau[2][2] = 'O'
            if tableau[2][0] == tableau[2][2]:
                tableau[2][1] = 'O'
            if tableau[0][0] == tableau[1][0]: 
                tableau[2][0] = 'O'
            if tableau[0][0] == tableau[2][0]:
                tableau[1][0] = 'O'
            if tableau[0][1] == tableau[1][1]:
                tableau[2][1] = 'O'
            if tableau[0][1] == tableau[2][1]:
                tableau[1][1] = 'O'
            if tableau[0][2] == tableau[1][2]:
                tableau[2][2] = 'O'
            if tableau[0][2] == tableau[2][2]:
                tableau[1][2] = 'O'
            if tableau[0][0] == tableau[1][1]:
                tableau[2][2] = 'O'
            if tableau[0][0] == tableau[2][2]:
                tableau[1][1] = 'O'
            if tableau[0][2] == tableau[1][1]:
                tableau[2][0] = 'O'
            if tableau[0][2] == tableau[2][0]:
                tableau[1][1] = 'O'
            for i in tableau:
                print (i)

    else:
        print("le bot commence, vous avez les ronds")
        tableau[0][2] = 'X'
        
        for i in tableau:
                print (i)

morpion()