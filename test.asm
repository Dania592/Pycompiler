.add
resn 1
get 0
get 1
add
dup
set 2
drop 1
get 2
ret
push 0
ret
.main
resn 1
push 10
dup
set 0
drop 1
get 0
push 10
cmpeq
jumpf l1a
push 1
dbg
jump l1b
.l1a
push 0
dbg
.l1b
prep add
get 0
push 5
call 2
dbg
push 0
ret
push 0
ret
.start
prep main
call 0
halt

