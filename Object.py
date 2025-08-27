class token :
    def __init__(self, type : int, valeur : int, chaine : str):
        self.type = type
        self.valeur = valeur
        self.chaine = chaine 

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
    "tok_continue": "continue"
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

# autres 
"tok_debug": "debug",
"tok_send": "send",
"tok_recv": "recv"
}