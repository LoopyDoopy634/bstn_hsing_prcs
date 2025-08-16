import csv

def add_header_if_missing(filename, header):
    
    try:
        with open(filename, 'r') as f:
            first_line = f.readline().strip()
            
            try:
                float(first_line.split()[0])
                has_header = False
            except (ValueError, IndexError):
                has_header = True
        
        if not has_header:
            print(f"'{filename}' is  missing a header. Adding one now...")
            
            with open(filename, 'r') as f:
                original_content = f.read()
                
            with open(filename, 'w') as f:
                f.write(' '.join(header) + '\n')
                f.write(original_content)
        
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