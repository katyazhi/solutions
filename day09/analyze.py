import re
import argparse
from Bio import SeqIO

def find_longest_repeated_subsequence(sequence):
    length = 1
    longest_subsequence = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        m = re.search(regex, sequence)
        if m:
            longest_subsequence = m.group(1)
            length += 1
        else:
            break
    return longest_subsequence

def count_repeated_A(sequence):
    matches = re.findall(r'(A+)', sequence)
    longest_A = max(matches, key=len, default="")
    return len(longest_A)

def main():
    parser = argparse.ArgumentParser(description='Analyzing Fasta or GeneBank files')
    parser.add_argument('file', help="Path to FASTA/GeneBank file")
    parser.add_argument('--duplicate', action='store_true', help='Find the longest repeated sub-sequence')
    parser.add_argument('--repeated_A', action='store_true', help='Find the number of repeated A')
    args = parser.parse_args()

    if args.file.endswith(".gb") or args.file.endswith(".gbk"):
        format = "genbank"
    elif args.file.endswith(".fasta") or args.file.endswith(".fa"):
        format = "fasta"

    for sequence in SeqIO.parse(args.file, format):
        sequence = str(sequence.seq)
        if args.duplicate:
            longest_subsequence = find_longest_repeated_subsequence(sequence)
            print("Longest repeated sub-sequence:", longest_subsequence)

        if args.repeated_A:
            a_count = count_repeated_A(sequence)
            print("Number of repeated A:", a_count)

if __name__ == "__main__":
    main()