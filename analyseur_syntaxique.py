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
        elif(self.analyseur.check("tok_ident")): 
            return  Node("node_ref", config.Last.chaine)
        
        raise Exception(f"Regle de grammaire non respectée avec le token {config.T.type}")
    
    def I(self) -> Node:
        if (self.analyseur.check("tok_debug")):
            node = self.E(0)
            self.analyseur.accept("tok_semicolon")
            N = Node("node_debug")
            N.ajouter_enfant(node)
            return N 
        elif (self.analyseur.check("tok_brace_open")):
            node = Node("node_block")
            while ( not self.analyseur.check("tok_brace_close")):
                node.ajouter_enfant(self.I())
            return node 
        elif(self.analyseur.check("tok_int")):
            node = Node("node_decl", chaine = config.T.chaine)
            self.analyseur.accept("tok_ident")
            self.analyseur.accept("tok_semicolon")
            return node
        elif(self.analyseur.check("tok_if")): 
            self.analyseur.accept("tok_par_open")
            E1 = self.E(0)
            self.analyseur.accept("tok_par_close")
            I1 = self.I()
            N1 = Node("node_cond")
            N1.ajouter_enfant(E1)
            N1.ajouter_enfant(I1)
            
            if(self.analyseur.check("tok_else")):
                I2 = self.I()
                N1.ajouter_enfant(I2)

            
            
            # N1.afficher_arbre_joli()
            return N1
        elif(self.analyseur.check("tok_while")):
            self.analyseur.accept("tok_par_open")
            E1 = self.E(0)
            self.analyseur.accept("tok_par_close")
            I1 = self.I()

            N1 = Node("node_loop")
            N2 = Node("node_cond")
            N1.ajouter_enfant(N2)
            N2.ajouter_enfant(E1)
            N2.ajouter_enfant(I1)
            return N1
        elif(self.analyseur.check("tok_do")):
            I1 = self.I()
            self.analyseur.accept("tok_while")
            self.analyseur.accept("tok_par_open")
            E1 = self.E(0)
            self.analyseur.accept("tok_par_close")
            self.analyseur.accept("tok_semicolon")
            N1 = Node("node_loop")
            N1.ajouter_enfant(I1)
            N2 = Node("node_target")
            N1.ajouter_enfant(N2)
            N3 = Node("node_cond")
            N1.ajouter_enfant(N3)
            N4 = Node("node_not")
            N3.ajouter_enfant(N4)
            N5 = Node("node_break")
            N3.ajouter_enfant(N5)
            N4.ajouter_enfant(E1)
            return N1
        elif(self.analyseur.check("tok_for")): 
            self.analyseur.accept("tok_par_open")
            E1 = self.E(0)
            self.analyseur.accept("tok_semicolon")
            E2 = self.E(0)
            self.analyseur.accept("tok_semicolon")
            E3 = self.E(0)
            self.analyseur.accept("tok_par_close")
            I1 = self.I()
            N1 = Node("node_seq")
            N2 = Node("node_loop")
            N3 = Node("node_drop")
            N1.ajouter_enfant(N3)
            N1.ajouter_enfant(N2)
            N3.ajouter_enfant(E1)
            N4 = Node("node_cond")
            N2.ajouter_enfant(N4)
            N4.ajouter_enfant(E2)
            N5 = Node("node_break")
            N6 = Node("node_seq")
            N4.ajouter_enfant(N6)
            N4.ajouter_enfant(N5)
            N7 = Node("node_target")
            N8 = Node("node_drop")
            N6.ajouter_enfant(I1)
            N6.ajouter_enfant(N7)
            N6.ajouter_enfant(N8)
            N8.ajouter_enfant(E3)
            return N1

        else :
            N = self.E(0)
            self.analyseur.accept("tok_semicolon")
            node = Node("node_drop")
            node.ajouter_enfant(N)
            return node
        