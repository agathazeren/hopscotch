# This is the start of a python interpreter.  It does not correctly interpret all programs yet and needs much debuging and documenting.

source_code = r'''

'''



hello_world = r'''3_72>>!3_29>+>!3_7>+>!!3_3>+>!3_44!3_12!3_2@3_15>+>!<^!3_3>+>!3_-6>+>!3_10>3_10>*!3_33!
'''





#Spec:
"""
+ ADD
> PUSH
< POP
^ PEAK
/ OUT
\ IN
* MULT
? IF
@ ROT
_ NOP
[Int Literal] JUMP
"""




stack = []
code_pttr = 0
code_chars = "+<>^/\\!*?@_-0123456789"
cmd_chars = "+<>^/\\!*?@_"
num_chars = "-0123456789"
def proc_code(c):
    x = []
    n = ""
    for char in c:
        if char in num_chars:
            
                n+=char
        if char not in num_chars and n != "" and char in code_chars:
            x.append(n)
            n = ""
        if char not in code_chars:
            pass
        if char in cmd_chars:
            x.append(char)
    return x

def CMD_ADD(n):
    global stack
    return stack.pop(0) + stack.pop(0)
def CMD_PUSH(n):
    global stack
    stack = [n]+stack
    return n
def CMD_POP(n):
    global stack
    return stack.pop(0)
def CMD_PEAK(n):
    return stack[0]

def CMD_IN(n):
    return ord(input()[:1])
def CMD_OUT(n):
    print(chr(n),end="")
    return n
def CMD_MULT(n):
    global stack
    return stack.pop(0) * stack.pop(0)
def CMD_ROT(n):
    global stack
    stack.insert(0,stack.pop())
    return n
def CMD_IF(n):
    if n:
        global code_pttr
        code_pttr+=1
    return n
def CMD_NOP(n):
    return n

def run_code(xc):
    global code_pttr
    n = 0
    r = True
    
    while r:
        if code_pttr >= len(xc):
            r = False
            break
        x = xc[code_pttr]
        if x in cmd_chars:
            n = cmd_ref[x](n)
        else:
            code_pttr+=int(x)-1
            if code_pttr >= len(xc):
                r = False
                break
            if xc[code_pttr] not in cmd_chars:
                n = int(xc[code_pttr])
        code_pttr+=1
        

cmd_ref = {
    "+" :CMD_ADD,
    ">" :CMD_PUSH,
    "<" :CMD_POP,
    "^" :CMD_PEAK,
    "/" :CMD_OUT,
    "\\":CMD_IN,
    "*" :CMD_MULT,
    "?" :CMD_IF,
    "@" :CMD_ROT,
    "_" :CMD_NOP,
}




code = proc_code(source_code)
run_code(code)
            
