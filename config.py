from Object import Token

T = Token("test",0,"")
Last = Token("",0,"")

operateur={
    "tok_plus": {"priority": 5 , "parg":6 , "Ntype": "node_add"},
    "tok_minus":{"priority": 5 , "parg":6 , "Ntype":"node_sub" },
    "tok_mult":{"priority": 6 , "parg":7 , "Ntype":"node_mult"},
    "tok_div":{"priority": 6 , "parg":7 , "Ntype":"node_div"},
    "tok_mod":{"priority": 6 , "parg":7 , "Ntype":"node_mod"},
    "tok_and":{"priority": 3 , "parg":4 , "Ntype":"node_and"},
    "tok_or":{"priority": 2 , "parg":3 , "Ntype":"node_or"},

    "tok_eq":{"priority": 4 , "parg":5 , "Ntype":"node_eq"},
    "tok_neq":{"priority": 4 , "parg":5 , "Ntype":"node_neq"},
    "tok_lt":{"priority": 4 , "parg":5 , "Ntype":"node_lt"},
    "tok_gt":{"priority": 4 , "parg":5 , "Ntype":"node_gt"},
    "tok_le":{"priority": 4 , "parg":5 , "Ntype":"node_le"},
    "tok_ge":{"priority": 4 , "parg":5 , "Ntype":"node_ge"},
    "tok_assign":{"priority": 1 , "parg":1 , "Ntype":"node_assign"}

}