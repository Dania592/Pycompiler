# la classe Token répresente un élément reconnu dans le texte du programme (mot clé, nombre, opérateur, ...)
class Token :
    # constructeur du token 
    def __init__(self, type : str, valeur : int, chaine : str):
        self.type = type # catégorie du token 
        self.valeur = valeur # valeur du token (le nombre si le type est constante par example)
        self.chaine = chaine # le contenu exact du token 
        # if type != "":
        #     self.print_token()

    #methode pour affichier le contenu du token 
    def print_token(self):
        print(f"Token : [{self.type}, {self.valeur}, {self.chaine}]")


# la classe Node represente un bloc ou une opération dans l'arbre syntaxiique

class Node : 
    def __init__(self, type : str, valeur:int = None, chaine:str = None, nbArg : int = None, pointeur : int = None):
        ## déclaration des attributs
        self.type = type # type du noeud (opérateur, constante, ...)
        if valeur != None :
            self.valeur = valeur 
        elif chaine != None : 
            self.chaine = chaine 
        elif nbArg != None: 
            self.nbArg= nbArg
        elif pointeur != None:
            self.pointeur = pointeur
        self.fils = [] #liste des enfants de ce noeud pour les branchements de l'arbre
        self.index = None 
        
    ## Méthode pour ajouter un enfant à un noeud 
    def ajouter_enfant(self, f:"Node"):
        self.fils.append(f)

    ## Méthode pour afficher l'arbre 
    def afficher_arbre(self):
        print("(", self.type, end="")
        for f in self.fils :
            print(" ", end="")
            f.afficher_arbre()
        print(" )", end="")

    def afficher_arbre_joli(self, indent: str = "", last: bool = True):
        # Préparer les infos du noeud
        info = self.type
        if hasattr(self, "valeur") and self.valeur is not None:
            info += f" [valeur={self.valeur}]"
        if hasattr(self, "chaine") and self.chaine:
            info += f" [chaine='{self.chaine}']"

        # Préfixe graphique selon si c'est le dernier enfant ou pas
        branch = "└── " if last else "├── "
        print(str(indent) + str(branch) + str(info))

        # Préparer l'indentation pour les enfants
        indent += "    " if last else "│   "

        # Afficher récursivement les enfants
        for i, f in enumerate(self.fils):
            f.afficher_arbre_joli(indent, i == len(self.fils) - 1)


# le dictoinnaire key_words associe a chaque type de mot clé (ex : tok_int, ...)  la chaine correspondante dans le langageu compilé
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


# cette énumération associe chaque type de token à son symbole au au mot qu'il représente dans le code source
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

