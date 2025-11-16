import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class DeclareTests(unittest.TestCase):
    
    def test_declare_var_bloc(self):
        code = """
        void main(){
            int x;
            int y; 
            x = 1;
            debug x;
            {
                int x;
                x = 26;
                debug x; 
                int y;
                y = 12;
                debug y;
            }
            debug x;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 4
push 1
dup
set 0
drop 1
get 0
dbg
push 26
dup
set 2
drop 1
get 2
dbg
push 12
dup
set 3
drop 1
get 3
dbg
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

    def test_cond_if_equ(self):
        code = """
void main(){
    int x;
    x = 1;
    if (x == 1){
        debug x;
    }else{
        debug x;
    }
    
    if (x== 1){
        debug x;
    }else{
        debug x ;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 1
dup
set 0
drop 1
get 0
push 1
cmpeq
jumpf l1a
get 0
dbg
jump l1b
.l1a
get 0
dbg
.l1b
get 0
push 1
cmpeq
jumpf l2a
get 0
dbg
jump l2b
.l2a
get 0
dbg
.l2b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
    
    def test_cond_if_f(self):
        code = """
void main(){
    int x;
    x = 2;
    if (x == 1){
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 1
cmpeq
jumpf l1a
get 0
dbg
jump l1b
.l1a
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_cond_else_sup(self):
        code = """
void main(){
    int x;
    x = 2;
    if (x > 1){
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 1
cmpgt
jumpf l1a
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
        
    def test_cond_else_inf(self):
        code = """
void main(){
    int x;
    x = 2;
    if (x < 1){
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 1
cmplt
jumpf l1a
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_cond_else_neg(self):
        code = """
void main(){
    int x;
    x = 2;
    if (!(x < 1)){
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 1
cmplt
not
jumpf l1a
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_cond_else_and(self):
        code = """
void main(){
    int x;
    x = 2;
    if ((x != 5) && (x == 2)){
        x = 5;
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 5
cmpne
get 0
push 2
cmpeq
and
jumpf l1a
push 5
dup
set 0
drop 1
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

    def test_cond_else_and_f(self):
        code = """
void main(){
    int x;
    x = 2;
    if ((x > 5) && (x == 2)){
        x = 5;
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 5
cmpgt
get 0
push 2
cmpeq
and
jumpf l1a
push 5
dup
set 0
drop 1
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        

    def test_cond_else_or(self):
        code = """
void main(){
    int x;
    x = 2;
    if ((x > 5) || (x == 2)){
        x = 5;
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 5
cmpgt
get 0
push 2
cmpeq
or
jumpf l1a
push 5
dup
set 0
drop 1
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
push 0
ret
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_cond_else_or_f(self):
        code = """
void main(){
    int x;
    x = 2;
    if ((x > 5) || (x != 2)){
        x = 5;
        debug x;
    }else{
        x = 3;
        debug x;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """.main
resn 1
push 2
dup
set 0
drop 1
get 0
push 5
cmpgt
get 0
push 2
cmpne
or
jumpf l1a
push 5
dup
set 0
drop 1
get 0
dbg
jump l1b
.l1a
push 3
dup
set 0
drop 1
get 0
dbg
.l1b
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