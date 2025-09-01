from analyseur_semantique import AnalyseurSemantique
from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Token
from config import T, Last

def main(path : str):
    global T
    global Last
    analyseur_semantique = AnalyseurSemantique(path)
    print("start")
    while T.type != "tok_eof":
        print("dans main ",T.type)
        analyseur_semantique.gencode()
    
    print("debug")
    print("hlt")


main("text.txt")