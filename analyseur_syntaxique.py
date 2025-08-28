from analyseur_lexical import AnalyserLexical
from Object import Token, Node

class AnalyseurSyntaxique :
    def __init__(self, path : str):
        self.analyseur = AnalyserLexical(path)
        pass
    
    def E(self):
        return self.P()
    
    def P(self):
        if (self.analyseur.check("tok_not")):
            node = P()
            arbre = Node("node_not")
            arbre.ajouter_enfant(node)
            return arbre 