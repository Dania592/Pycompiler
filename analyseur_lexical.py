import os
from Object import Token, key_words, enum
import config

class AnalyserLexical : 
    def __init__(self, path : str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier à l'emplacement {path} n'existe pas !")
        
        self.file = open(path)
        self.text_content = self.file.read()
        self.length = len(self.text_content)
        self.pos = 0
        self.next()
        #print("dans l'analyseur lexical : ", config.T.type)
        
    
    def next(self):
        global T
        global Last
        config.Last = config.T 
        ## TODO gérer les commentaires  
        while self.length > self.pos and self.text_content[self.pos] in [" ", "\n", "\t"]:
            self.pos += 1
            
        if self.length <= self.pos :
            ## token de fin de fichier 
            config.T = Token("tok_eof", 0, "eof")
            
        else :
            car = self.text_content[self.pos] 
            if (car.isdigit()):
                ## token de constante 
                number = self.get_number()
                config.T = Token("tok_const", number, "")
                
            elif (car.isalpha() or car == "_"):
                ## récupération du mot
                word = self.get_alpha()
                
                if word in key_words.values():
                    ## token mots clé
                    config.T =Token("tok_" + word, 0, word)
                else :
                    ## token indicateur / varibale / fonction 
                    config.T =Token("tok_ident", 0, word)
            else :
                self.get_motif()
        
    def get_number(self) -> int:
        """Extrait un nombre depuis la position courante"""
        num = ""
        while self.length > self.pos and self.text_content[self.pos].isdigit():
            num += self.text_content[self.pos]
            self.pos += 1
        return int(num)
    
    def get_alpha(self) -> str:
        """Extrait une chaîne alphabétique depuis la position courante"""
        car = ""
        while (self.length > self.pos and 
        (self.text_content[self.pos].isalpha() or self.text_content[self.pos]== "_")):
            car += self.text_content[self.pos]
            self.pos += 1
        return car
    
    def get_motif(self):
        """Traite les opérateurs et symboles spéciaux"""
        global T
        c = self.text_content[self.pos]
        
        # Gestion des opérateurs composés
        if (c in ["=", "!", ">", "<"] ):
            if self.length > self.pos + 1 and self.text_content[self.pos+1] == "=":
                self.pos += 1
                c += self.text_content[self.pos]
        elif (c == "&"):
            if self.length > self.pos + 1 and self.text_content[self.pos+1] == "&":
                self.pos += 1
                c += self.text_content[self.pos]
        elif (c == "|"):
            if self.length > self.pos + 1 and self.text_content[self.pos+1] == "|":
                self.pos += 1
                c += self.text_content[self.pos]
                
        self.pos += 1
        
        inverse_enum = {v: k for k, v in enum.items()}
        if c in inverse_enum.keys():
            token_type = inverse_enum[c]
            config.T =Token(token_type, 0, c)
        else :
            # TODO erreur lors de l'identification du car 
            config.T =Token("inconnu", 0, c)
        
    def check(self, type : str) -> bool:
        global T
        if (config.T.type == type):
            self.next()
            return True
        return False
    
    def accept(self, type : str):
        global T
        if (not self.check(type)):
            raise Exception(f"Le type attendu <{type}> ne correspond par au type du token <{config.T.type}>")

# analyseur  = AnalyserLexical("text.txt")
# while T.type != "tok_eof":
#     analyseur.next()
