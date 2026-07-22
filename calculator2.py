import tkinter as tk

def click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill="both", ipadx=8, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

frame = tk.Frame(root)
frame.pack()

for button in buttons:
    b = tk.Button(frame, text=button, font="Arial 15", width=5, height=2)
    b.bind("<Button-1>", click)
    b.pack(side="left")

clear = tk.Button(root, text="C", font="Arial 15", height=2)
clear.bind("<Button-1>", click)
clear.pack(fill="both")

root.mainloop()