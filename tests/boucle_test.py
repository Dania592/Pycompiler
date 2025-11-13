import unittest 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CompilateurC import compiler

class BoucleTest(unittest.TestCase):
    def test_for_pos(self):
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
jumpf l1b
get 2
dbg
.l1c
get 2
push 1
add
dup
set 2
drop 1
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
        
    def test_for_neg(self):
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
jumpf l1b
get 2
dbg
.l1c
get 2
push 1
sub
dup
set 2
drop 1
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

    def test_for_imbrique(self):
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
jumpf l1b
push 2
dup
set 4
drop 1
.l2a
get 4
push 24
cmplt
jumpf l2b
get 2
get 4
mul
dup
set 6
drop 1
get 6
dbg
.l2c
get 4
push 2
mul
dup
set 4
drop 1
jump l2a
.l2b
get 2
dbg
.l1c
get 2
push 1
sub
dup
set 2
drop 1
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
        

    def test_boucle_while(self):
        code = """
void main(){
    int i;
    i = 2;
    while(i < 10){
        i = i + 1;
        debug i;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 2
dup
set 2
drop 1
.l1a
get 2
push 10
cmplt
jumpf l1b
get 2
push 1
add
dup
set 2
drop 1
get 2
dbg
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


    def test_boucle_do_while(self):
        code = """
void main(){
    int i;
    i = 15;
    do{
        i = i - 1;
        debug i;
    }while(i > 1);
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 15
dup
set 2
drop 1
.l1a
get 2
push 1
sub
dup
set 2
drop 1
get 2
dbg
.l1c
get 2
push 1
cmpgt
not
jumpf l2a
jump l1b
jump l2b
.l2a
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
        

    def test_boucle_do_while_cond(self):
        code = """
void main(){
    int i;
    i = 15;
    do{
        if (i == 5){
            i = 2;
        }else{
            i = i - 1;
        }
        debug i;
    }while(i > 1);
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 15
dup
set 2
drop 1
.l1a
get 2
push 5
cmpeq
jumpf l2a
push 2
dup
set 2
drop 1
jump l2b
.l2a
get 2
push 1
sub
dup
set 2
drop 1
.l2b
get 2
dbg
.l1c
get 2
push 1
cmpgt
not
jumpf l3a
jump l1b
jump l3b
.l3a
.l3b
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
        

    def test_boucle_while_cond(self):
        code = """
void main(){
    int i;
    i = 15;
    while(i > 1){
        if (i == 5){
            i = 2;
        }else{
            i = i - 1;
        }
        debug i;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 15
dup
set 2
drop 1
.l1a
get 2
push 1
cmpgt
jumpf l1b
get 2
push 5
cmpeq
jumpf l2a
push 2
dup
set 2
drop 1
jump l2b
.l2a
get 2
push 1
sub
dup
set 2
drop 1
.l2b
get 2
dbg
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

    def test_boucle_for_cond(self):
        code = """
void main(){
    int i;
    for(i = 15; i > 1; i = i - 1){
        if (i == 5){
            i = 2;
        }else{
            i = i - 1;
        }
        debug i;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 15
dup
set 2
drop 1
.l1a
get 2
push 1
cmpgt
jumpf l1b
get 2
push 5
cmpeq
jumpf l2a
push 2
dup
set 2
drop 1
jump l2b
.l2a
get 2
push 1
sub
dup
set 2
drop 1
.l2b
get 2
dbg
.l1c
get 2
push 1
sub
dup
set 2
drop 1
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
        

    def test_boucle_while_break(self):
        code = """
void main(){
    int i;
    i = 15;
    while(i > 1){
        if (i == 5){
            i = 18;
            break;
        }else{
            i = i - 1;
        }
        debug i;
    }
    debug i;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 15
dup
set 2
drop 1
.l1a
get 2
push 1
cmpgt
jumpf l1b
get 2
push 5
cmpeq
jumpf l2a
push 18
dup
set 2
drop 1
jump l1b
jump l2b
.l2a
get 2
push 1
sub
dup
set 2
drop 1
.l2b
get 2
dbg
jump l1a
.l1b
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
        
    def test_boucle_while_continue(self):
        code = """
void main(){
    int i;
    i = 5;
    while(i < 20){
        if (i == 9){
            i = 18;
            continue;
        }else{
            i = i + 1;
        }
        debug i;
    }
    debug i;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 5
dup
set 2
drop 1
.l1a
get 2
push 20
cmplt
jumpf l1b
get 2
push 9
cmpeq
jumpf l2a
push 18
dup
set 2
drop 1
jump l1a
jump l2b
.l2a
get 2
push 1
add
dup
set 2
drop 1
.l2b
get 2
dbg
jump l1a
.l1b
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
        
    def test_boucle_do_while_break(self):
        code = """
void main(){
    int i;
    i = 15;
    do{
        if (i == 5){
            i = 18;
            break;
        }else{
            i = i - 1;
        }
        debug i;
    }while(i > 1);
    debug i;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 15
dup
set 2
drop 1
.l1a
get 2
push 5
cmpeq
jumpf l2a
push 18
dup
set 2
drop 1
jump l1b
jump l2b
.l2a
get 2
push 1
sub
dup
set 2
drop 1
.l2b
get 2
dbg
.l1c
get 2
push 1
cmpgt
not
jumpf l3a
jump l1b
jump l3b
.l3a
.l3b
jump l1a
.l1b
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
        
        
    def test_boucle_do_while_continue(self):
        code = """
void main(){
    int i;
    i = 5;
    do{
        if (i == 9){
            i = 18;
            continue;
        }else{
            i = i + 1;
        }
        debug i;
    }while(i < 29);
    debug i;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 5
dup
set 2
drop 1
.l1a
get 2
push 9
cmpeq
jumpf l2a
push 18
dup
set 2
drop 1
jump l1a
jump l2b
.l2a
get 2
push 1
add
dup
set 2
drop 1
.l2b
get 2
dbg
.l1c
get 2
push 29
cmplt
not
jumpf l3a
jump l1b
jump l3b
.l3a
.l3b
jump l1a
.l1b
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
        

    def test_boucle_for_break(self):
        code = """
void main(){
    int i;
    for(i = 5; i < 20; i = i + 1){
        if (i > 15){
            i = 29;
            break;
        }else{
            i = i + 1;
        }
        debug i;
    }
    debug i;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 5
dup
set 2
drop 1
.l1a
get 2
push 20
cmplt
jumpf l1b
get 2
push 15
cmpgt
jumpf l2a
push 29
dup
set 2
drop 1
jump l1b
jump l2b
.l2a
get 2
push 1
add
dup
set 2
drop 1
.l2b
get 2
dbg
.l1c
get 2
push 1
add
dup
set 2
drop 1
jump l1a
.l1b
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
        
    def test_boucle_for_continue(self):
        code = """
void main(){
    int i;
    for(i = 5; i < 20; i = i + 1){
        if (i == 9){
            i = 18;
            continue;
        }else{
            i = i + 1;
        }
        debug i;
    }
    debug i;
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 5
dup
set 2
drop 1
.l1a
get 2
push 20
cmplt
jumpf l1b
get 2
push 9
cmpeq
jumpf l2a
push 18
dup
set 2
drop 1
jump l1a
jump l2b
.l2a
get 2
push 1
add
dup
set 2
drop 1
.l2b
get 2
dbg
.l1c
get 2
push 1
add
dup
set 2
drop 1
jump l1a
.l1b
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
        
    def test_boucle_for_while(self):
        code = """
void main(){
    int i;
    int j;
    for(j = 0; j < 10; j = j + 1){
        debug j;
        i = 0;
        while(i < 5){
            debug i;
            i = i + 1; 
        }
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 0
dup
set 4
drop 1
.l1a
get 4
push 10
cmplt
jumpf l1b
get 4
dbg
push 0
dup
set 2
drop 1
.l2a
get 2
push 5
cmplt
jumpf l2b
get 2
dbg
get 2
push 1
add
dup
set 2
drop 1
jump l2a
.l2b
.l1c
get 4
push 1
add
dup
set 4
drop 1
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
        
    def test_boucle_for_do_while(self):
        code = """
void main(){
    int i;
    int j;
    for(j = 0; j < 10; j = j + 1){
        debug j;
        i = 0;
        do{
            debug i;
            i = i + 1; 
        }while(i < 5);
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 0
dup
set 4
drop 1
.l1a
get 4
push 10
cmplt
jumpf l1b
get 4
dbg
push 0
dup
set 2
drop 1
.l2a
get 2
dbg
get 2
push 1
add
dup
set 2
drop 1
.l2c
get 2
push 5
cmplt
not
jumpf l3a
jump l2b
jump l3b
.l3a
.l3b
jump l2a
.l2b
.l1c
get 4
push 1
add
dup
set 4
drop 1
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
        
    def test_boucle_while_do_while(self):
        code = """
void main(){
    int i;
    int j;
    j = 0;
    while(j < 10){
        debug j;
        i = 0;
        do{
            debug i;
            i = i + 1; 
        }while(i < 5);
        j = j + 1;
    }
}
        """
        asm = compiler(code).encode('utf-8').decode('unicode_escape')
        result = """resn 1
.main
resn 0
push 0
dup
set 4
drop 1
.l1a
get 4
push 10
cmplt
jumpf l1b
get 4
dbg
push 0
dup
set 2
drop 1
.l2a
get 2
dbg
get 2
push 1
add
dup
set 2
drop 1
.l2c
get 2
push 5
cmplt
not
jumpf l3a
jump l2b
jump l3b
.l3a
.l3b
jump l2a
.l2b
get 4
push 1
add
dup
set 4
drop 1
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

if __name__ == '__main__':
    unittest.main()