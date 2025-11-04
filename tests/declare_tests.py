import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class DeclareTests(unittest.TestCase):
    def test_constante_pos_v(self):
        code = """
        void main(){
            24;
            +12;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 24
drop 1
push 12
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
    
    def test_constante_neg_2(self):
        code = """
        void main(){
            (-24);
            - 13;
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
push 13
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
    
    def test_constante_add(self):
        code = """
        void main(){
            2 + 6;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 2
push 6
add
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
        
    def test_constante_sub(self):
        code = """
        void main(){
            2 - 6;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 2
push 6
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
    
    def test_constante_mul(self):
        code = """
        void main(){
            10*3;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 10
push 3
mul
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
    
    def test_constante_calcul_1(self):
        code = """
        void main(){
            (-10)*3 + 2;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 0
push 10
sub
push 3
mul
push 2
add
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
        
    def test_constante_calcul_2(self):
        code = """
        void main(){
            (-10 - 2)*(-24);
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 0
.main
resn 0
push 0
push 10
sub
push 2
sub
push 0
push 24
sub
mul
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
    
        
        
if __name__ == '__main__':
    unittest.main()