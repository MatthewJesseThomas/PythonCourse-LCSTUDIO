import tkinter as tk
from tkinter import simpledialog
from dna_sequence import GeneSequenceComparer  # Import from the correct module

class DNASEQUENCEGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("DNA Mutation Analyzer")

        self.seq1 = ""
        self.seq2 = ""

        self.label_seq1 = tk.Label(self.window, text="Enter DNA sequence1:")
        self.label_seq1.pack()

        self.entry_seq1 = tk.Entry(self.window)
        self.entry_seq1.pack()

        self.button_seq1 = tk.Button(self.window, text="Submit", command=self.get_seq1)
        self.button_seq1.pack()

        self.window.mainloop()

    def get_seq1(self):
        self.seq1 = self.entry_seq1.get()
        self.label_seq1.destroy()
        self.entry_seq1.destroy()
        self.button_seq1.destroy()

        self.label_seq2 = tk.Label(self.window, text="Enter DNA sequence2:")
        self.label_seq2.pack()

        self.entry_seq2 = tk.Entry(self.window)
        self.entry_seq2.pack()

        self.button_seq2 = tk.Button(self.window, text="Submit", command=self.get_seq2)
        self.button_seq2.pack()

    def get_seq2(self):
        self.seq2 = self.entry_seq2.get()
        self.label_seq2.destroy()
        self.entry_seq2.destroy()
        self.button_seq2.destroy()

        self.compare_sequences()

    def compare_sequences(self):
        comparer = GeneSequenceComparer(self.seq1, self.seq2)
        results = comparer.compare_sequences()

        # Display the comparison results in a text widget
        text_widget = tk.Text(self.window, height=10, width=50)
        text_widget.insert("end", results)
        text_widget.pack()

if __name__ == "__main__":
    dna_gui = DNASEQUENCEGUI()
