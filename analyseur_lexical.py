import os
from Object import Token
import config
class AnalyserLexical : 
    def __init__(self, path = "text.txt", test = False, content = ""): 
        if test :
            self.text_content = content 
        else :
            if not os.path.exists(path):
                raise FileNotFoundError(f"Le fichier à l'emplacement {path} n'existe pas !")
            self.file = open(path)
            self.text_content = self.file.read() 
        self.length = len(self.text_content)
        self.pos = 0
        self.next()
        
        
    def next(self):
        """récupération du caratère suivant 
        """
        config.Last = config.T 
        while self.length > self.pos and self.text_content[self.pos] in [" ", "\n", "\t"]:
            self.pos += 1
            
        if self.length <= self.pos : 
            config.T = Token("tok_eof", 0, "eof")
            
        else :
            car = self.text_content[self.pos] 
            if (car.isdigit()):
                number = self.get_number()
                config.T = Token("tok_const", number, "")
                
            elif (car.isalpha() or car == "_"):
                word = self.get_alpha()
                if word in config.key_words.values():
                    config.T =Token("tok_" + word, 0, word)
                else :
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
        
        inverse_enum = {v: k for k, v in config.enum.items()}
        if c in inverse_enum.keys():
            token_type = inverse_enum[c]
            config.T =Token(token_type, 0, c)
        else :
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
    
    def peek(self):
        pos_backup = self.pos
        T_backup = config.T
        Last_backup = config.Last
        self.next()
        next_token = config.T

        # Restaurer l'état initial
        self.pos = pos_backup
        config.T = T_backup
        config.Last = Last_backup
        
        return next_token


