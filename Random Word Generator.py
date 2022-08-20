from tkinter import *
import random

root=Tk()

root.title("Random Word Generator")
root.geometry("500x500")


list1 = ["Fantastic" , "Gorgeous" , "Sophisticated" , "Beautiful" , "Pretty"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_word = list1[random_no]
    print("the random word is: " + random_word)
    
btn1 = Button(root)
btn1 = Button(root, text="What is the random word? ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

root.mainloop()

