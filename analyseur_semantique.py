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
        self.gennode(arbre)
        print("drop ", config.NB_VAR)
        
    #fait l'analyse sémantique de l'arbre syntaxite avec 0 comme priorité initiale
    def optim(self):
        arbre = self.anaSem()
        return arbre
    
    def anaSem(self):
        arbre = self.analyseur_syntaxique.I()
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
        elif (arbre.type == "node_debug"):
            self.gennode(arbre.fils[0])
            print("dbg")
        elif ( arbre.type in config.op_assembleur.keys() ): # si le type du noeud existe dans notre dictoinnaire 
            prefixe = config.op_assembleur[arbre.type]["prefixe"]
            if prefixe != "" :
                print(prefixe)
            for fils in arbre.fils:
                self.gennode(fils) # on fait de la recursivité sur les fils pour parcourir toute l'expression
            suffixe = config.op_assembleur[arbre.type]["suffixe"]
            if suffixe != "":
                print(suffixe)
        elif (arbre.type == "node_assign"):
            self.gennode(arbre.fils[1])
            print("dup")
            print("set ", arbre.fils[0].index)
        elif (arbre.type == "node_ref"):
            # print("test")
            print("get ", arbre.index)
        elif (arbre.type == "node_drop"):
            self.gennode(arbre.fils[0])
            # erreur psk ici  on droit le nombre de variable et non la vrai valeur
            # arbre.afficher_arbre_joli() 
            # t = self.find(arbre.fils[0].chaine)
            # print(t)
            print("drop 1")
            
        elif arbre.type == "node_cond":
            config.NB_LB += 1
            l = config.NB_LB
            self.gennode(arbre.fils[0])
            print(f"jumpf l{l}a")
            self.gennode(arbre.fils[1])
            print(f"jump l{l}b")
            print(f".l{l}a")
            if len(arbre.fils) > 2 and arbre.fils[2] is not None:
                self.gennode(arbre.fils[2])
            print(f"jump l{l}b")
            print(f".l{l}a")
            self.gennode(arbre.fils[1])
            print(f".l{l}b")

        elif(arbre.type == "node_loop"): 
            temp = config.ll
            config.NB_LB += 1
            config.ll = config.NB_LB
            print(f".l{config.ll}a")
            for fils in arbre.fils:
                self.gennode(fils)
            print(f"jump l{config.ll}a")
            print(f".l{config.ll}b")
            config.ll = temp
        elif(arbre.type == "node_break"): 
            print(f"jump l{config.ll}b")
        elif(arbre.type == "node_continue"):
            print(f"jump l{config.ll}c")
        elif(arbre.type == "node_target"): 
            print(f".l{config.ll}c")
        elif arbre.type == "node_seq":
            for fils in arbre.fils:
                self.gennode(fils)



            
    def begin(self):
        config.TS.append({})
    
    def end(self):
        return config.TS[-1]
    
    def declare(self, name: str) -> dict :
        if(not config.TS and name in config.TS[0]): ## erreur quand TS vide 
            raise Exception(f"La varibale {name} existe deja dans le block")
        sym = {name : {"index" : 0, "name" : name}}
        config.TS[0].update(sym)
        return sym 
    
    
    
    def find(self, name: str) -> dict:
        for table in reversed(config.TS):  # on parcourt les scopes de haut en bas
            if name in table:              # si la variable existe dans cette table
                return table[name]         # on renvoie son symbole
        raise Exception(f"La variable '{name}' n'existe pas")

    def semNode(self, arbre : Node):
        if (arbre.type ==  "node_block"):
            self.begin()
            for fils in arbre.fils:
                self.semNode(fils)
            self.end()
        elif (arbre.type == "node_decl"):
            s = self.declare(arbre.chaine)
           
            config.TS[0][arbre.chaine]["index"] = config.NB_VAR
            # print(config.TS)
            
            config.NB_VAR += 1
        
        elif (arbre.type == "node_ref"):
            name = getattr(arbre, "chaine", None) or getattr(arbre, "valeur", None)
            if name is None:
                raise Exception("node_ref sans nom")
            sym = self.find(name)
            arbre.index = sym["index"]

        
     

        elif (arbre.type == "node_assign"):
            if (arbre.fils[0].type != "node_ref"):
                raise Exception("La partie gauche d'une affectation doit etre une variable")
            self.semNode(arbre.fils[0])
            self.semNode(arbre.fils[1])
        else:
            for fils in arbre.fils:
                self.semNode(fils)
