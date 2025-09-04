from analyseur_lexical import AnalyserLexical
from Object import Token, Node
import config

## actuellement on gére juste les opérateur unaire 
class AnalyseurSyntaxique :
    def __init__(self, path : str):
        global T
        self.analyseur = AnalyserLexical(path)
    
    def E(self, prio: int)->Node:
        node=self.P()
        while config.T.type in config.operateurs.keys() and config.operateurs[config.T.type]["priority"] >= prio:
            operateur = config.T.type
            self.analyseur.next()
            M = self.E(config.operateurs[operateur]["parg"])
            N= Node(config.operateurs[operateur]["Ntype"])
            N.ajouter_enfant(node)
            N.ajouter_enfant(M)
            node=N
        return node 

    
    def P(self):
        ## gestion des expressions simple avec un prefixe et un nom
        ## expression : préfixe ==> délégation du reste à la fonction S
        if (self.analyseur.check("tok_not")):
            node = self.P()
            arbre = Node("node_not")
            arbre.ajouter_enfant(node)
            return arbre 
        
        elif (self.analyseur.check("tok_minus")):
            node = self.P()
            arbre = Node("node_neg")
            arbre.ajouter_enfant(node)
            return arbre
        
        elif (self.analyseur.check("tok_plus")):
            return self.P()
        
        else : 
            return self.S()
        
    def S(self):
        return self.A()
    
    def A(self):
        global Last
        global T
        ## gestion des chiffres sinon renvoie vers E avec les parenthèse entre une expression 
        if (self.analyseur.check("tok_const")):
            node = Node("node_const", config.Last.valeur)
            return node
        elif (self.analyseur.check("tok_par_open")):
            r = self.E()
            self.analyseur.accept("tok_par_close")
            return r
        
        raise Exception(f"Regle de grammaire non respectée avec le token {config.T.type}")
    
        