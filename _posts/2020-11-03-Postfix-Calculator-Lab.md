# PostFix Calculator Lab
Worked on With Anthony White

#### 1. Calculate what each line in calculate_me.csv evaluates to. The only operators are +, -, and *! There is no /. 
#### What is the average of all the final values?
Average =  529.91

#### 2. Explain how a stack is used to evaluate postfix notation.
Since in postfix notation you need to utilize only the first two numbers you have on hand,
you use a stack to store and access numbers in that order.

For example, if you had a list [3, 4, 10, +, 6, *, -],
The code would read it like:
~~~
[3]
[3, 4]
[3, 4, 10]
[3, 4 + 10] = [3, 14]
[3, 14, 6]
[3, 14 * 6] = [3, 84]
[3 - 84] = [-81]
~~~
The operator would only be applied when it's encountered in the list to the last two numbers in the list, or rather the top two numbers on the Stack.

#### 3. Describe your process of how you worked on this lab. Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response!
Worked on With Anthony White

This lab I found was also quite difficult in how specific it had to be, a problem I found I encountered similarly with the Iris Lab we did earlier.

A lot of the code utilized in this lab was adapted from the Iris Lab in terms of importing the .csv file syntax and parsing through rows in that file. A couple things that I changed include changing from _csv.DictReader_ to _csv.reader_, so that the file was now in list format rather than dictionary as Stacks work with lists, at least in this case.

Another important thing to mention is the minute changes I made within the Stack Class.
~~~
class Stack:
    def __init__(self, elements=[]):
        self.stack = elements
       
    
    def peek(self):
        return self.stack[-1]

    def push(self, element):
        self.stack.append(element)
        return None

    def pop(self):
        temp = self.stack[-1]
        del self.stack[-1]
        return temp

    def __repr__(self):
        return str(self.stack)
~~~
So here I changed the return for push() to _None_, in addition to changing the pop() method to delete the first element in a Stack within the method.


Looking back at the code for the PostFix Lab, it isn't very complicated. However I found myself missing certain details or necessities while writing the code. For instance, I needed to find a method of the sorts to identify if a string was a number or not. I went through a couple things (check links on postfix.py for info), until eventually finding isnumeric(), which needs to have the string attached to it rather than in its parameter. Ex. ("21").isnumeric(), and would return a boolean.

Using this method, I could then identify if this was an operator or number, and if it was an operator, apply that operation to the top two numbers on the Stack. Both strings are casted to a _float_.

~~~
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
~~~

Another thing I had to address was how to identify exactly _which operator_ was being applied onto the Stack, and then apply it. I wanted to make the code as amendable as possible, so not specific to just this problem, so I made it so it accesses a list of operators which acts like a key on a chart.
~~~
import operator
~~~
~~~
oper = {"+": operator.add, "-": operator.sub, "*": operator.mul}
~~~
~~~
for i in oper: #identify which operator matches the string version
    if i == row[x]:
        tempOper = oper[i]

temp = tempOper(num2, num1) #executes operator onto two numbers
tempStack.push(temp) #push new Number to Stack
~~~
Iterates through the list, looking to see which operator encountered matches which operator on the operator list. That operator is then saved, and then applied to the two numbers.

One major problem I ran into here that Anthony helped with that I almost didn't catch was the order of applying operators to the numbers. Beforehand I had _temp = tempOper(**num1**, **num2**)_, giving me an entirely different list of numbers and an average of _329.27_. All this simply because I applied the operator to the numbers in the wrong order.

Ex. [4, 8, 9]
operator = *
temp = 8*9

You need to make it so that the 2nd number(number after the first on the Stack) is the one you have at the beginning of the expression. Basically you want 8x9 rather than what I originally did, which was 9x8.

Everything else is self explanatory, so I will leave that out.

#### Conclusion
This lab required a lot of minute changes and a need to figure out/discover new things about Python, especially since I am fairly new to it. In general though, it was not too bad and I feel like I understand Python a lot better now than before, in addition to understanding how classes work together in Python.


