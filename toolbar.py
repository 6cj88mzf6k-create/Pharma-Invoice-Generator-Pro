import tkinter as tk


class ToolBar:

    def __init__(self, parent):

        self.frame = tk.Frame(
            parent,
            bg="#f5f5f5",
            height=60
        )
        self.frame.pack(fill="x", padx=12, pady=8)

        button_style = {
            "font": ("Segoe UI", 10, "bold"),
            "bd": 0,
            "relief": "flat",
            "cursor": "hand2",
            "height": 2
        }

        # ===============================
        # Import Excel
        # ===============================
        self.import_btn = tk.Button(
            self.frame,
            text="📂  Import Excel",
            bg="#1976D2",
            fg="white",
            activebackground="#1565C0",
            activeforeground="white",
            width=18,
            **button_style
        )
        self.import_btn.pack(side="left", padx=5)

        # ===============================
        # Generate
        # ===============================
        self.generate_btn = tk.Button(
            self.frame,
            text="🚀  Generate",
            bg="#2E7D32",
            fg="white",
            activebackground="#1B5E20",
            activeforeground="white",
            width=18,
            **button_style
        )
        self.generate_btn.pack(side="left", padx=5)

        # ===============================
        # Word
        # ===============================
        self.word_btn = tk.Button(
            self.frame,
            text="📄 Word",
            width=12,
            state="disabled",
            **button_style
        )
        self.word_btn.pack(side="left", padx=5)

        # ===============================
        # PDF
        # ===============================
        self.pdf_btn = tk.Button(
            self.frame,
            text="📕 PDF",
            width=12,
            state="disabled",
            **button_style
        )
        self.pdf_btn.pack(side="left", padx=5)

        # ===============================
        # Excel
        # ===============================
        self.excel_btn = tk.Button(
            self.frame,
            text="📊 Excel",
            width=12,
            state="disabled",
            **button_style
        )
        self.excel_btn.pack(side="left", padx=5)

        # ===============================
        # Print
        # ===============================
        self.print_btn = tk.Button(
            self.frame,
            text="🖨 Print All",
            bg="#EF6C00",
            fg="white",
            activebackground="#E65100",
            activeforeground="white",
            width=15,
            **button_style
        )
        self.print_btn.pack(side="left", padx=5)

    # ---------------------------------
    # Commands
    # ---------------------------------

    def set_import_command(self, command):
        self.import_btn.config(command=command)

    def set_generate_command(self, command):
        self.generate_btn.config(command=command)

    def set_word_command(self, command):
        self.word_btn.config(command=command)

    def set_pdf_command(self, command):
        self.pdf_btn.config(command=command)

    def set_excel_command(self, command):
        self.excel_btn.config(command=command)

    def set_print_command(self, command):
        self.print_btn.config(command=command)

    # ---------------------------------
    # Enable Export Buttons
    # ---------------------------------

    def enable_export_buttons(self):
        self.word_btn.config(state="normal")
        self.pdf_btn.config(state="normal")
        self.excel_btn.config(state="normal")

    def disable_export_buttons(self):
        self.word_btn.config(state="disabled")
        self.pdf_btn.config(state="disabled")
        self.excel_btn.config(state="disabled")