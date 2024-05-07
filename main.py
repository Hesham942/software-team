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
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)