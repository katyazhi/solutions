import sys
from conductivity_fun import custom_factor, excel_work, input_values

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]
    thickness, diameter = input_values()
    factor = custom_factor(thickness, diameter)
    excel_work(filename, factor)
    
main()
