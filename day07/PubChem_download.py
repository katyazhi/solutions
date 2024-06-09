import sys
from Bio import Entrez
from datetime import datetime
import csv
import os
Entrez.email = "ekaterina.zhigileva@gmail.com"


def compound_search(term, number):
    search = Entrez.esearch(db="pccompound", term=term, retmax=number, sort="CID")
    records = Entrez.read(search)
    search.close()
    return records

def data_downloader(records):   
    for Id in records["IdList"]:
        handle = Entrez.efetch(db="pccompound", id=Id, rettype="text", retmode="text")
        data = handle.read()
        filename = data.partition('CID: ')[2].partition('\n')[0]
        with open(filename,'w') as fh:
            fh.write(f"{data}")
        print(filename)
        handle.close()

def search_journal(term, number, total):
    file_exists = os.path.isfile('search_journal.csv')
    with open('search_journal.csv', 'a', newline='') as fh:
        fieldnames = ['date', 'term', 'max', 'total']
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'term': term, 'max': number, 'total': total})


def main():
    if len(sys.argv) !=3:
        exit("Usage: {sys.argv[0]} TERM NUMBER")
    term = sys.argv[1]
    number = sys.argv[2]
    records = compound_search(term, number)
    data_downloader(records)
    search_journal(term, number, records['Count'])

main()