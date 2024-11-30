import re

# Define structures for keywords and operators
keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
    "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
]

operators = ["*", "+", "=", "-", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=", "&&", "||"]

special_symbols = ['#', '(', ')', '{', '}', '[', ']', ';', ':', ',', '"', "'"]

# Define a list to store the output
output = []

def classify_token(token):
    """Classifies a given token into one of the predefined types."""
    # Check if the token is a keyword
    if token in keywords:
        return "Keyword"

    # Check if the token is an operator
    if token in operators:
        return "Operator"

    # Check if the token is a constant
    if re.fullmatch(r'\d+', token):  # Match integers
        return "Constant"

    # Check if the token is a special symbol
    if token in special_symbols:
        return "Special Symbol"

    # Default classification is an identifier
    return "Identifier"

def process_file(file_path):
    """Processes the given file and generates the classification output."""
    try:
        with open(file_path, "r") as file:
            serial_number = 1
            for line in file:
                # Tokenize using regex: matches keywords, identifiers, operators, and symbols
                tokens = re.findall(r'[a-zA-Z_]\w*|\d+|==|!=|>=|<=|&&|\|\||[+\-*/%=;:(){}[\],#<>"]', line)
                for token in tokens:
                    token_type = classify_token(token)
                    output.append({
                        "sr": serial_number,
                        "name": token,
                        "type": token_type
                    })
                    serial_number += 1
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_output():
    """Displays the output in a tabular form."""
    print(f"{'Sr.No.':<10}{'Name':<20}{'Type':<20}")
    print("=" * 50)
    for entry in output:
        print(f"{entry['sr']:<10}{entry['name']:<20}{entry['type']:<20}")

if __name__ == "__main__":
    file_path = "input1.c"  # Change this to your input file's path
    process_file(file_path)
    display_output()
