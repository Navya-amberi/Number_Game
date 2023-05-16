from tkinter import * 
from tkinter import messagebox

rem = 36
i = 1
selected = 0


def Caluculate():
    global rem
    global i
    global selected

    choice = int(E1.get())

    if(choice > 6 or choice < 0):
       messagebox.showerror("Warning!", "Please choose chocolates between 1-6")
    else:
        if(rem>0):
            rem = rem - choice
            i = 2 if(i == 1) else 1

            if(rem <= 6):
                L2.configure(text= "Remaining chocolates are " + str(rem))
                for i in range(choice):
                    buttons[i + selected].config(state = "disabled")
                selected = selected + choice
                messagebox.showinfo("Game End!", "Remaining chocolates are "+str(rem)+" So, Player "+str(i)+" is Winner!! Yayy!!!")
                root.destroy()

            L1.configure(text= "                Player "+ str(i)+" Enter your choice here: ")
            L2.configure(text= "Remaining chocolates are " + str(rem))
            
            for i in range(choice):
                buttons[i + selected].config(state = "disabled")
            selected = selected + choice

    E1.delete(first=0,last=100)









root = Tk()             
root.geometry('1000x1000')

frame = Frame(root)
frame.grid(row=4, column=1)

L1 = Label(root, text="                 Player 1 Enter your Choice here: ")
L1.grid(row = 0, column = 0, sticky = W, pady = 1)

E1 = Entry(root, bd =5, width=30)
E1.grid(row = 0, column = 2, sticky = W, pady = 2)

B1 = Button(root, text = 'Enter ', bd = '5', command = Caluculate)
B1.grid(row = 1, column = 1, sticky = W, pady = 3)

L2 = Label(root, text="Remaining chocolates are 36")
L2.grid(row = 2, column = 0, sticky = W, pady = 1)


photo = PhotoImage(file = r"choco1.png").subsample(1,1)


buttons = []
k = 1
for i in range(1,7):
    for j in range(1,7):
        btn = Button(frame, text= k, image=photo)
        k = k + 1
        btn.grid(row=i, column=j)
        buttons.append(btn)







root.mainloop()