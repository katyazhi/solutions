With this programm you can analyze DNA sequences in FASTA or GeneBank formats. The functionalities of this programm include:
1. finding the longest duplicated subsequence.
2. finding the length of the longest subsequence of repeated А.

## Installation
Download files from day09 folder of this repository to your computer and install required Python packages with the command:

`pip install -r requirements.txt`

## Usage
To use the programm run the following command:

`python analyze.py [-h] file [--duplicate] [--repeated_A]`

where:

positional arguments:
file          Path to FASTA/GeneBank file

options:
-h, --help    show this help message and exit
--duplicate   Find the longest repeated sub-sequence
--repeated_A  Find the number of repeated A
