import tkinter as tk


class SearchBar:

    def __init__(self, parent):

        frame = tk.Frame(parent)

        frame.pack(fill="x", padx=15, pady=5)

        tk.Label(
            frame,
            text="🔍 Search :"
        ).pack(side="left")

        self.entry = tk.Entry(
            frame,
            width=40
        )

        self.entry.pack(
            side="left",
            padx=5
        )

    def bind(self, callback):

        self.entry.bind("<KeyRelease>", callback)

    def text(self):

        return self.entry.get()