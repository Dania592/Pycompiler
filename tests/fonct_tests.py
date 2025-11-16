import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class FonctionTest(unittest.TestCase):
    def test_fonct_declare(self):
        code = """
void fonction(){
    int x;
    x = (-10)*3 + 2;
    debug x;
}

void main(){
    fonction();
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.fonction
resn 1
push 0
push 10
sub
push 3
mul
push 2
add
dup
set 0
drop 1
get 0
dbg
push 0
ret
.main
prep fonction
call 0
drop 1
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_fonct_var(self):
        code = """
void fonction(){
    int x;
    x = (-10)*3 + 2;
    debug x;
}

void main(){
  int x; 
  x = 12;
  debug x;
  fonction();
  debug x;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.fonction
resn 1
push 0
push 10
sub
push 3
mul
push 2
add
dup
set 0
drop 1
get 0
dbg
push 0
ret
.main
resn 1
push 12
dup
set 0
drop 1
get 0
dbg
prep fonction
call 0
drop 1
get 0
dbg
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_fonct_retour(self):
        code = """
int fonction(int a, int b){
    return a + b;
}

void main(){
  int x; 
  x = 12;
  debug x;
  int z; 
  z = 3;
  debug z;
  debug(fonction(x, z));
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.fonction
get 0
get 1
add
ret
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
push 3
dup
set 1
drop 1
get 1
dbg
prep fonction
get 0
get 1
call 2
dbg
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_fonct_retour_affect(self):
        code = """
int fonction(int a, int b){
    return a + b;
}

void main(){
  int x; 
  x = 12;
  debug x;
  int z; 
  z = 3;
  debug z;
  int res; 
  res = fonction(x, z);
  debug res;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.fonction
get 0
get 1
add
ret
push 0
ret
.main
resn 3
push 12
dup
set 0
drop 1
get 0
dbg
push 3
dup
set 1
drop 1
get 1
dbg
prep fonction
get 0
get 1
call 2
dup
set 2
drop 1
get 2
dbg
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_fonct_recur(self):
        code = """
int fonction(int a, int b){
    if (a > 20){
      return a;
    }
    debug a;
    return fonction(a + b,b);
}

void main(){
  int x; 
  x = 12;
  debug x;
  int z; 
  z = 3;
  debug z;
  int res; 
  res = fonction(x, z);
  debug res;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.fonction
get 0
push 20
cmpgt
jumpf l1a
get 0
ret
jump l1b
.l1a
.l1b
get 0
dbg
prep fonction
get 0
get 1
add
get 1
call 2
ret
push 0
ret
.main
resn 3
push 12
dup
set 0
drop 1
get 0
dbg
push 3
dup
set 1
drop 1
get 1
dbg
prep fonction
get 0
get 1
call 2
dup
set 2
drop 1
get 2
dbg
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