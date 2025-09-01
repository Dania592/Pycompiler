from analyseur_lexical import AnalyserLexical
from Object import Token, Node
from config import T, Last

## actuellement on gére juste les opérateur unaire 
class AnalyseurSyntaxique :
    def __init__(self, path : str):
        global T
        self.analyseur = AnalyserLexical(path)
    
    def E(self):
        global T
        return self.P()
    
    
    def P(self):
        ## gestion des expressions simple avec un prefixe et un nom
        ## expression : préfixe ==> délégation du reste à la fonction S
        if (self.analyseur.check("tok_not")):
            print("token not")
            node = self.P()
            arbre = Node("node_not")
            arbre.ajouter_enfant(node)
            return arbre 
        
        elif (self.analyseur.check("tok_minus")):
            print("token moins")
            node = self.P()
            arbre = Node("node_neg")
            arbre.ajouter_enfant(node)
            return arbre
        
        elif (self.analyseur.check("tok_plus")):
            print("token plus")
            return self.P()
        
        else : 
            print("constante")
            return self.S()
        
    def S(self):
        return self.A()
    
    def A(self):
        global Last
        global T
        ## gestion des chiffres sinon renvoie vers E avec les parenthèse entre une expression 
        if (self.analyseur.check("tok_const")):
            node = Node("node_const", Last.valeur)
            return node
        elif (self.analyseur.check("tok_par_open")):
            r = self.E()
            self.analyseur.accept("tok_par_close")
            return r
        
        raise Exception(f"Regle de grammaire non respectée avec le token {T.type}")
    
        