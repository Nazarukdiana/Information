import tkinter as tk
from math import sin

def calculate_function(event=None):
    try:
        x = float(entry_x.get())
        total = 0
        for k in range(2, 7):
            numerator = sin(0.17 * (x ** k))
            denominator = 2 * k + x
            total += numerator / denominator

        format_result = "{:.2f}".format(total)
        label_result.config(text="Результат: " + format_result)
    except Exception as e:
        label_result.config(text="Помилка у введенні")

root = tk.Tk()
root.title("Обчислення суми")
root.geometry("400x450")

label_image = tk.Label(root)
label_image.pack()
photo = tk.PhotoImage(file="image.png")  
label_image.configure(image=photo)
label_image.image = photo

label_x = tk.Label(root, text="Введіть значення x:")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

button_calculate = tk.Button(root, text="Обчислити")
button_calculate.pack()
button_calculate.bind('<Button-1>', calculate_function)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
