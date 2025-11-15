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
    AnalyseurSemantique.begin(analyseur_semantique)
    
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
        
    AnalyseurSemantique.end(analyseur_semantique)
    
    config.CODE_ASM += ".start\n"
    config.CODE_ASM += "prep main\n"
    config.CODE_ASM += "call 0\n"
    config.CODE_ASM += "halt\n"
    asm = config.CODE_ASM
    config.CODE_ASM = ""
    return asm

def main(path : str):
    analyseur_semantique = AnalyseurSemantique(path)
    AnalyseurSemantique.begin(analyseur_semantique)
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    AnalyseurSemantique.end(analyseur_semantique)
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
