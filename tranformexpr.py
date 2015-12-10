import sys
import string

operators = ['+', '-', '*', '/', '^']

n = int(raw_input())

def isoperator(char):
        if char in operators:
                return True
        else:
                return False

def process_line(line):
        stck = []
        output = ""
        for i in range(0,len(line)):
                if line[i].isalpha():
                        output += line[i]
                else:
                        if isoperator(line[i]):
                                while len(stck) >0 and stck[-1] in operators and operators.index(line[i]) < operators.index(stck[-1]): #lower precendence of new operator, so pop the higher precendence from stck
                                        output+=stck.pop()
                                stck.append(line[i])
                        elif line[i] == ')': #is a closing brace
                                while stck[-1] != '(' :
                                        output+=stck.pop()
                                stck.pop()
                        else : # opening brace, and put it to stck
                                stck.append(line[i])
                #print "stck     :" + str(stck)
                #print "output   :" + output
        while len(stck) > 0:
                output+=stck.pop()
        print output

while n > 0:
        line = raw_input()
        n-=1
        process_line(line)