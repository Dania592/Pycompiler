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
        self.gennode(arbre)

    def optim(self):
        """ fait l'analyse sémantique de l'arbre syntaxite avec 0 comme priorité initiale """
        arbre = self.anaSem()
        return arbre
    
    def anaSem(self):
        arbre = self.analyseur_syntaxique.F()
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
            if arbre.nbLocales > 0:
                config.CODE_ASM += f"resn {arbre.nbLocales}\n"
            
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
            
            
    # MODIFIE : Ajout du drapeau 'is_function_scope'
    def begin(self, is_function_scope=False):
        config.TS.append({})
        if not hasattr(config, 'var_stack'):
            config.var_stack = []
            
        # MODIFIE : On sauvegarde TOUJOURS le NB_VAR parent
        config.var_stack.append(config.NB_VAR)
        
        # MODIFIE : On ne réinitialise NB_VAR que si c'est un nouveau
        # scope de FONCTION (pour les args et les locaux)
        if is_function_scope:
            config.NB_VAR = 0
        # SINON (pour un simple bloc), NB_VAR continue de s'incrémenter
        
        
    def end(self):
        table = config.TS.pop()
        
        # MODIFIE : On récupère le nombre de variables déclarées *dans ce scope*
        nb_vars_in_this_scope = len(table)
        
        # MODIFIE : On restaure TOUJOURS le NB_VAR du parent
        config.NB_VAR = config.var_stack.pop()
        
        # MODIFIE : On retourne le nombre de variables déclarées ici
        return nb_vars_in_this_scope
    
    
    def declare(self, name: str) -> dict :
        if not config.TS:
            raise Exception("Pas de scope actif pour déclarer la variable. 'begin()' a-t-il été appelé ?")
        
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
            # MODIFIE : C'est un simple bloc, PAS un scope de fonction
            self.begin(is_function_scope=False)
            
            # MODIFIE : On doit compter les locales de ce bloc et des sous-blocs
            locales_count = 0
            for fils in arbre.fils:
                self.semNode(fils)
                # MODIFIE : On compte les déclarations directes
                if fils.type == "node_decl":
                    locales_count += 1
                # MODIFIE : On ajoute les locales des sous-blocs
                elif fils.type == "node_block":
                    locales_count += fils.nbLocales
            
            # MODIFIE : 'end()' ne nous donne que les vars de ce niveau
            nb_vars_declared_here = self.end()
            
            # MODIFIE : Le nombre total de locales est la somme
            arbre.nbLocales = locales_count
            
        elif (arbre.type == "node_decl"):
            s = self.declare(arbre.chaine) 
        
        elif (arbre.type == "node_ref"):
            name = getattr(arbre, "chaine", None) or getattr(arbre, "valeur", None)
            if name is None:
                raise Exception("node_ref sans nom")
            sym = self.find(name)
            arbre.index = sym["index"]

        
        elif(arbre.type == "node_fonct"): 
            self.declare(arbre.chaine)
            
            # MODIFIE : C'EST un scope de fonction
            self.begin(is_function_scope=True)
            
            nb_args = 0
            body_node = None
            
            for fils in arbre.fils:
                if fils.type == "node_decl":
                    self.semNode(fils) 
                    nb_args += 1
                else:
                    body_node = fils
            
            arbre.nbArg = nb_args
            
            if body_node:
                self.semNode(body_node) # On analyse le corps
            
            # MODIFIE : 'end()' ne retourne que les vars de ce niveau
            self.end()
            
            # MODIFIE : On récupère le 'nbLocales' du bloc-corps
            if body_node and hasattr(body_node, "nbLocales"):
                arbre.nbLocales = body_node.nbLocales
            else:
                arbre.nbLocales = 0

        elif arbre.type == "node_appel" : 
            if arbre.fils[0].type == "node_ref":
                sym = self.find(arbre.fils[0].chaine)
            
            for fils in arbre.fils[1:]:
                self.semNode(fils) 
            
        elif (arbre.type == "node_assign"):
            self.semNode(arbre.fils[1]) 
            
            if (arbre.fils[0].type == "node_ref"):
                self.semNode(arbre.fils[0]) 
            elif (arbre.fils[0].type == "node_ind"):
                 self.semNode(arbre.fils[0]) 
            else:
                raise Exception("La partie gauche d'une affectation doit etre une variable ou une indirection")
        
        elif(arbre.type == "node_ind"):
            self.semNode(arbre.fils[0]) 
        
        elif(arbre.type == "node_adr"):
             self.semNode(arbre.fils[0]) 
                
        else:
            for fils in arbre.fils:
                self.semNode(fils)

    def verifier_main(self):
        if not config.TS:
             raise Exception("Impossible de vérifier 'main', la table des symboles globale est vide.")
             
        fonctions = config.TS[0].keys()
        
        if "main" not in fonctions:
            raise Exception("Erreur: fonction 'main' obligatoire absente")
        if "start" in fonctions:
            raise Exception("Erreur: fonction nommée 'start' interdite")