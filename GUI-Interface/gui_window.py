import tkinter as tk
import tkinter.font as tkfont

window = tk.Tk()

window.geometry("800x500")
window.title("Hellvitivca")

# Provide the absolute path to the font file
font_path = "C:/path/to/vermin-vibes-v-font/VerminVibesV-Zlg3.ttf"  # Replace with the actual absolute path to the font file

# Load the font
custom_font = tkfont.Font(family="Vermin-Vibes-V-Zlg3", size=26)

# Apply the custom font to the label
label = tk.Label(window, text="Salve in Nostrum Mundo", font=(custom_font, 26))
label.pack()

window.mainloop()

