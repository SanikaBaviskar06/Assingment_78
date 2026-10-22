import tkinter as tk , math

root = tk.Tk()
root.title("Area of Circle")
root.geometry("400x300")

tk.Label(root, text="Enter Radius").pack()
e1 = tk.Entry(root)
e1.pack()

result = tk.Label(root, text="")
result.pack(pady=10)

def calculate():
    radius = float(e1.get())
    area = math.pi * radius * radius
    result.config(text=f"Area of Circle: {area:.2f}")

tk.Button(root, text="Calculate Area", command=calculate).pack()

root.mainloop()
