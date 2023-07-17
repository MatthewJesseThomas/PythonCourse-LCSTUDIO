import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox


class TodoListApp:

    def __init__(self):
        self.gui_window = tk.Tk()
        self.gui_window.geometry("800x600")
        self.gui_window.title("Todo List")

        self.font_families = tkfont.families()
        self.selected_font = "Helvetica"

        self.menubar = tk.Menu(self.gui_window)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.gui_window.config(menu=self.menubar)

        self.label = tk.Label(self.gui_window, text="Todo List", font=(self.selected_font, 36))
        self.label.pack(pady=(20, 40))

        self.todo_listbox = tk.Listbox(self.gui_window, height=10, font=(self.selected_font, 20))
        self.todo_listbox.pack(padx=10, pady=10)
        self.todo_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.search_entry = tk.Entry(self.gui_window, font=(self.selected_font, 20))
        self.search_entry.pack(padx=10, pady=10)

        self.search_button = tk.Button(self.gui_window, text="Search", font=(self.selected_font, 20),
                                       command=self.search_todo)
        self.search_button.pack(padx=10, pady=10)

        self.todo_items = []

        self.add_entry = tk.Entry(self.gui_window, font=(self.selected_font, 20))
        self.add_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.gui_window, text="Add Task", font=(self.selected_font, 20),
                                    command=self.add_todo_item)
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.gui_window, text="Update Task", font=(self.selected_font, 20),
                                       command=self.update_todo_item, state=tk.DISABLED)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.gui_window, text="Delete Task", font=(self.selected_font, 20),
                                       command=self.delete_todo_item, state=tk.DISABLED)
        self.delete_button.pack(padx=10, pady=10)

        self.gui_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.gui_window.mainloop()

    def show_message(self):
        messagebox.showinfo(title="Message", message="This is a sample message.")

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.gui_window.destroy()

    def search_todo(self):
        search_text = self.search_entry.get().strip().lower()
        self.todo_listbox.selection_clear(0, tk.END)
        self.update_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)

        if not search_text:
            messagebox.showinfo(title="Search Result", message="Please enter a search text.")
            return

        matching_indices = [
            index
            for index, item in enumerate(self.todo_items)
            if search_text in item.lower()
        ]

        if matching_indices:
            messagebox.showinfo(title="Search Result", message="Search text found in the Todo list!")
            self.todo_listbox.selection_set(matching_indices[0])
            self.todo_listbox.yview(matching_indices[0])
            self.update_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo(title="Search Result", message="Search text not found in the Todo list.")

    def add_todo_item(self):
        item_text = self.add_entry.get().strip()
        if item_text:
            self.todo_items.append(item_text)
            self.update_todo_list()

    def update_todo_item(self):
        selected_index = self.todo_listbox.curselection()[0]
        new_item_text = self.add_entry.get().strip()
        if new_item_text:
            self.todo_items[selected_index] = new_item_text
            self.update_todo_list()

    def delete_todo_item(self):
        selected_index = self.todo_listbox.curselection()[0]
        del self.todo_items[selected_index]
        self.update_todo_list()

    def update_todo_list(self):
        self.todo_listbox.delete(0, tk.END)
        for item in self.todo_items:
            self.todo_listbox.insert(tk.END, item)

    def on_select(self, event):
        selected_index = self.todo_listbox.curselection()
        if selected_index:
            self.add_entry.delete(0, tk.END)
            self.add_entry.insert(tk.END, self.todo_items[selected_index[0]])
            self.update_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.update_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)
            self.add_entry.delete(0, tk.END)


if __name__ == "__main__":
    TodoListApp()
