# coding=utf-8
class Noeud:
    """ Constructeur de la classe Noeud """
    def __init__(self,val = None):
    	self.valeur=val
    	self.gauche=None
    	self.droite=None

    """ Retourne un boolean determinant si le fils est vide """
    def estVide(self):
        return (self.valeur == None)

    """ Retourne la valeur du fils gauche """
    def FilsGauche(self):
        if(self.estVide()):
            return self.valeur
        else:
            return self.gauche

    """ Retourne la valeur du fils droite """
    def FilsDroite(self):
        if(self.estVide()):
            return self.valeur
        else:
            return self.droite

    """ Retourne un boolean determinant si le noeud n'a aucun fils """
    def estFeuille(self):
        if(self.estVide()):
            return False
        elif((self.FilsGauche() == None) and (self.FilsDroite() == None)):
            return True
        else:
            return False

    """ Retourne un boolean determinant si le noeud a au moins 1 fils """
    def estNoeudInterne(self):
        if(self.estFeuille()):
            return False
        else:
            return True

    """ Retourne un boolean determinant si le noeud a deux fils """
    def estDouble(self):
        return((self.gauche is not None) and (self.droite is not None))

    """ Retourne un boolean determinant si le noeud a un seul fils """
    def estSimple(self):
        if((self.gauche is None) and (self.droite is not None)):
            return True
        elif((self.gauche is not None) and (self.droite is None)):
            return True
        else:
            return False


    """ Permet de construire l'abre """
    @staticmethod
    def creer(A=None):
            valeur = input("Entrez la valeur du noeud : ")
            A = Noeud(valeur)
            gauche = ""
            droite = ""
            while((gauche != "oui") and (gauche != "non")):
                gauche = raw_input("Creer un noeud à gauche ? (oui/non) : \n")
            if(gauche == "oui"):
                A.gauche = Noeud.creer(A.gauche)
            while((droite != "oui") and (droite != "non")):
                droite = raw_input("Creer un noeud à droite ? (oui/non) : \n")
            if(droite == "oui"):
                A.droite = Noeud.creer(A.droite)
            return A

    """ Permet d'afficher l'arbre """
    def afficher(self):
    		if(self.estDouble()):
    			return str(self.valeur)+"("+self.gauche.afficher()+";"+self.droite.afficher()+")"
    		elif(self.gauche != None):
    			return str(self.valeur)+"("+self.gauche.afficher()+";)"
    		elif(self.droite != None):
    			return str(self.valeur)+"(;"+self.droite.afficher()+")"
    		else:
    			return str(self.valeur)

""" Retourne la taille de l'abre """
def taille(arbre):
    if(arbre == None):
    	return 0
    else:
    	return 1 + taille(arbre.gauche) + taille(arbre.droite)

""" Retourne la hauteur de l'abre """
def hauteur(arbre):
    if(arbre == None):
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche),hauteur(arbre.droite))

""" Retourne un boolean determinant si l'abre est équilibré """
def estEquilibre(arbre):
    if(arbre == None):
        return True
    tailleGauche = hauteur(arbre.gauche)
    tailleDroite = hauteur(arbre.droite)
    if(abs(tailleGauche - tailleDroite) <= 1 and estEquilibre(arbre.gauche) and estEquilibre(arbre.droite)):
        return True
    return False;

""" Retourne les valeurs des noeuds d'un arbre dans l'ordre du parcour prefix (r, g, d)"""
def parcourPrefix(arbre):
    if (arbre != None):
        print arbre.valeur
        parcourPrefix(arbre.gauche)
        parcourPrefix(arbre.droite)
    else:
        return None

""" Rotation gauche de l'arbre donné en paramètre ( destructive method ) """
def rotationGauche(arbre):
    arbreBis = arbre.droite
    arbre.droite = arbreBis.gauche
    arbreBis.gauche = arbre
    return arbreBis

arbre = Noeud.creer()
print("Arbre :  " + arbre.afficher())
print("Parcour Prefix : ")
parcourPrefix(arbre)
print("L'abre est-il vide ? ")
print(arbre.estVide())
print("Taille de l'abre : ")
print(taille(arbre))
print("Hauteur de l'abre : ")
print(hauteur(arbre))
print("L'abre est-il équilibré ? ")
print(estEquilibre(arbre))
print("Rotation gauche de l'abre : ")
arbre = rotationGauche(arbre)
print("Arbre :  " + arbre.afficher())
