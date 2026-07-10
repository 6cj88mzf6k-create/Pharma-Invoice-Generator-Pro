import tkinter as tk
from tkinter import ttk

class TableView:

    def __init__(self, parent):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except:
            pass
        style.configure("Treeview", font=("Segoe UI",11), rowheight=34, borderwidth=0)
        style.configure("Treeview.Heading", font=("Segoe UI",11,"bold"), background="#0B5394", foreground="white", relief="flat")
        style.map("Treeview", background=[("selected","#1976D2")], foreground=[("selected","white")])

        container = tk.Frame(parent,bg="#f5f5f5")
        container.pack(fill="both", expand=True, padx=15, pady=10)

        self.tree = ttk.Treeview(container, show="headings")
        vsb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0,column=0,sticky="nsew")
        vsb.grid(row=0,column=1,sticky="ns")
        hsb.grid(row=1,column=0,sticky="ew")

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

    def load_dataframe(self, df):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"]="headings"


        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, minwidth=120, anchor="w", stretch=True)

        for i,(_,row) in enumerate(df.iterrows()):
            tag="even" if i%2==0 else "odd"
            self.tree.insert("", "end", values=list(row), tags=(tag,))

        self.tree.tag_configure("even", background="#FFFFFF")
        self.tree.tag_configure("odd", background="#F3F6FA")
