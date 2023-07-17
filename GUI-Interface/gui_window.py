import tkinter as tk
import tkinter.font as tkfont

# GUI window - Init
window = tk.Tk()  # To init the Window

window.geometry("800x500")
window.title("Hellvitivca") # To init and print the Title

# Get the available font families
font_families = tkfont.families() # To init Font

# Choose a font from the available families
chosen_font = "Comic Sans MS"

# Apply the chosen font to the label
label = tk.Label(window, text="Salve in Nostrum Mundo", font=(chosen_font, 18), relief=tk.SOLID, borderwidth=1)
label.pack(padx=20, pady=20)

# # For User Inputs the tk.Text is a Multi line Box for Inputs
# text_box = tk.Text(window, height=8, font=(chosen_font, 18), relief=tk.SOLID, borderwidth=1)
# text_box.pack()  # To init the component

# Buttons Components
button_frame = tk.Frame(window)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(button_frame, text="1", font=(chosen_font, 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(button_frame, text="2", font=(chosen_font, 18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(button_frame, text="3", font=(chosen_font, 18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(button_frame, text="4", font=(chosen_font, 18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(button_frame, text="5", font=(chosen_font, 18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(button_frame, text="6", font=(chosen_font, 18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

button_frame.pack(fill='x')

# Create another button with custom styling
# anotherbtn = tk.Button(window, text="Test", font=(chosen_font, 18))
# anotherbtn.place(x=400, y=300, height=100, width=100)

# # For Passwords the tk.Entry is a Single line Box for passwords or statements
# text_entry = tk.Entry(window, font=(chosen_font, 18))
# text_entry.pack(pady=20)
# text_entry.pack()  # To init the component

# # Button tk.Button to create a Button
# button = tk.Button(window, text="Submit", font=(chosen_font, 20), borderwidth=2)
# button.pack() #To init the component

window.mainloop()  # To init and Display the Window
