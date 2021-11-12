from tkinter import *

Window = Tk()
Window.title("Convertor")
Window.minsize(width=300, height=200)
Window.config(padx=50,pady=50)
print("Hello")


def convertLogic():
   value = float(input.get()) * 1.609
   label2.config(text=f"{round(value,2)}")


if __name__=="__main__":
   print("Starts here")
   label = Label(text="Miles  ",width=10)
   label.grid(column=0,row=0)

   input = Entry(width=15)
   input.grid(column=1,row=0)

   label1 = Label(text="Kilometers  ", width=10)
   label1.grid(column=0, row=1)
   label1.config(pady=25)

   label2 = Label(width=15)
   label2.grid(column=1, row=1)
   label2.config(pady=25)

   button = Button(text="Convert",width=20,command=convertLogic)
   button.grid(column=1,row=2)









Window.mainloop()