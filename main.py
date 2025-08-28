from analyseur_lexical import AnalyserLexical
from analyseur_semantique import AnalyserSemantique
from analyseur_syntaxique import AnalyserSyntaxique 
from Object import Token, 

T = Token("",0,"")
Last = Token("",0,"")

def main(path : str):
    analyseur = AnalyserLexical(path)
    print("start")
    
    pass 