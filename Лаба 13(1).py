import tkinter as tk
from math import cos, sqrt, radians

def calculate_function(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        numerator = a + cos(radians(b))
        denominator = 3 * a + 4 * sqrt(a + c)
        result = numerator / denominator - 5 * c

        format_result = "{:.2f}".format(result)
        label_result.config(text="Результат: " + format_result)
    except Exception as e:
        label_result.config(text="Помилка у введенні")

root = tk.Tk()
root.title("Обчислення функції f")
root.geometry("400x500")

label_image = tk.Label(root)
label_image.pack()

photo = tk.PhotoImage(file="image.gif")
label_image.configure(image=photo)
label_image.image = photo  

label_a = tk.Label(root, text="Введіть значення a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Введіть значення b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Введіть значення c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()


button_calculate = tk.Button(root, text="Обчислити")
button_calculate.pack()
button_calculate.bind('<Button-1>', calculate_function)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()

