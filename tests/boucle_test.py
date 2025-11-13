import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class DeclareTests(unittest.TestCase):
    def for_pos(self):
        code = """
void main(){
    int i;
    for(i = 0; i <= 5; i = i+1){
        debug i;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 0
dup
set 2
drop 1
.l1a
get 2
push 5
cmple
jumpf l2a
get 2
dbg
.l1c
get 2
push 1
add
dup
set 2
drop 1
jump l2b
.l2a
jump l1b
.l2b
jump l1a
.l1b
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def for_neg(self):
        code = """
void main(){
    int i;
    for(i = 10; i > 5; i = i-1){
        debug i;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 10
dup
set 2
drop 1
.l1a
get 2
push 5
cmpgt
jumpf l2a
get 2
dbg
.l1c
get 2
push 1
sub
dup
set 2
drop 1
jump l2b
.l2a
jump l1b
.l2b
jump l1a
.l1b
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

    def for_imbrique(self):
        code = """
void main(){
    int i;
    int j;
    int x;
    for(i = 10; i > 5; i = i-1){
        for(j = 2; j < 24; j = j*2){
            x = i*j;
            debug x;
        }
        debug i;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 10
dup
set 2
drop 1
.l1a
get 2
push 5
cmpgt
jumpf l2a
push 2
dup
set 4
drop 1
.l3a
get 4
push 24
cmplt
jumpf l4a
get 2
get 4
mul
dup
set 6
drop 1
get 6
dbg
.l3c
get 4
push 2
mul
dup
set 4
drop 1
jump l4b
.l4a
jump l3b
.l4b
jump l3a
.l3b
get 2
dbg
.l1c
get 2
push 1
sub
dup
set 2
drop 1
jump l2b
.l2a
jump l1b
.l2b
jump l1a
.l1b
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        

    def boucle_while(self):
        code = """
        void main(){
            -24;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 0
push 24
sub
drop 1
push 0
ret
drop 0
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)


    def test_constante_neg_1(self):
        code = """
        void main(){
            -24;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 0
push 24
sub
drop 1
push 0
ret
drop 0
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        

    def test_constante_neg_1(self):
        code = """
        void main(){
            -24;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 0
push 24
sub
drop 1
push 0
ret
drop 0
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        

    def test_constante_neg_1(self):
        code = """
        void main(){
            -24;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 0
push 24
sub
drop 1
push 0
ret
drop 0
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)