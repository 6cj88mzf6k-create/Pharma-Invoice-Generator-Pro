
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

from modules.excel_reader import ExcelReader
from modules.invoice_generator import InvoiceGenerator
from modules.pdf_exporter import PdfExporter

from ui.toolbar import ToolBar
from ui.table_view import TableView
from ui.search_bar import SearchBar
from ui.status_bar import StatusBar


class MainWindow:

    def __init__(self):
        self.reader = ExcelReader()
        self.generator = InvoiceGenerator()

        self.window = tk.Tk()
        self.window.title("Pharma Invoice Generator Pro")
        self.window.geometry("1450x900")
        self.window.minsize(1200,700)
        self.window.configure(bg="#eef2f7")
        try:
            self.window.iconbitmap("app.ico")
        except Exception:
            pass

        sw=self.window.winfo_screenwidth()
        sh=self.window.winfo_screenheight()
        w,h=1450,900
        self.window.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        tk.Label(self.window,text="Pharma Invoice Generator Pro",
                 font=("Segoe UI",28,"bold"),
                 fg="#1565C0",bg="#eef2f7").pack(pady=(15,8))

        self.toolbar=ToolBar(self.window)
        self.toolbar.set_import_command(self.import_excel)
        self.toolbar.set_generate_command(self.generate_invoices)

        info=tk.Frame(self.window,bg="white",bd=1,relief="solid")
        info.pack(fill="x",padx=15,pady=(6,6))

        self.file_label=tk.Label(info,text="📄 File : -",font=("Segoe UI",10,"bold"),bg="white")
        self.file_label.pack(side="left",padx=15,pady=8)

        self.items_label=tk.Label(info,text="📦 Items : 0",font=("Segoe UI",10,"bold"),bg="white")
        self.items_label.pack(side="left",padx=15)

        self.inv_label=tk.Label(info,text="🧾 Invoices : 0",font=("Segoe UI",10,"bold"),bg="white")
        self.inv_label.pack(side="left",padx=15)

        self.ready=tk.Label(info,text="🟢 Ready",font=("Segoe UI",10,"bold"),fg="#2E7D32",bg="white")
        self.ready.pack(side="right",padx=15)

        self.search=SearchBar(self.window)
        self.table=TableView(self.window)

        self.status=StatusBar(self.window)
        self.status.set("Ready")

    def import_excel(self):
        file=filedialog.askopenfilename(title="Select Excel File",
                                        filetypes=[("Excel Files","*.xlsx *.xls")])
        if not file:
            return
        try:
            self.reader.load(file)
            self.file_label.config(text=f"📄 File : {os.path.basename(file)}")
            self.items_label.config(text=f"📦 Items : {self.reader.get_rows_count()}")
            self.table.load_dataframe(self.reader.data)
            self.toolbar.enable_export_buttons()
            self.status.set(f"Loaded {self.reader.get_rows_count()} rows")
            messagebox.showinfo("Success","Excel imported successfully.")
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def generate_invoices(self):
        if self.reader.data is None:
            messagebox.showwarning("Warning","Please import Excel first.")
            return
        count=simpledialog.askinteger("Generate Invoices","Enter number of invoices:",
                                      minvalue=1,maxvalue=500)
        if not count:
            return
        invoices=self.generator.generate(self.reader.data,count)
        folder=self.generator.export_excel()
        self.inv_label.config(text=f"🧾 Invoices : {len(invoices)}")
        messagebox.showinfo("Success",
                            f"{len(invoices)} invoice files created successfully.\n\nFiles saved inside OUTPUT folder.")
        if messagebox.askyesno("Print","Do you want to print all invoices now?"):
            for f in sorted(os.listdir(folder)):
                if f.endswith(".xlsx"):
                    os.startfile(os.path.join(folder,f),"print")
        self.status.set(f"{len(invoices)} invoices exported.")

    def run(self):
        self.window.mainloop()
