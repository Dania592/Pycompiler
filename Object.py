class Token :
    def __init__(self, type : str, valeur : int, chaine : str):
        self.type = type
        self.valeur = valeur
        self.chaine = chaine 
        if type != "":
            self.print_token()
    def print_token(self):
        print(f"Token : [{self.type}, {self.valeur}, {self.chaine}]")


class Node :
    ## création de noeud 
    def __init__(self, type : str):
        ## déclaration des attributs
        pass 
    ## ajouter un enfant 
    def ajouter_enfant(self, fils : Node):
        pass
    ## afficher arbre 
    def afficher_arbre(self):
        pass
    def nodeV(self, type : str, valeur : int):
        ## création du noeud et renseignement de la valeur du chiffre
        pass
    def nodeC(self, type : str, chaine : str):
        ## création du noeud et renseignmenet de la chaine de caractère 
        pass 
    def node_1(self, type : str, fils : Node):
        ## création du noeud pere et ajout du fils dans la liste des fils 
        pass
    def node_2(self, type : str, fils1 : Node, fils2 : Node):
        ## création du noeud pere et ajout des deux fils dans la liste des fils 
        pass 
        
    
    


key_words = {
    # mots-clés
    "tok_int": "int",
    "tok_void": "void",
    "tok_return": "return",
    "tok_if": "if",
    "tok_else": "else",
    "tok_for": "for",
    "tok_do": "do",
    "tok_while": "while",
    "tok_break": "break",
    "tok_continue": "continue",
    # autres 
    "tok_debug": "debug",
    "tok_send": "send",
    "tok_recv": "recv"
}

enum = {
"tok_eof": "eof", ## TODO à voir c'est quoi la fin de fichier 
"tok_const": "const",## TODO comment avoir la valeur 
"tok_ident": "ident",## TODO comment avoir la valeur 

# opérateurs
"tok_plus": "+",
"tok_minus": "-",
"tok_mult": "*",
"tok_div": "/",
"tok_mod": "%",
"tok_and": "&&",
"tok_or": "||",
"tok_not": "!",
"tok_eq": "==",
"tok_neq": "!=",
"tok_lt": "<",
"tok_gt": ">",
"tok_le": "<=",
"tok_ge": ">=",
"tok_assign": "=",

# ponctuation
"tok_par_open": "(",
"tok_par_close": ")",
"tok_brace_open": "{",
"tok_brace_close": "}",
"tok_bracket_open": "[",
"tok_bracket_close": "]",
"tok_semicolon": ";",
"tok_comma": ",",
"tok_amp": "&",
}

