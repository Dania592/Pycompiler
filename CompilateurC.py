from analyseur_semantique import AnalyseurSemantique
from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Token
import config 

def compiler(content : str):
    analyseur_semantique = AnalyseurSemantique(test = True, content = content)
    config.CODE_ASM += ".start\n"
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    config.CODE_ASM += "halt\n"
    asm = config.CODE_ASM
    config.CODE_ASM = ""
    return asm

def main(path : str):
    global T
    global Last
    analyseur_semantique = AnalyseurSemantique(path)
    # print(".start")
    config.CODE_ASM += ".start\n"
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    # print("halt")
    config.CODE_ASM += "halt\n"
    
    print(config.CODE_ASM)
    
if __name__ == "__main__":
    main("text.txt") 