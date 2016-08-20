# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:53:09 2016

@author: pengcheng
"""
class Stack:
    def __init__(self):
        self.items=[]
        
    def isempty(self):
        return self.items==[]
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self,index=-1):
        return self.items[index]
        
    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        

def parChecker(symbolString):
#    print (symbolString)
    s=Stack()
    balanced= True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isempty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False
        index=index+1
        
    if balanced and s.isempty():
        return True
    else:
        return False
        
def matches(opens,closes):
    print(opens)
    print(closes)
    Opens=['(','[','{']
    
    closers=[')',']','}']
    return Opens.index(opens)==closers.index(closes)
    
def infixToPostfix(infixepr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    
    opStack=Stack()
    postfixList=[]
    tokenlist=infixepr.split()
    
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" or token in "123456789":
            postfixList.append(token)
        elif token=='(':
            opStack.push(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
                
        else:
            while (not opStack.isempty()) and (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
            
    while not opStack.isempty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
    
#print (infixToPostfix("A * B + C * D"))
#print (infixToPostfix("( A + B ) * C"))

def postfixEval(postfixExpr):
    operandStack=Stack()
    tokenList=postfixExpr.split()
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
            
    return operandStack.pop()
    
def doMath(op,op1,op2):
    if op =="*":
        return op1*op2
    elif op=="/":
        return op1/op2
    elif op=="+":
        return op1+op2
    else:
        return op1-op2
        
#print (postfixEval('7 8 + 3 2 + /'))
    
def baseConverter(decNumber, base):
    digits="0123456789ABCDEF"
    
    remstack=Stack()
    while decNumber>0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber=decNumber//base
        
    newString=""
    while not remstack.isempty():
        newString=newString+digits[remstack.pop()]
        
    return newString
    

     
            
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                    