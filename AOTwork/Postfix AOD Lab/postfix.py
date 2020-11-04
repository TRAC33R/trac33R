
import csv
import operator
from Stack import Stack

average_list = []
oper = {"+": operator.add, "-": operator.sub, "*": operator.mul}
##https://stackoverflow.com/questions/1740726/turn-string-into-operator
##https://www.csee.umbc.edu/courses/331/fall11/notes/python/python3.ppt.pdf
##https://note.nkmk.me/en/python-check-int-float/
##https://www.tutorialspoint.com/python/dictionary_len.htm
##https://stackoverflow.com/questions/31366231/how-to-check-if-two-boolean-values-are-equal
##https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
##https://www.w3schools.com/python/ref_string_isnumeric.asp

'''
WORKED ON WITH ANTHONY WHITE
'''

with open("calculate_me.csv", "r") as f: #Parse through iris.csv file found at relative path folder "Datasets"
    data = csv.reader(f) #Reads the .csv file in dictionary format
        
        
    for row in data: #Go through rows in compiled dataset
        tempStack = Stack()
        is_operator = False
            

        for x in range(0, len(row)):
            
            if (row[x]).isnumeric() == is_operator: #if this is NOT a float / or is an Operator
                num1 = float(tempStack.peek())
                tempStack.pop()
                num2 = float(tempStack.peek())
                tempStack.pop()

                for i in oper: #identify which operator matches the string version
                    if i == row[x]:
                        tempOper = oper[i]

                temp = tempOper(num2, num1) #executes operator onto two numbers
                tempStack.push(temp) #push new Number to Stack
                #print(tempStack)

            else: #else just add number in list to stack
                tempStack.push(row[x])
                #print(tempStack)

            #print(tempStack)
        tempNumber = float(tempStack.peek())
        average_list.append(tempNumber)

    finalAverage = 0

    for n in average_list:
        finalAverage += float(n)

    returnAverage = finalAverage / len(average_list)
    
    print(returnAverage)
    
    
                

#1. Calculate what each line in calculate_me.csv evaluates to. The only operators are +, -, and *! There is no /. 
#What is the average of all the final values?
'''
Average =  529.91
'''

#2. Explain how a stack is used to evaluate postfix notation.
'''
Since in postfix notation you need to utilize only the first two numbers you have on hand,
you use a stack to store and access numbers in that order.

For example, if you had a list [3, 4, 10, +, 6, *, -],
The code would read it like:
[3]
[3, 4]
[3, 4, 10]
[3, 4 + 10] = [3, 14]
[3, 14, 6]
[3, 14 * 6] = [3, 84]
[3 - 84] = [-81]

The operator would only be applied when it's encountered in the list to the
last two numbers in the list, or rather the top two numbers on the Stack.
'''

#3. Describe your process of how you worked on this lab. Include details such as who you worked with, 
# what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. 
# Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response!