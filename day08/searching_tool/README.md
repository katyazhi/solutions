With this command-line tool you may search and download data from the [NCBI PubChem Compounds](https://pubchem.ncbi.nlm.nih.gov/docs/compounds) or [NCBI PubChem Substances](https://pubchem.ncbi.nlm.nih.gov/docs/substances) database.

## Installation
Download files from searching_tool folder of this repository to your computer and install required Python packages with the command:

`pip install -r requirements.txt`

## Usage
To use the programm run the following command:

`python PubChem_download.py`

and fill the boxes with following information:

TERM is a name/part of a name of the chemical(s) of your interest OR molecular formula. 
NUMBER is a maximum number of compound profiles to download.

You also can choose a format of downloading data (txt or csv) and the datatbase to search within (PubChem Substances or PubChem Compounds). 

## Output
The programm saves information about each compound in a separate file containing full name of compound, molecular formula, molecular weight and the CID - identificational number in PubChem database. Each file is named with the CID number of compound.

Search information (date and time of the search, item, maximum number of items to download and total number of items of the search) is automatically saved and updated in a csv file called search_journal.csv
