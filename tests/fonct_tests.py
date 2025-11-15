import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class BasicTests(unittest.TestCase):
    def fonct_declare(self):
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
        result = """resn 1
.fonction
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
resn 1
.main
resn 0
prep fonction
call 0
drop 1
push 0
ret
drop 1
.start
prep main
call 0
halt
"""
        self.assertEqual(asm, result)