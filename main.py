import tkinter as tk


class Calculate:
    def __new__(cls):
        _instance = None
        if _instance is None:
            _instance = super().__new__(cls)
        return _instance

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.label1 = tk.Label(self.root, text='Введите первое число')
        self.entry1 = tk.Entry(self.root, width=20)
        self.label2 = tk.Label(self.root, text='Введите второе число')
        self.entry2 = tk.Entry(self.root, width=20)
        self.button_mul = tk.Button(self.root, text='*', width=2, height=1, command=self._mul)
        self.button_sub = tk.Button(self.root, text='-', width=2, height=1, command=self._sub)
        self.button_add = tk.Button(self.root, text='+', width=2, height=1, command=self._add)
        self.button_div = tk.Button(self.root, text='/', width=2, height=1, command=self._div)
        self.label3 = tk.Label(self.root, text='Ответ:')
        self.entry3 = tk.Entry(self.root, width=40)

    def _window(self) -> None:
        self.root.geometry('350x350')
        self.root.resizable(False, False)
        self.label1.place(x=30, y=50)
        self.entry1.place(x=30, y=80)
        self.label2.place(x=200, y=50)
        self.entry2.place(x=200, y=80)
        self.button_mul.place(x=60, y=150)
        self.button_sub.place(x=130, y=150)
        self.button_add.place(x=200, y=150)
        self.button_div.place(x=270, y=150)
        self.label3.place(x=30, y=250)
        self.entry3.place(x=80, y=250)

    def get_values(self):
        return int(self.entry1.get()), int(self.entry2.get())

    def _mul(self) -> None:
        self.entry3.delete(0, tk.END)
        try:
            num1, num2 = self.get_values()
            result = num1 * num2
            self.entry3.insert(tk.END, str(result))
        except ValueError:
            self.entry3.insert(0, 'Некорректные данные!')

    def _sub(self) -> None:
        self.entry3.delete(0, tk.END)
        try:
            num1, num2 = self.get_values()
            result = num1 - num2
            self.entry3.insert(tk.END, str(result))
        except ValueError:
            self.entry3.insert(0, 'Некорректные данные!')

    def _add(self) -> None:
        self.entry3.delete(0, tk.END)
        try:
            num1, num2 = self.get_values()
            result = num1 + num2
            self.entry3.insert(tk.END, str(result))
        except ValueError:
            self.entry3.insert(0, 'Некорректные данные!')

    def _div(self) -> None:
        self.entry3.delete(0, tk.END)
        try:
            num1, num2 = self.get_values()
            try:
                result = num1 / num2
                self.entry3.insert(0, str(result))
            except ZeroDivisionError:
                self.entry3.insert(0, 'На ноль делить нельзя!')
        except ValueError:
            self.entry3.insert(0, 'Некорректные данные!')

    def start(self) -> None:
        self._window()
        self.root.mainloop()


if __name__ == '__main__':
    Calculate().start()
