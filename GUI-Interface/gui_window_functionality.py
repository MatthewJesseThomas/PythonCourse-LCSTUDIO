import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.gui_window = tk.Tk()
        self.gui_window.geometry("800x600")
        self.gui_window.title("Testing Grounds - GUI")

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
        
        self.label = tk.Label(self.gui_window, text="Welcome To My Testing Grounds", font=(self.selected_font, 36))
        self.label.pack()

        self.label = tk.Label(self.gui_window, text="Your Message", font=(self.selected_font, 32))
        self.label.pack(pady=(20, 40))

        self.textbox = tk.Text(self.gui_window, height=5, font=(self.selected_font, 30))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.gui_window, text="Show MessageBox", font=(self.selected_font, 28), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.gui_window, text="Show Message", font=(self.selected_font, 28), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.gui_window, text="Clear", font=(self.selected_font, 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.gui_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.gui_window.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
            
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you Really want to Quit?"):  # Confirm to Close Application
            self.gui_window.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        
if __name__ == "__main__":
    MyGUI()
