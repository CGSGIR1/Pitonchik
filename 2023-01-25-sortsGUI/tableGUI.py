# Илья Родин 11.01.2023

from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
import random 
import time
from fills import *
import tkinter as tk 
import tkinter.ttk as ttk
import re

n = 10 ** 5
sorts = [(bubble_sort, "bubble"), (insertion_sort, "insertion"), (selection_sort, "selection"),
        (heap_sort, "heap"), (quick_sort, "quick"), (merge_sort, "merge")]
fills = [(fill_increase, "increase"), (fill_decrease, "decrease"),
         (fill_random, "random"), (fill_almostsort, "almostsort")]


class ArrayControl(tk.Text):
    def __init__(self, *args, **kwargs):
        # Передаём в параметры всё, что дали на вход
        super().__init__(*args, **kwargs)

        # Заполняем текстовый контрол через метод базового класса tk.Text
        self.insert("1.0", "3, 1, 2")

    def get_list(self):
        # Получаем текст из базового класса tk.Text
        text = self.get("1.0", tk.END)

        # Заменяем все "плохие" символы на пробелы
        text = re.sub(r"[^0-9]", " ", text)

        # Строим список по строке
        return list(map(int, text.split()))

    def set_list(self, array):
        # Удаляем старый текст и вставляем новый
        self.delete("1.0", tk.END)
        self.insert("1.0", ", ".join(map(str, array)))


class Window(tk.Tk):
    PAD = 10
    
    def __init__(self):
        super().__init__()
        # Define the size of window or frame
        self.geometry("800x600")
        
        self.defaultFont = tk.font.nametofont("TkDefaultFont")
        self.defaultFont.configure( family = "Comic Sans MS", 
                                     size = 15, 
                                     weight = "bold")
        topFrame = tk.Frame(self)
        topFrame.pack(side = tk.TOP)
        
        ttk.Label(topFrame, text="Number of elements:").pack()
        
        self.spinbox = ttk.Spinbox(topFrame, from_=1.0, to=100.0, command = self.lang_changed)
        
        self.spinbox.pack()
        
        # Set the StringVar associated with tk.OptionMenu
        self.menu = tk.StringVar()
        self.menu.set("Select Any Language")
        self.menu.trace("w", self.lang_changed)
        
        ttk.Label(text="Fill:").pack()
        self.cmb = ttk.Combobox(self, values=["increase", "decrease", "random", "almostsort"], state="readonly")
        self.cmb.bind("<<ComboboxSelected>>", self.fill_changed)
        self.cmb.pack()
        # Alternative: Combobox control from ttk
        
        # Alternative: Combobox control from ttk
        ttk.Label(text="Sorts:").pack() 
        #selected = tk.StringVar()
        self.cmb1 = ttk.Combobox(self, values=["bubble", "insertion", "selection", "heap", "quick", "merge"], state="readonly")
        self.cmb1.bind("<<ComboboxSelected>>", self.sort_changed)
        self.cmb1.pack()
        button = tk.Button(self, width=9, text="Fills")
        button.config(command = self.pressed_Fills)
        button.pack(side=tk.RIGHT)
        button1 = tk.Button(self, width=9, text="Sorts")
        button1.config(command = self.pressed_Sorts)
        button1.pack(side=tk.RIGHT)
        # Добавляем ArrayControl отнаследованный от tk.Text
        self.array = ArrayControl(self, width=10, height=10)
        # self.array.insert(0, "Hi")
        self.array.pack(anchor=tk.NW, fill=tk.BOTH, expand=1, padx=self.PAD, pady=self.PAD)
        self.fill = 0
        self.sort = 0
        self.num = 0


    def lang_changed(self, *args):
        option = self.spinbox.get()
        self.num = option
        print(f"changed on {option}")

    def fill_changed(self, event):
        option = self.cmb.get()
        index = self.cmb.current()
        self.fill = index
        print(f"changed on {option} index = {index}")
        
    def sort_changed(self, event):
        option = self.cmb1.get()
        index = self.cmb1.current()
        self.sort = index
        print(f"changed on {option} index = {index}")
    
    def pressed_Fills(self):
        if self.fill == 0:
            self.array.set_list(fill_increase(int(self.num)))
        elif self.fill == 1:
            self.array.set_list(fill_decrease(int(self.num)))
        elif self.fill == 2:
            self.array.set_list(fill_random(int(self.num)))
        elif self.fill == 3:
            self.array.set_list(fill_almostsort(int(self.num)))
        print(1)

    def pressed_Sorts(self):
        a = self.array.get_list()
        if self.sort == 0:
            self.array.set_list(bubble_sort(a))
        elif self.sort == 1:
            self.array.set_list(insertion_sort(a))
        elif self.sort == 2:
            self.array.set_list(selection_sort(a))
        elif self.sort == 3:
            self.array.set_list(heap_sort(a))
        elif self.sort == 4:
            self.array.set_list(quick_sort(a))
        elif self.sort == 5:
            self.array.set_list(merge_sort(a))
        print(2)
    

if __name__ == '__main__':
    # Create an instance of tkinter frame
    win = Window()
    win.mainloop()
