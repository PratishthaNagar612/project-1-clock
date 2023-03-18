#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
from tkinter.ttk import*


# In[ ]:


from time import strftime


# In[ ]:


root=Tk()
root.title("clock")


# In[ ]:


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)


# In[ ]:


label = Label(root, font=("ds-digital",80), background="black", foreground = "cyan")
label.pack(anchor='center')
time()
mainloop()


# In[ ]:





# In[ ]:




