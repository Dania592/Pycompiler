import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class DeclareTests(unittest.TestCase):
    def test_constante_pos_v(self):
        code = """
        void main(){
            int x;
            x = 1;
            debug x;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 1
dup
set 2
drop 1
get 2
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def test_constante_neg_1(self):
        code = """
        void main(){
            int x;
            x = -24;
            debug x;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 0
push 24
sub
dup
set 2
drop 1
get 2
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

    def declare_add(self):
        code = """
        void main(){
            int x;
            x = (-10)*3 + 2;
            debug x;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 0
push 10
sub
push 3
mul
push 2
add
dup
set 2
drop 1
get 2
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)
        
    def declare_add2(self):
        code = """
        void main(){
            int x;
            x = 1;
            x = x + 2;
            debug x;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 3
dup
set 2
drop 1
get 2
push 2
add
dup
set 2
drop 1
get 2
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

           
    def declare_add_var(self):
        code = """
        void main(){
            int x;
            int y; 
            int z; 
            x = 1;
            y = 2;
            z = 3;
            debug x;
            debug y;
            debug z;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 1
dup
set 2
drop 1
push 2
dup
set 4
drop 1
push 3
dup
set 6
drop 1
get 2
dbg
get 4
dbg
get 6
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

    def declare_var_bloc(self):
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
        result = """resn 1
.main
resn 0
push 1
dup
set 2
drop 1
get 2
dbg
push 26
dup
set 6
drop 1
get 6
dbg
push 12
dup
set 8
drop 1
get 8
dbg
get 2
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

    
    def declare_var_add(self):
        code = """
        void main(){
            int x;
            int y; 
            x = 1;
            y = x + 4;
            debug x;
            debug y;
        }
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 1
dup
set 2
drop 1
get 2
push 4
add
dup
set 4
drop 1
get 2
dbg
get 4
dbg
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)

        
if __name__ == '__main__':
    unittest.main()