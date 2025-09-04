from analyseur_semantique import AnalyseurSemantique
from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Token
import config 

def main(path : str):
    global T
    global Last
    analyseur_semantique = AnalyseurSemantique(path)
    print("start")
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    
    print("debug")
    print("hlt")


main("text.txt")