from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Node
import config

class AnalyseurSemantique:  
    """
    Parcours l'arbre syntaxique pour effectuer des verifications afin de génerer le pseudo code machine
    """  
    def __init__(self, path ="text.txt", test = False, content = ""):
        self.analyseur_syntaxique = AnalyseurSyntaxique(path, test, content) 
        
    def gencode(self):
        arbre = self.optim()
        config.CODE_ASM += "resn "+ str(config.NB_VAR) + "\n"
        self.gennode(arbre)

        config.CODE_ASM += "drop "+ str(config.NB_VAR) + "\n"

    def optim(self):
        """ fait l'analyse sémantique de l'arbre syntaxite avec 0 comme priorité initiale """
        arbre = self.anaSem()
        return arbre
    
    def anaSem(self):
        arbre = self.analyseur_syntaxique.F()
        config.NB_VAR = 0
        self.semNode(arbre)
        return arbre

    def gennode(self, arbre : Node):
        """ Méthode qui parcours récursivement l'arbre de noeud et génère le code machine associé a chaque noeud """
        if (arbre.type ==  "node_const"):  
            config.CODE_ASM += "push "+ str(arbre.valeur) + "\n"
            
        elif (arbre.type == "node_not"): 
            self.gennode(arbre.fils[0]) 
            config.CODE_ASM += "not\n"
            
        elif (arbre.type == "node_neg"): 
            config.CODE_ASM += "push 0\n"
            self.gennode(arbre.fils[0])
            config.CODE_ASM += "sub\n"
            
        elif (arbre.type == "node_debug"):
            self.gennode(arbre.fils[0])
            config.CODE_ASM += "dbg\n"
            
        elif(arbre.type == "node_send"): 
            self.gennode(arbre.fils[0])
            config.CODE_ASM += "send\n"
            
        elif(arbre.type == "node_recv"): 
            config.CODE_ASM += "recv\n"
            
        elif (arbre.type == "node_ret"):
            self.gennode(arbre.fils[0])
            config.CODE_ASM += "ret\n"
            
        elif ( arbre.type in config.op_assembleur.keys() ):
            prefixe = config.op_assembleur[arbre.type]["prefixe"]
            if prefixe != "" :
                config.CODE_ASM += prefixe + "\n"
                
            for fils in arbre.fils:
                self.gennode(fils) 
            suffixe = config.op_assembleur[arbre.type]["suffixe"]
            if suffixe != "":
                config.CODE_ASM += suffixe + "\n"
                
        elif (arbre.type == "node_assign"):
            if arbre.fils[0].type == "node_ind":
                self.gennode(arbre.fils[1]) 
                config.CODE_ASM += "dup\n"           
                self.gennode(arbre.fils[0].fils[0])   
                config.CODE_ASM += "write\n" 
            else: 
                self.gennode(arbre.fils[1])
                config.CODE_ASM += "dup\n"
                config.CODE_ASM += "set " + str(arbre.fils[0].index) + "\n"
        
        elif (arbre.type == "node_ref"):
            config.CODE_ASM += "get " +  str(arbre.index) + "\n"
            
        elif (arbre.type == "node_drop"):
            self.gennode(arbre.fils[0])
            config.CODE_ASM += "drop 1\n"
            
        elif arbre.type == "node_cond":
            config.NB_LB += 1
            l = config.NB_LB
            self.gennode(arbre.fils[0])
            config.CODE_ASM += f"jumpf l{l}a\n"
            self.gennode(arbre.fils[1])
            config.CODE_ASM += f"jump l{l}b\n"  
            config.CODE_ASM += f".l{l}a\n"
            
            if len(arbre.fils) > 2 and arbre.fils[2] is not None:
                self.gennode(arbre.fils[2])
                
            config.CODE_ASM += f".l{l}b\n"
            
            
        elif(arbre.type == "node_loop"): 
            temp = config.ll
            config.NB_LB += 1
            config.ll = config.NB_LB
            
            if len(arbre.fils) > 0 and arbre.fils[0].type == "node_cond":
                # C'est une boucle while
                config.CODE_ASM += f".l{config.ll}a\n"
                
                # Générer la condition
                self.gennode(arbre.fils[0].fils[0])  
                config.CODE_ASM += f"jumpf l{config.ll}b\n" 
                
                # Générer le corps de la boucle
                if len(arbre.fils[0].fils) > 1:
                    self.gennode(arbre.fils[0].fils[1])  
                
                config.CODE_ASM += f"jump l{config.ll}a\n" 
                config.CODE_ASM += f".l{config.ll}b\n" 
                
            else:
                config.CODE_ASM += f".l{config.ll}a\n"
                
                for i in range(len(arbre.fils)):
                    self.gennode(arbre.fils[i])
                    
                config.CODE_ASM += f"jump l{config.ll}a\n"
                config.CODE_ASM += f".l{config.ll}b\n"
                
            config.ll = temp
            
        elif(arbre.type == "node_break"): 
            config.CODE_ASM += f"jump l{config.ll}b\n"
            
        elif(arbre.type == "node_continue"):
            config.CODE_ASM += f"jump l{config.ll}a\n"
            
        elif(arbre.type == "node_target"): 
            config.CODE_ASM += f".l{config.ll}c\n"
            
        elif arbre.type == "node_seq":
            for fils in arbre.fils:
                self.gennode(fils)
                
        elif(arbre.type == "node_fonct"): 
            config.CODE_ASM += f".{arbre.chaine}\n"
            config.CODE_ASM += f"resn {arbre.nbArg}\n"
            self.gennode(arbre.fils[-1])
            config.CODE_ASM += "push 0\n"
            config.CODE_ASM += "ret\n"
            
        elif(arbre.type == "node_appel"): 
            config.CODE_ASM += f"prep {arbre.fils[0].chaine}\n"
            for arg in arbre.fils[1:]: 
                self.gennode(arg)
            config.CODE_ASM += f"call {len(arbre.fils) - 1}\n"

        elif(arbre.type == "node_ind"): 
            self.gennode(arbre.fils[0])
            config.CODE_ASM += "read \n"
        
        elif arbre.type == "node_adr":
            var = arbre.fils[0]
            config.CODE_ASM += f"push {var.index}\n"
            
            
    def begin(self):
        config.TS.append({})
        if not hasattr(config, 'var_stack'):
            config.var_stack = []
        config.var_stack.append(config.NB_VAR)
        
        
    def end(self):
        table = config.TS.pop()
        nb_vars_liberated = len(table)
        config.NB_VAR = config.var_stack.pop()
        return nb_vars_liberated
    
    
    def declare(self, name: str) -> dict :
        if not config.TS:
            raise Exception("Pas de scope actif pour déclarer la variable")
        if name in config.TS[-1]:
            raise Exception(f"La variable {name} existe deja dans le block courant")
        
        sym = {name: {"index": config.NB_VAR, "name": name}}
        config.TS[-1].update(sym)
        config.NB_VAR += 1
        return sym
    
    
    def find(self, name: str) -> dict:
        for table in reversed(config.TS):  
            if name in table:             
                return table[name]    
        raise Exception(f"La variable '{name}' n'existe pas")
    

    def semNode(self, arbre : Node):
        if (arbre.type ==  "node_block"):
            self.begin()
            for fils in arbre.fils:
                self.semNode(fils)
            nb_vars = self.end()
            arbre.nbArg = nb_vars
            
        elif (arbre.type == "node_decl"):
            s = self.declare(arbre.chaine) 
            config.TS[-1][arbre.chaine]["index"] = config.NB_VAR
            config.NB_VAR += 1
        
        elif (arbre.type == "node_ref"):
            name = getattr(arbre, "chaine", None) or getattr(arbre, "valeur", None)
            if name is None:
                raise Exception("node_ref sans nom")
            sym = self.find(name)
            arbre.index = sym["index"]

        
        elif(arbre.type == "node_fonct"): 
            N = self.declare(arbre.chaine)
            config.NB_ARG = 0
            self.begin()
            for fils in arbre.fils:
                self.semNode(fils)
                if fils.type == "node_decl":
                    config.NB_ARG += 1
            self.end()
            arbre.nbArg =  config.NB_ARG

        elif arbre.type == "node_appel" : 
            for fils in arbre.fils:
                self.semNode(fils) 
            # Vérification de la cible de l'appel
            #cible = arbre.fils[0]
            #print(cible)
            
        elif (arbre.type == "node_assign"):
            if (arbre.fils[0].type != "node_ref"):
                raise Exception("La partie gauche d'une affectation doit etre une variable")
            self.semNode(arbre.fils[0])
            self.semNode(arbre.fils[1])
        else:
            for fils in arbre.fils:
                self.semNode(fils)

    def verifier_main(self):
        fonctions = [key for key, info in config.TS[0].items() if info.get("type") == "node_fonct"]
        if "main" not in fonctions:
            raise Exception("Erreur: fonction 'main' obligatoire absente")
        if "start" in fonctions:
            raise Exception("Erreur: fonction nommée 'start' interdite")