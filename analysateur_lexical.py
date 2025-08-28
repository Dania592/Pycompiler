import os
from Object import Token, key_words, enum

T = Token("",0,"")
Last = Token("",0,"")

class AnalyserLexical : 
    def __init__(self, path : str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier à l'emplacement {path} n'existe pas !")
        
        self.file = open(path)
        self.text_content = self.file.read()
        self.length = len(self.text_content)
        self.pos = 0
        self.next()
    
    def next(self):
        global T 
        global Last 
        Last = T 
        ## TODO gérer les commentaires  
        while self.length > self.pos and self.text_content[self.pos] in [" ", "\n", "\t"]:
            self.pos += 1
            
        if self.length == self.pos :
            ## token de fin de fichier 
            T = Token("tok_eof", 0, "eof")
            
        else :
            car = self.text_content[self.pos] 
            if (car.isdigit()):
                ## token de constante 
                number = self.get_number()
                T = Token("tok_const", number, "")
                
            elif (car.isalpha() or car == "_"):
                ## récupération du mot
                print("c'est une lettre ", car)
                word = self.get_alpha()
                
                if word in key_words.values():
                    ## token mots clé
                    T = Token("tok_"+word, 0, word)
                else :
                    ## token indicateur / varibale / fonction 
                    T = Token("tok_ident", 0, word)
            else :
                self.get_motif()
                    
    def get_number(self) -> int:
        num = ""
        while self.length > self.pos and self.text_content[self.pos].isdigit():
            num += self.text_content[self.pos]
            self.pos += 1
        return int(num)
    
    def get_alpha(self) -> str:
        car = ""
        while self.length > self.pos and (self.text_content[self.pos].isalpha() or self.text_content[self.pos]== "_"):
            car += self.text_content[self.pos]
            self.pos += 1
        return car
    
    def get_motif(self):
        global T
        c = self.text_content[self.pos]
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
                
        inverse_enum = {v: k for k, v in enum.items()}
        if c in inverse_enum.keys():
            token_type = inverse_enum[c]
            T = Token(token_type, 0, c)
        else :
            # TODO erreur 
            T = Token("inconnu", 0, c)
        
    def check(self, type : str) -> bool:
        global T
        if (T.type == type):
            self.next()
            return True
        return False
    
    def accept(self, type : str):
        global T
        if ( not self.check(type)):
            raise Exception(f"Le type attendu <{type}> ne correspond par au type du token <{T.type}>")

analyseur  = AnalyserLexical("text.txt")
analyseur.accept("tok_e")