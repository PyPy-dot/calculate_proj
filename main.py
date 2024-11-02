import tkinter as tk


def is_valid_data():
    return entry1.get().isdigit() and entry2.get().isdigit()


def mul_func() -> None:
    entry3.delete(0, tk.END)
    if is_valid_data():
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        entry3.insert(0, str(num1 * num2))
    else:
        entry3.insert(0, 'Некорректные данные!')


def mul_sub() -> None:
    entry3.delete(0, tk.END)
    if is_valid_data():
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        entry3.insert(0, str(num1 - num2))
    else:
        entry3.insert(0, 'Некорректные данные!')


def mul_add() -> None:
    entry3.delete(0, tk.END)
    if is_valid_data():
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        entry3.insert(0, str(num1 + num2))
    else:
        entry3.insert(0, 'Некорректные данные!')


def mul_div() -> None:
    entry3.delete(0, tk.END)
    if is_valid_data():
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        if num2:
            entry3.insert(0, str(num1 / num2))
        else:
            entry3.insert(0, 'На ноль делить нельзя!')
    else:
        entry3.insert(0, 'Некорректные данные!')


root = tk.Tk()
root.geometry('350x350')
root.resizable(False, False)

label1 = tk.Label(root, text='Введите первое число')
entry1 = tk.Entry(root, width=20)
label2 = tk.Label(root, text='Введите второе число')
entry2 = tk.Entry(root, width=20)
button_mul = tk.Button(root, text='*', width=2, height=1, command=mul_func)
button_sub = tk.Button(root, text='-', width=2, height=1, command=mul_sub)
button_add = tk.Button(root, text='+', width=2, height=1, command=mul_add)
button_div = tk.Button(root, text='/', width=2, height=1, command=mul_div)
label3 = tk.Label(root, text='Ответ:')
entry3 = tk.Entry(root, width=40)

label1.place(x=30, y=50)
entry1.place(x=30, y=80)
label2.place(x=200, y=50)
entry2.place(x=200, y=80)
button_mul.place(x=60, y=150)
button_sub.place(x=130, y=150)
button_add.place(x=200, y=150)
button_div.place(x=270, y=150)
label3.place(x=30, y=250)
entry3.place(x=80, y=250)

root.mainloop()
