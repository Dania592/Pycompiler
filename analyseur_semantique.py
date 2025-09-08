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
        print("resn ", config.NB_VAR)
        # arbre.afficher_arbre()
        self.gennode(arbre)
        print("drop ", config.NB_VAR)
        
    #fait l'analyse sémantique de l'arbre syntaxite avec 0 comme priorité initiale
    def optim(self):
        arbre = self.anaSem()
        # arbre.afficher_arbre_joli()
        return arbre
    
    def anaSem(self):
        arbre = self.analyseur_syntaxique.I()
        arbre.afficher_arbre_joli()
        config.NB_VAR = 0
        self.semNode(arbre)
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
        elif (arbre.type == "node_affect"):
            self.gennode(arbre.fils[1])
            print("dup")
            print("set ", arbre.fils[0].index)
        elif (arbre.type == "node_ref"):
            print("get ", arbre.index)
            
    def begin(self):
        config.TS.append({})
    
    def end(self):
        return config.TS[-1]
    
    def declare(self, name: str) -> dict :
        if(not config.TS and name in config.TS[0]): ## erreur quand TS vide 
            raise Exception(f"La varibale {name} existe deja dans le block")
        sym = {name : {"index" : None, "name" : name}}
        config.TS[0].update(sym)
        return sym 
    
    def find (self , name:str):
        for i in config.TS : 
            if config.TS[i][name]:
                return  i #on veut recuperer les infos de la variable 
        raise Exception(f"la variable n'existe pas")
        
    def semNode(self, arbre : Node):
        if (arbre.type ==  "node_block"):
            self.begin()
            for fils in arbre.fils:
                self.semNode(fils)
            self.end()
        elif (arbre.type == "node_decl"):
            s = self.declare(arbre.chaine)
            config.TS[0][arbre.chaine]["index"] = config.NB_VAR
            config.NB_VAR += 1
        elif (arbre.type == "node_ref"):
            s = self.find(arbre.chaine)
            arbre.index = config.T[s][arbre.chaine]["index"]
        elif (arbre.type == "node_affect"):
            if (arbre.fils[0].type != "node_ref"):
                raise Exception("La partie gauche d'une affectation doit etre une variable")