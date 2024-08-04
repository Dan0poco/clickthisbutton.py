from tkinter import *

print('Welcome to my first python GUI app haha i like it')
print()

count = 0
def click():
    global count
    count+=1
    label.config(text=count)
    print("Logs",count)

                          #<3
window = Tk()
window.title("Counter")

button = Button(window,text='Click me') 
button.config(command=click)
button.config(font=('Monospace',50,'bold'))
button.config(bg='#3ae7f0') 
label = Label(window,text=count)
label.config(font=('Monospace',50))
label.pack()
button.pack()
window.mainloop()
