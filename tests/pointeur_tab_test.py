import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class PointeurTableauTest(unittest.TestCase):
    def test_pointeur_fonct(self):
        code = """
void fonction(int *x){
  *x = 244;
}

void main(){
  int x; 
  x = 12;
  debug x;
  fonction(&x);
  debug x;
  int *p;
  *p = x;
  debug *p;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.fonction
push 244
dup
get 0
write
drop 1
push 0
ret
.main
resn 2
push 12
dup
set 0
drop 1
get 0
dbg
prep fonction
push 0
call 1
drop 1
get 0
dbg
get 0
dup
get 1
write
drop 1
get 1
read 
dbg
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
        
    def test_tableau(self):
        code = """
void free(int *p){}

int *malloc(int n){
  int *p;
  p = *0;
  *0 = *0 + n;
  return p;
}

int main(){
  int *tab; 
  tab = malloc(5);
  int i;
  i = 0;
  for(i= 0; i < 4; i = i + 1){
    *(tab + i) = i+ 10;
  }
  for(i= 0; i < 4; i = i + 1){
    debug(*(tab + i));
  }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.free
push 0
ret
.malloc
resn 1
push 0
read 
dup
set 1
drop 1
push 0
read 
get 0
add
dup
push 0
write
drop 1
get 1
ret
push 0
ret
.main
resn 2
prep malloc
push 5
call 1
dup
set 0
drop 1
push 0
dup
set 1
drop 1
push 0
dup
set 1
drop 1
.l1a
get 1
push 4
cmplt
jumpf l1b
get 1
push 10
add
dup
get 0
get 1
add
write
drop 1
.l1c
get 1
push 1
add
dup
set 1
drop 1
jump l1a
.l1b
push 0
dup
set 1
drop 1
.l2a
get 1
push 4
cmplt
jumpf l2b
get 0
get 1
add
read 
dbg
.l2c
get 1
push 1
add
dup
set 1
drop 1
jump l2a
.l2b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

        
if __name__ == '__main__':
    unittest.main()