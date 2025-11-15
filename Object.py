class Token :
    """ la classe Token répresente un élément reconnu dans le texte du programme (mot clé, nombre, opérateur, ...)"""
    def __init__(self, type : str, valeur : int, chaine : str):
        self.type = type 
        self.valeur = valeur 
        self.chaine = chaine 

    def print_token(self):
        print(f"Token : [{self.type}, {self.valeur}, {self.chaine}]")

class Node : 
    """ la classe Node represente un bloc ou une opération dans l'arbre syntaxique """
    def __init__(self, type : str, valeur:int = None, chaine:str = None, nbArg : int = None, pointeur : int = None):
        self.type = type 
        if valeur != None :
            self.valeur = valeur 
        elif chaine != None : 
            self.chaine = chaine 
        elif nbArg != None: 
            self.nbArg= nbArg
        elif pointeur != None:
            self.pointeur = pointeur
        self.fils = [] 
        self.index = None 
        
    def ajouter_enfant(self, f:"Node"):
        self.fils.append(f)

    def afficher_arbre(self):
        print("(", self.type, end="")
        for f in self.fils :
            print(" ", end="")
            f.afficher_arbre()
        print(" )", end="")

    def afficher_arbre_joli(self, indent: str = "", last: bool = True):
        info = self.type
        if hasattr(self, "valeur") and self.valeur is not None:
            info += f" [valeur={self.valeur}]"
        if hasattr(self, "chaine") and self.chaine:
            info += f" [chaine='{self.chaine}']"

        branch = "└── " if last else "├── "
        print(str(indent) + str(branch) + str(info))
        indent += "    " if last else "│   "

        for i, f in enumerate(self.fils):
            f.afficher_arbre_joli(indent, i == len(self.fils) - 1)





