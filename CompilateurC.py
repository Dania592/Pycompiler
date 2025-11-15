from analyseur_semantique import AnalyseurSemantique
from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Token
import config 
import sys

def compiler(content : str):
    config.NB_VAR = 0 
    config.NB_LB = 0 
    config.ll = 0 
    config.NB_ARG = 0 

    config.TS = []
    config.var_stack = []
    analyseur_semantique = AnalyseurSemantique(test = True, content = content)
    
    # MODIFIE : On commence le scope GLOBAL ici
    AnalyseurSemantique.begin(analyseur_semantique)
    
    while config.T.type != "tok_eof":
        # MODIFIE : On appelle anaSem() puis gennode(), pas gencode()
        arbre = analyseur_semantique.anaSem()
        analyseur_semantique.gennode(arbre)
        
    # MODIFIE : On ferme le scope GLOBAL
    AnalyseurSemantique.end(analyseur_semantique)
    
    # MODIFIE : Vérification de 'main' après avoir tout parsé
    # analyseur_semantique.verifier_main() # Décommentez si vous voulez activer la vérification
    
    config.CODE_ASM += ".start\n"
    config.CODE_ASM += "prep main\n"
    config.CODE_ASM += "call 0\n"
    config.CODE_ASM += "halt\n"
    asm = config.CODE_ASM
    config.CODE_ASM = ""
    return asm

def main(path : str):
    analyseur_semantique = AnalyseurSemantique(path)
    
    # MODIFIE : Logique de compilation déplacée comme dans la fonction 'compiler'
    # MODIFIE : On commence le scope GLOBAL ici
    AnalyseurSemantique.begin(analyseur_semantique)
    
    while config.T.type != "tok_eof":
        # MODIFIE : On appelle anaSem() puis gennode(), pas gencode()
        arbre = analyseur_semantique.anaSem()
        analyseur_semantique.gennode(arbre)
        
    # MODIFIE : On ferme le scope GLOBAL
    AnalyseurSemantique.end(analyseur_semantique)

    # MODIFIE : Vérification de 'main' après avoir tout parsé
    # analyseur_semantique.verifier_main() # Décommentez si vous voulez activer la vérification

    config.CODE_ASM += ".start\n"
    config.CODE_ASM += "prep main\n"
    config.CODE_ASM += "call 0\n"
    config.CODE_ASM += "halt\n"

    print(config.CODE_ASM)
    
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file = sys.argv[1]
    else : 
        file = "text.txt"
    main(file)