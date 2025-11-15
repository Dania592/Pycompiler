from Object import Token

CODE_ASM = ""

T = Token("",0,"")
Last = Token("",0,"")

NB_VAR = 0 # variable globale qui compte le nombre de variable 
NB_LB = 0 # variable globale qui compte le nombre de label
ll = 0 # variable globale au fichier analyseur semantique pour  les labels 
NB_ARG = 0 # nombre d'argument d" une fonction 

operateurs={
    "tok_plus": {"priority": 5 , "parg":6 , "Ntype": "node_add"},
    "tok_minus":{"priority": 5 , "parg":6 , "Ntype":"node_sub" },
    "tok_mult":{"priority": 6 , "parg":7 , "Ntype":"node_mult"},
    "tok_div":{"priority": 6 , "parg":7 , "Ntype":"node_div"},
    "tok_mod":{"priority": 6 , "parg":7 , "Ntype":"node_mod"},
    "tok_and":{"priority": 3 , "parg":4 , "Ntype":"node_and"},
    "tok_or":{"priority": 2 , "parg":3 , "Ntype":"node_or"},

    "tok_eq":{"priority": 4 , "parg":5 , "Ntype":"node_eq"},
    "tok_neq":{"priority": 4 , "parg":5 , "Ntype":"node_neq"},
    "tok_lt":{"priority": 4.5 , "parg":5 , "Ntype":"node_lt"},
    "tok_gt":{"priority": 4.5 , "parg":5 , "Ntype":"node_gt"},
    "tok_le":{"priority": 4.5 , "parg":5 , "Ntype":"node_le"},
    "tok_ge":{"priority": 4.5 , "parg":5 , "Ntype":"node_ge"},
    "tok_assign":{"priority": 1 , "parg":1 , "Ntype":"node_assign"}
}

op_assembleur={
    "node_add":{"suffixe": "add", "prefixe": ""},
    "node_minus":{"suffixe": "sub", "prefixe": "push 0"},
    "node_sub":{"suffixe": "sub", "prefixe": ""},
    "node_not":{"suffixe": "not", "prefixe": ""},
    "node_mult":{"suffixe": "mul", "prefixe": ""},
    "node_div":{"suffixe": "div", "prefixe": ""},
    "node_mod":{"suffixe": "mod", "prefixe": ""},
    "node_and":{"suffixe": "and", "prefixe": ""},
    "node_or":{"suffixe": "or", "prefixe": ""},
    "node_affect":{"suffixe": "", "prefixe": ""}, 
    "node_eq":{"suffixe": "cmpeq", "prefixe": ""},
    "node_neq":{"suffixe": "cmpne", "prefixe": ""},
    "node_lt":{"suffixe": "cmplt", "prefixe": ""},
    "node_gt":{"suffixe": "cmpgt", "prefixe": ""},
    "node_le":{"suffixe": "cmple", "prefixe": ""},
    "node_ge":{"suffixe": "cmpge", "prefixe": ""},
    "node_debug":{"suffixe": "", "prefixe": ""}, 
    "node_decl" :{"suffixe": "", "prefixe": ""},
    "node_block" :{"suffixe": "", "prefixe": ""},
}



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
"tok_eof": "eof", 
"tok_const": "const",
"tok_ident": "ident",

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



TS = []
var_stack = []