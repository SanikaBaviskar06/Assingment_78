import tkinter as tk

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("400x300")

tk.Label(root, text="Username").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Password").pack()
e2 = tk.Entry(root, show="*")
e2.pack()

result = tk.Label(root, text="")
result.pack(pady=10)

def login():
    username = e1.get()
    password = e2.get()

    if username == "sanika" and password == "1234":
        result.config(text="Login Successful")
    else:
        result.config(text="Invalid Username or Password")

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
