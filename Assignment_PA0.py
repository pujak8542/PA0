#!/usr/bin/env python
# coding: utf-8

# # Code to Encipher

# In[1]:


def encipher():
    p = entry2.get()
    
    s=""
    for i in range(0, len(p)):
        #For checking spaces
        if p[i]==" ":
            s+=" "
        #for small letters    
        elif ord(p[i])<=122 and ord(p[i])>=97:
            x=ord('z')-(ord(p[i])-97)
            s+=chr(x)
        #for capital letters    
        else:
            x=ord('Z')-(ord(p[i])-65)
            s+=chr(x)
        
    entry3.delete(0,"end")
    entry3.insert(0, s)
        


# # Code to Decipher

# In[2]:


def decipher():
    q=entry3.get()
    
    l=""
    for i in range(0, len(q)):
        #For checking spaces
        if q[i]==" ":
            l+=" "
        #for small letters    
        elif ord(q[i])<=122 and ord(q[i])>=97:
            x=ord('z')-(ord(q[i])-97) 
            l+=chr(x)
        #for capital letters    
        else:
            x=ord('Z')-(ord(q[i])-65)
            l+=chr(x)
    entry2.delete(0,"end")
    entry2.insert(0, l)    
    


# # For deleting the entries

# In[3]:


#for deleting plain text
def delepl():
    entry2.delete(0,"end")
#for deleting cipher text    
def deleci():
     entry3.delete(0,"end")


# # Code for the User Interface

# In[ ]:


import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('900x700')
frame.configure(bg='black')
# Function for getting Input
# from textbox and printing it
# at label widget



text2 = Label(frame, text="PLAIN TEXT",bg="#000fff000")
text2.place(x=200,y=0)
text2.config(font=('Helvetica bold',15))


entry2 = tk.Entry (frame,font=('Georgia 14')) 
entry2.place(x = 200,
        y = 50,
        width=350,
        height=100)
btn = Button(frame, text = 'ENCIPHER', bd = '5',command=encipher)
btn.place(x=200, y=180)
btn.config(font=('Helvetica bold',12))

text3 = Label(frame, text="CIPHER TEXT",bg="#000fff000")
text3.place(x=660,y=0)
text3.config(font=('Helvetica bold',15))

entry3 = tk.Entry (frame,font=('Georgia 14')) 
entry3.place(x = 660,
        y = 50,
        width=350,
        height=100)
btn2 = Button(frame, text = 'DECIPHER', bd = '5',command=decipher)
btn2.place(x=660, y=180)
btn2.config(font=('Helvetica bold',12))
# Label Creation
btn3 = Button(frame, text = 'DELETE PLAIN TEXT', bd = '5',command=delepl)
btn3.place(x=200, y=230)
btn3.config(font=('Helvetica bold',12))
btn4 = Button(frame, text = 'DELETE CIPHER TEXT', bd = '5',command=deleci)
btn4.place(x=660, y=230)
btn4.config(font=('Helvetica bold',12))
frame.mainloop()


# In[ ]:




