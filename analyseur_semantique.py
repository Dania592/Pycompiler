from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Node
from config import T, Last

class AnalyseurSemantique:    
    def __init__(self, path):
        self.analyseur_syntaxique = AnalyseurSyntaxique(path)
        
    def gencode(self):
        global T
        arbre = self.optim()
        self.gennode(arbre)
        
    def optim(self):
        arbre = self.analyseur_syntaxique.E()
        return arbre
        
    def gennode(self, arbre : Node):
        if (arbre.type ==  "node_const"): 
            print("push ", arbre.valeur)
        elif (arbre.type == "node_not"):
            gennode(arbre.fils[0])
            print("not")
        elif (arbre.type == "node_neg"):
            print("push 0")
            gennode(arbre.fils[0])
            print("sub")
        