With this command-line tool you may search and downloads data from the NCBI PubChem Compounds database, which contains information about chemicals.

Installation
Download files from day07 folder of this repository to your computer and install required Python packages with the command:

pip install -r requirements.txt

Usage
To use the programm run the following command:

python PubChem_download.py TERM NUMBER

where:
TERM is a name/part of a name of the chemical(s) of your interest OR molecular formula. 
NUMBER is a maximum number of compound profiles to download.

Examples:
python PubChem_download.py C5H10 4 
python PubChem_download.py aspirine 2
python PubChem_download.py 2-aminoethanol 4

The programm saves information about each compound in a separate txt file containing full name of compound, molecular formula, molecular weight and the CID - identificational number in PubChem database. Each file is named with the CID number of compound, and the programm displays names of saved files while running. 

Search information (date and time of the search, item, maximum number of items to download and total number of items of the search) is automatically saved and updated in a csv file called search_journal.csv
