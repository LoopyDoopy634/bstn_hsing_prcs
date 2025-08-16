import csv

def add_header_if_missing(filename, header):
    
    try:
        with open(filename, 'r') as f:
            first_line = f.readline().strip()   #Read the first line of the csv file
            
            #If the first line has a numerical value then converting to float is fine.
            #If the first line has a text value then converting to float leads to error.
            
            try:
                float(first_line.split()[0])   #Take the first character from the current header and convert it into float.
                has_header = False   #Set a boolean to check if headers are there or not.
            except (ValueError, IndexError):   #Wrong conversion will give error.
                has_header = True
        
        if not has_header:
            print(f"'{filename}' is  missing a header. Adding one now...")
            
            with open(filename, 'r') as f:
                original_content = f.read()   #Read the entire contents of the current csv file.
                
            with open(filename, 'w') as f:
                f.write(' '.join(header) + '\n')   #Add the headings first.
                f.write(original_content)   #After the headings, add the rest of the dataset.
        
        else:
            print(f"'{filename}' already has a header. No changes were made.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        

if __name__ == "__main__":
    CSV_FILE = "dataset/housing.csv"
    COLUMN_NAMES = [
        'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
    ]
    add_header_if_missing(CSV_FILE, COLUMN_NAMES)