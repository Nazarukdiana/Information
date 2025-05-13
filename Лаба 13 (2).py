import tkinter as tk
from math import sqrt

def calculate(event=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    median_b = 0.5 * sqrt(2 * a**2 + 2 * c**2 - b**2)

    s = (a + b + c) / 2

    area = sqrt(s * (s - a) * (s - b) * (s - c))

    height_c = 2 * area / c

    result_text = f"Медіана до b: {median_b:.2f} см\nВисота до c: {height_c:.2f} см"
    label_result.config(text=result_text)

root = tk.Tk()
root.title("Обчислення елементів трикутника")
root.geometry("300x200")

label_a = tk.Label(root, text="Введіть сторону a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.insert(0, "11.3")
entry_a.pack()

label_b = tk.Label(root, text="Введіть сторону b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.insert(0, "15.9")
entry_b.pack()

label_c = tk.Label(root, text="Введіть сторону c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.insert(0, "20.7")
entry_c.pack()

button_calc = tk.Button(root, text="Обчислити")
button_calc.pack()
button_calc.bind('<Button-1>', calculate)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
