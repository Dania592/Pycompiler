from Object import token

T = token(0,0,"")
Last = token(0,0,"")

def init(path : str):
    ## TODO vérification d'existance du fichier
    file = open(path)

    content = file.read()
    T = next(content)
    
def next(content : str):
    Last = T 
    





init("text.txt")