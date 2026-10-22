import tkinter as tk

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("400x300")

tk.Label(root, text="Enter Your Name").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Your Age").pack()
e2 = tk.Entry(root)
e2.pack()

result = tk.Label(root, text="")
result.pack(pady=10)

def check():
    name = e1.get()
    age = int(e2.get())

    if age >= 18:
        result.config(text=f"{name}, You are Eligible to Vote")
    else:
        result.config(text=f"{name}, You are Not Eligible to Vote")

tk.Button(root, text="Check Eligibility", command=check).pack()

root.mainloop()
