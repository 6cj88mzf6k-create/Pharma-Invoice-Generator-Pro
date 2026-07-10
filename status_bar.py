import tkinter as tk


class StatusBar:

    def __init__(self, parent):

        self.status = tk.StringVar()

        self.status.set("Ready")

        self.label = tk.Label(
            parent,
            textvariable=self.status,
            anchor="w",
            bg="#e9ecef",
            relief="sunken",
            padx=10
        )

        self.label.pack(
            side="bottom",
            fill="x"
        )

    def set(self, text):

        self.status.set(text)