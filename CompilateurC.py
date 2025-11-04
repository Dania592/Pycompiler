from analyseur_semantique import AnalyseurSemantique
from analyseur_syntaxique import AnalyseurSyntaxique 
from Object import Token
import config 

def compiler(content : str):
    analyseur_semantique = AnalyseurSemantique(test = True, content = content)
    AnalyseurSemantique.begin(analyseur_semantique)
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    AnalyseurSemantique.end(analyseur_semantique)
    #analyseur_semantique.verifier_main() # on verifie qu'une fonction main existe et qu'il n'ya pas de fonction star 
    # print(".start")
    config.CODE_ASM += ".start\n"
    # print("prep main")
    config.CODE_ASM += "prep main\n"
    # print("call 0")
    config.CODE_ASM += "call 0\n"
    # print("halt")
    config.CODE_ASM += "halt\n"
    
    asm = config.CODE_ASM
    config.CODE_ASM = ""
    return asm

def main(path : str):
    global T
    global Last
    analyseur_semantique = AnalyseurSemantique(path)
    AnalyseurSemantique.begin(analyseur_semantique)
    while config.T.type != "tok_eof":
        analyseur_semantique.gencode()
    AnalyseurSemantique.end(analyseur_semantique)
    #analyseur_semantique.verifier_main() # on verifie qu'une fonction main existe et qu'il n'ya pas de fonction star 
    # print(".start")
    config.CODE_ASM += ".start\n"
    # print("prep main")
    config.CODE_ASM += "prep main\n"
    # print("call 0")
    config.CODE_ASM += "call 0\n"
    # print("halt")
    config.CODE_ASM += "halt\n"
    
    print(config.CODE_ASM)
    #todo
    # refaire du début a la fin la partie fonction et se rassurer que tout est cohérent
    # faire des verification minimal pour l'appel de fonctions  
    
if __name__ == "__main__":
    main("text.txt") 
