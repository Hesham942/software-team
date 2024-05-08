from tkinter import *
import math


'''
Functions
'''
# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)


 # Function to calculate the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)   

# Function to find the square root of a number
def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Function to find the third root of a number
def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Function to change the sign of number
def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp

def percent():
    global calc_operator
    temp = str(eval(calc_operator + '/100'))
    calc_operator = temp
    text_input.set(temp)

