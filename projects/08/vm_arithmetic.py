def unary_operation(f):
    ''' Unary operation function wrapper to hold the top element from the stack in M, popping it from the stack'''
    def wrapper(*args, **kwargs):
        command = '''@SP
                A = M-1; // Point to top element\n'''
        return command + f(*args, **kwargs)
    
    return wrapper

def binary_operator(f):
    ''' Binary operation function wrapper to extract the first element from the stack to D, second element in M, 
        popping them from the stack'''
    def wrapper(*args, **kwargs):
        command = '''@SP
                AM = M-1 // Point to where the stack top element is, decrease SP
                D = M // Take value of top element
                A = A-1 // Point to the second top element\n'''
        return command + f(*args, **kwargs)
    
    return wrapper

@unary_operation
def neg():
    return 'M = -M;\n'

@unary_operation
def not_():
    return 'M = !M;\n'

@binary_operator
def add():
    return 'M = D+M;\n'

@binary_operator
def sub():
    return 'M = M-D;\n'

@binary_operator
def and_()
    return 'M = D&M;\n'

@binary_operator
def or_():
    return 'M = D|M;\n'

cid = 0 # Compare id, used to label the comparsion jumps
jmp_instruction = {
    'eq' : 'JEQ',
    'gt' : 'JGT',
    'lt' : 'JLT',
}

@binary_operator
def compare(instruction):
    ''' Translate comparison instruciton to comparison logic on the stack by using jumps'''
    global cid
    jmp = jmp_instruction[instruction]
    command = '''D = M-D
                @h_true.{cid}
                D;{jmp}
                @h_finish.{cid}
                0;JMP
                {h_true.{cid}}
                D = -1;
                (h_finish.{cid})
                @SP
                A = M-1;
                M = D;\n'''.format(cid=cid, jmp=jmp)