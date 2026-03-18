import tkinter as tk

root = tk.Tk()

SWIDTH = root.winfo_screenwidth()
SHEIGHT = root.winfo_screenheight()

root.title("Money Tracker (updated)")
root.geometry(f"{SWIDTH}x{SHEIGHT}")

BG = "lightblue"
root.config(bg=BG)

STL = tk.Label(text="Enter \n \nthe \n \nmoney \n \nyou \n \nhave \n \nas \n \nper \n \nthe \n \nnumber \n \nof \n \nnotes:", font=("Arial", 30), bg=BG)
STL.place(x=SWIDTH//2-650, y=SHEIGHT//11-80)

E500N = tk.Entry(font=("Arial", 15))
E500N.place(x=SWIDTH//2, y=SHEIGHT//11-80)

L500N = tk.Label(text="Number of ₹500 notes", font=("Arial", 20), bg=BG)
L500N.place(x=SWIDTH//2-300, y=SHEIGHT//11-80)

T500N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T500N.place(x=SWIDTH//2+400, y=SHEIGHT//11-80)

E200N = tk.Entry(font=("Arial", 15))
E200N.place(x=SWIDTH//2, y=SHEIGHT//11)

L200N = tk.Label(text="Number of ₹200 notes", font=("Arial", 20), bg=BG)
L200N.place(x=SWIDTH//2-300, y=SHEIGHT//11)

T200N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T200N.place(x=SWIDTH//2+400, y=SHEIGHT//11)

E100N = tk.Entry(font=("Arial", 15))
E100N.place(x=SWIDTH//2, y=SHEIGHT//11+100)

L100N = tk.Label(text="Number of ₹100 notes", font=("Arial", 20), bg=BG)
L100N.place(x=SWIDTH//2-300, y=SHEIGHT//11+100)

T100N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T100N.place(x=SWIDTH//2+400, y=SHEIGHT//11+100)

E50N = tk.Entry(font=("Arial", 15))
E50N.place(x=SWIDTH//2, y=SHEIGHT//11+200)

L50N = tk.Label(text="Number of ₹50 notes", font=("Arial", 20), bg=BG)
L50N.place(x=SWIDTH//2-300, y=SHEIGHT//11+200)

T50N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T50N.place(x=SWIDTH//2+400, y=SHEIGHT//11+200)

E20N = tk.Entry(font=("Arial", 15))
E20N.place(x=SWIDTH//2, y=SHEIGHT//11+300)

L20N = tk.Label(text="Number of ₹20 notes", font=("Arial", 20), bg=BG)
L20N.place(x=SWIDTH//2-300, y=SHEIGHT//11+300)

T20N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T20N.place(x=SWIDTH//2+400, y=SHEIGHT//11+300)

E10N = tk.Entry(font=("Arial", 15))
E10N.place(x=SWIDTH//2, y=SHEIGHT//11+400)

L10N = tk.Label(text="Number of ₹10 notes", font=("Arial", 20), bg=BG)
L10N.place(x=SWIDTH//2-300, y=SHEIGHT//11+400)

T10N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T10N.place(x=SWIDTH//2+400, y=SHEIGHT//11+400)

E10C = tk.Entry(font=("Arial", 15))
E10C.place(x=SWIDTH//2, y=SHEIGHT//11+500)

L10C = tk.Label(text="Number of ₹10 coins", font=("Arial", 20), bg=BG)
L10C.place(x=SWIDTH//2-300, y=SHEIGHT//11+500)

T10C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T10C.place(x=SWIDTH//2+400, y=SHEIGHT//11+500)

E5C = tk.Entry(font=("Arial", 15))
E5C.place(x=SWIDTH//2, y=SHEIGHT//11+600)

L5C = tk.Label(text="Number of ₹5 coins", font=("Arial", 20), bg=BG)
L5C.place(x=SWIDTH//2-300, y=SHEIGHT//11+600)

T5C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T5C.place(x=SWIDTH//2+400, y=SHEIGHT//11+600)

E2C = tk.Entry(font=("Arial", 15))
E2C.place(x=SWIDTH//2, y=SHEIGHT//11+700)

L2C = tk.Label(text="Number of ₹2 coins", font=("Arial", 20), bg=BG)
L2C.place(x=SWIDTH//2-300, y=SHEIGHT//11+700)

T2C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T2C.place(x=SWIDTH//2+400, y=SHEIGHT//11+700)

E1C = tk.Entry(font=("Arial", 15))
E1C.place(x=SWIDTH//2, y=SHEIGHT//11+800)

L1C = tk.Label(text="Number of ₹1 coins", font=("Arial", 20), bg=BG)
L1C.place(x=SWIDTH//2-300, y=SHEIGHT//11+800)

T1C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T1C.place(x=SWIDTH//2+400, y=SHEIGHT//11+800)

GB = tk.Button(text="Get total", font=("Arial", 20), command=lambda: get_total(), bg=BG)
GB.place(x=SWIDTH//2+600, y=SHEIGHT//2)

TA = tk.Label(text="Total amount: ₹0", font=("Arial", 30), bg=BG)
TA.place(x=SWIDTH//2+500, y=SHEIGHT//2+100)

RB = tk.Button(text="Reset", font=("Arial", 20), command=lambda: reset(), bg=BG)
RB.place(x=SWIDTH//2+600, y=SHEIGHT//2+200)


def get_total():
    STL.config(text=" ")


    try:


        n500 = int(E500N.get())
        n200 = int(E200N.get())
        n100 = int(E100N.get())
        n50 = int(E50N.get())
        n20 = int(E20N.get())
        n10n = int(E10N.get())
        n10c = int(E10C.get())
        n5c = int(E5C.get())
        n2c = int(E2C.get())
        n1c = int(E1C.get())

        if n500 < 0 or n200 < 0 or n100 < 0 or n50 < 0 or n20 < 0 or n10n < 0 or n10c < 0 or n5c < 0 or n2c < 0 or n1c < 0:
            TA.config(text="Please enter non-negative numbers.")
            return
        

        total = (n500*500) + (n200*200) + (n100*100) + (n50*50) + (n20*20) + (n10n*10) + (n10c*10) + (n5c*5) + (n2c*2) + (n1c*1)

        T500N.config(text=f"=  ₹{n500*500}")
        T200N.config(text=f"=  ₹{n200*200}")
        T100N.config(text=f"=  ₹{n100*100}")
        T50N.config(text=f"=  ₹{n50*50}")
        T20N.config(text=f"=  ₹{n20*20}")
        T10N.config(text=f"=  ₹{n10n*10}")
        T10C.config(text=f"=  ₹{n10c*10}")
        T5C.config(text=f"=  ₹{n5c*5}")
        T2C.config(text=f"=  ₹{n2c*2}")
        T1C.config(text=f"=  ₹{n1c*1}")

        STL.config(text=f"Number of notes you have = {n500+n200+n100+n50+n20+n10n}\n\n\nNumber of coins you have = {n10c+n5c+n2c+n1c}")
        STL.place(x=SWIDTH//2-900, y=SHEIGHT//11-80)

        TA.config(text=f"Total amount: ₹{total}")

    except ValueError:
        TA.config(text="Please enter valid numbers.") 
    

def reset():
    E500N.delete(0, tk.END)
    E200N.delete(0, tk.END)
    E100N.delete(0, tk.END)
    E50N.delete(0, tk.END)
    E20N.delete(0, tk.END)
    E10N.delete(0, tk.END)
    E10C.delete(0, tk.END)
    E5C.delete(0, tk.END)
    E2C.delete(0, tk.END)
    E1C.delete(0, tk.END)

    T500N.config(text="=  ₹0")
    T200N.config(text="=  ₹0")
    T100N.config(text="=  ₹0")
    T50N.config(text="=  ₹0")
    T20N.config(text="=  ₹0")
    T10N.config(text="=  ₹0")
    T10C.config(text="=  ₹0")
    T5C.config(text="=  ₹0")
    T2C.config(text="=  ₹0")
    T1C.config(text="=  ₹0")

    STL.config(text="Enter \n \nthe \n \nmoney \n \nyou \n \nhave \n \nas \n \nper \n \nthe \n \nnumber \n \nof \n \nnotes:")
    STL.place(x=SWIDTH//2-650, y=SHEIGHT//11-80)

    TA.config(text="Total amount: ₹0")



root.mainloop()