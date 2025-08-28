from analyseur_lexical import AnalyserLexical
from Object import Token, Node

## actuellement on gére juste les opérateur unaire 
class AnalyseurSyntaxique :
    def __init__(self, path : str):
        self.analyseur = AnalyserLexical(path)
        pass
    
    def E(self):
        return self.P()
    
    
    def P(self):
        ## gestion des expressions simple avec un prefixe et un nom
        ## expression : préfixe ==> délégation du reste à la fonction S
        if (self.analyseur.check("tok_not")):
            node = P()
            arbre = Node("node_not")
            arbre.ajouter_enfant(node)
            return arbre 
        
    def S(self):
        ## gestion des expressions qui continnent des suffixes 
        ## actuelememnt on a pas trop d'expression avec un suffixe 
        pass
    
    def A(self):
        ## gestion des chiffres sinon renvoie vers E avec les parenthèse entre une expression 
        pass 