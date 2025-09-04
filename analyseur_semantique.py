from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Node
import config

#Parcours l'arbre syntaxique pour effectuer des verifications afin de génerer le pseudo code machine
class AnalyseurSemantique:    
    def __init__(self, path):
        self.analyseur_syntaxique = AnalyseurSyntaxique(path) # recupere le resultat de l'analyseur syntaxique
        
    # Méthode appelé pour générer le code machine
    def gencode(self):
        arbre = self.optim()
        # arbre.afficher_arbre()
        self.gennode(arbre)
        
    #fait l'analyse sémantique de l'arbre syntaxite avec 0 comme priorité initiale
    def optim(self):
        arbre = self.analyseur_syntaxique.I()
        # arbre.afficher_arbre_joli()
        return arbre
        
    # Méthode qui parcours récursivement l'arbre de noeud et génère le code machine associé a chaque noeud
    def gennode(self, arbre : Node):
        if (arbre.type ==  "node_const"):  #si le noeud est une constante on l'ajoute a la pile
            print("push ", arbre.valeur)
        elif (arbre.type == "node_not"): # si le noeud correspond a un non logique
            self.gennode(arbre.fils[0]) # on déroule la fonction gennode sur le fils 
            print("not")
        elif (arbre.type == "node_neg"): # si le neoud correspond à une négation arithmétique
            print("push 0")
            self.gennode(arbre.fils[0])
            print("sub")
        elif ( arbre.type in config.op_assembleur.keys() ): # si le type du noeud existe dans notre dictoinnaire 
            prefixe = config.op_assembleur[arbre.type]["prefixe"]
            if prefixe != "" :
                print(prefixe)
            for fils in arbre.fils:
                self.gennode(fils) # on fait de la recursivité sur les fils pour parcourir toute l'expression
            suffixe = config.op_assembleur[arbre.type]["suffixe"]
            if suffixe != "":
                print(suffixe)
            
    def begin(self):
        config.TS.append({})
    
    def end(self):
        return config.TS[-1]
    
    def declare(self, name: str) -> dict :
        if(not config.TS and name in config.TS[0]): ## erreur quand TS vide 
            raise Exception(f"La varibale {name} existe deja dans le block")
        sym = {name : ""}
        config.TS[0].update(sym)
        return sym 
        