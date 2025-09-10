from Object import Token

T = Token("test",0,"")
Last = Token("",0,"")

NB_VAR = 0 
NB_LB = 0 # variable globale qui compte le nombre de label

# Associe chaque token a sa priorité, son type de noeud dans l'arbre syntaxique et la priorité de l'élément qui doit le suivre dans l'expression
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

# Associe chaque noeud à sa conversion en pseudo code d'assemblage
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
    "node_affect":{"suffixe": "", "prefixe": ""}, #TODO !!!!!!!!!!!
    "node_eq":{"suffixe": "cmpeq", "prefixe": ""},
    "node_neq":{"suffixe": "cmpne", "prefixe": ""},
    "node_lt":{"suffixe": "cmplt", "prefixe": ""},
    "node_gt":{"suffixe": "cmpgt", "prefixe": ""},
    "node_le":{"suffixe": "cmple", "prefixe": ""},
    "node_ge":{"suffixe": "cmpge", "prefixe": ""},
    "node_debug":{"suffixe": "debug", "prefixe": ""}, ## TODO : revoir 
    "node_decl" :{"suffixe": "", "prefixe": ""},
    "node_block" :{"suffixe": "", "prefixe": ""},
    #"node_ref" : {"suffixe": "", "prefixe": ""},
    #"node_cond" : {"suffixe": "", "prefixe": ""},
    #"node_loop" : {"suffixe": "", "prefixe": ""}, 
    #"node_break" : {"suffixe": "", "prefixe": ""}
}

TS = []