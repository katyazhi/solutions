import tkinter as tk
from tkinter import messagebox
from Bio import Entrez
from datetime import datetime
import csv
import os

Entrez.email = "ekaterina.zhigileva@gmail.com"

def compound_search(term, number, db):
    search = Entrez.esearch(db=db, term=term, retmax=int(number), sort="relevance")
    records = Entrez.read(search)
    search.close()
    return records

def data_downloader(records, format, db):
    for Id in records["IdList"]:
        handle = Entrez.efetch(db=db, id=Id, rettype=format, retmode="text")
        data = handle.read()
        filename = f"{Id}.{format}"
        with open(filename, 'w') as fh:
            fh.write(data)
        handle.close()
    messagebox.showinfo("Download Complete", "Data download complete.")

def search_journal(term, number, total):
    file_exists = os.path.isfile('search_journal.csv')
    with open('search_journal.csv', 'a', newline='') as fh:
        fieldnames = ['date', 'term', 'max', 'total']
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'term': term, 'max': number, 'total': total})

def download_data():
    term = search_term_entry.get()
    number = number_entry.get()
    db = database_selector.get()
    format = format_selector.get()

    if not term or not number:
        messagebox.showerror("Error", "Please enter search term and number.")
        return
    
    try:
        records = compound_search(term, number, db)
        data_downloader(records, format, db)
        search_journal(term, number, records['Count'])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
app = tk.Tk()
app.title("PubChem Data Downloader")


tk.Label(app, text="Search Term:").grid(row=0, column=0, sticky="w")
search_term_entry = tk.Entry(app, width=50)
search_term_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Number of Records to Download:").grid(row=1, column=0, sticky="w")
number_entry = tk.Entry(app, width=10)
number_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Select Database:").grid(row=2, column=0, sticky="w")
database_options = ["pcsubstance", "pccompound"]
database_selector = tk.StringVar(app)
database_selector.set(database_options[0])  
db_dropdown = tk.OptionMenu(app, database_selector, *database_options)
db_dropdown.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Select File Format:").grid(row=3, column=0, sticky="w")
format_options = ["txt", "csv"]
format_selector = tk.StringVar(app)
format_selector.set(format_options[0])  
format_dropdown = tk.OptionMenu(app, format_selector, *format_options)
format_dropdown.grid(row=3, column=1, padx=10, pady=5)

download_button = tk.Button(app, text="Download Data", command=download_data)
download_button.grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()