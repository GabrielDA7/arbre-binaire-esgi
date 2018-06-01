
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
        return self.gauche

    """ Retourne la valeur du fils droite """
    def FilsDroite(self):
        if(self.estVide()):
            return self.valeur
        return self.droite

    """ Retourne un boolean determinant si le noeud n'a aucun fils """
    def estFeuille(self):
        if((self.FilsGauche() == None) and (self.FilsDroite() == None)):
            return True
        return False

    """ Retourne un boolean determinant si le noeud a au moins 1 fils """
    def estNoeudInterne(self):
        if(self.estFeuille()):
            return False
        return True

    """ Retourne un boolean determinant si le noeud a deux fils """
    def estDouble(self):
        return((self.gauche is not None) and (self.droite is not None))

    """ Retourne un boolean determinant si le noeud a un seul fils """
    def estSimple(self):
        if((self.gauche is None) and (self.droite is not None)):
            return True
        if((self.gauche is not None) and (self.droite is None)):
            return True
        return False


    """ Permet de construire l'abre """
    @staticmethod
    def creer(A=None):
            A = Noeud()
            valeur = raw_input("Entrez la valeur du noeud : ")
            if(valeur != None and valeur != ""):
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
    		if(self.gauche != None):
    			return str(self.valeur)+"("+self.gauche.afficher()+";)"
    		if(self.droite != None):
    			return str(self.valeur)+"(;"+self.droite.afficher()+")"
    		return str(self.valeur)

    """ Retourne la taille de l'abre """
    def taille(self):
        if(self.valeur == None):
        	return 0
        if(self.FilsGauche() != None):
            tailleGauche = self.FilsGauche().taille()
        else:
            tailleGauche = 0
        if(self.FilsDroite() != None):
            tailleDroite = self.FilsDroite().taille()
        else:
            tailleDroite = 0
    	return 1 + tailleGauche + tailleDroite

    """ Retourne la hauteur de l'abre """
    def hauteur(self):
        if(self.estVide()):
            return -1
        if(arbre.estFeuille()):
            return 0
        if(self.FilsGauche() != None):
            hauteurGauche = self.FilsGauche().hauteur()
        else:
            hauteurGauche = -1
        if(self.FilsDroite() != None):
            hauteurDroite = self.FilsDroite().hauteur()
        else:
            hauteurDroite = -1
        return 1 + max(hauteurGauche,hauteurDroite)

    """ Retourne un boolean determinant si l'abre est équilibré """
    def estEquilibre(self):
        if(self.estVide()):
            return True
        if(self.FilsGauche() != None):
            hauteurGauche = self.FilsGauche().hauteur()
            equilibreG = self.FilsGauche().estEquilibre()
        else:
            hauteurGauche = 0
            equilibreG = True
        if(self.FilsDroite() != None):
            hauteurDroite = self.FilsDroite().hauteur()
            equilibreD = self.FilsDroite().estEquilibre()
        else:
            hauteurDroite = 0
            equilibreD = True
        if(abs(hauteurGauche - hauteurDroite) <= 1 and equilibreG and equilibreD):
            return True
        return False;

    """ Retourne les valeurs des noeuds d'un arbre dans l'ordre du parcour prefix (r, g, d)"""
    def parcourPrefix(self):
        if (self.estVide()):
            return None
        print arbre.valeur
        if(self.FilsGauche() != None):
            self.FilsGauche().parcourPrefix()
        if(self.FilsDroite() != None):
            self.FilsDroite().parcourPrefix()

    """ Rotation gauche de l'arbre donné en paramètre ( destructive method ) """
    def rotationGauche(self):
        if(self.FilsDroite() == None):
            return self
        arbreBis = self.FilsDroite()
        arbre.droite = arbreBis.FilsGauche()
        arbreBis.gauche = arbre
        return arbreBis


arbre = Noeud.creer()

print("Arbre :  " + arbre.afficher())
print("Parcour Prefix : ")
arbre.parcourPrefix()
print("L'abre est-il vide ? ")
print(arbre.estVide())
print("Taille de l'abre : ")
print(arbre.taille())
print("Hauteur de l'abre : ")
print(arbre.hauteur())
print("L'abre est-il équilibré ? ")
print(arbre.estEquilibre())
print("Rotation gauche de l'abre : ")
arbre = arbre.rotationGauche()
print("Arbre :  " + arbre.afficher())
