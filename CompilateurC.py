from analyseur_semantique import AnalyseurSemantique
from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Token
import config 

def main(path : str):
    global T
    global Last
    analyseur_semantique = AnalyseurSemantique(path)
    AnalyseurSemantique.begin(analyseur_semantique)
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    AnalyseurSemantique.end(analyseur_semantique)
    #analyseur_semantique.verifier_main() # on verifie qu'une fonction main existe et qu'il n'ya pas de fonction star 
    print(".start")
    print("prep main")
    print("call 0")
    print("halt")
    #todo
    # refaire du début a la fin la partie fonction et se rassurer que tout est cohérent
    # faire des verification minimal pour l'appel de fonctions  
main("text.txt") 