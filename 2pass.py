# Define opcode table
opcode_table = {
    'STOP': "00",
    'ADD': "01",
    'SUB': "02",
    'MULT': "03",
    'MOVER': "04",
    'MOVEM': "05",
    'COMP': "06",
    'BC': "07",
    'DIV': "08",
    'READ': "09",
    'PRINT': "10"
}

# Symbol Table and Literal Table
symbol_table = {}
literal_table = {}
pool_table = []

# Address counter
address_counter = 0

# First Pass: Build Symbol and Literal Tables
def first_pass(assembly_code):
    global address_counter
    pool_table.append(0)  # Start first pool of literals
    for line in assembly_code:
        line = line.strip()
        print(f"Processing line (First Pass): '{line}'")  # Debugging output

        if not line or line.startswith("#"):  # Skip empty lines and comments
            continue

        if ":" in line:  # Handle labels
            parts = line.split(":", 1)
            if len(parts) == 2:  # Ensure the split resulted in two parts
                label = parts[0].strip()
                instruction = parts[1].strip()
                symbol_table[label] = address_counter
                line = instruction  # Process the instruction part
            else:
                print(f"Error: Invalid label format in line: '{line}'")
                continue

        if not line:  # Skip if no instruction remains after label processing
            continue

        parts = line.split()
        if len(parts) == 0:  # Check for empty lines after splitting
            print(f"Skipping empty or malformed line: '{line}'")
            continue

        opcode = parts[0]

        if opcode == "START":
            if len(parts) > 1:
                address_counter = int(parts[1])
            else:
                print(f"Error: Missing operand for START in line: '{line}'")
        elif opcode in ["LTORG", "END"]:
            # Process literals in the current pool
            for literal in literal_table:
                if literal_table[literal] is None:  # Assign address if not done
                    literal_table[literal] = address_counter
                    address_counter += 1
            if opcode == "LTORG":
                pool_table.append(len(literal_table))  # Start new pool
        elif opcode in opcode_table:
            if len(parts) > 1:
                operand = parts[1]
                if operand.startswith("="):
                    if operand not in literal_table:
                        literal_table[operand] = None
                elif operand not in symbol_table:
                    symbol_table[operand] = None
            address_counter += 1
        elif opcode == "ORIGIN":
            if len(parts) > 1:
                address_counter = evaluate_expression(parts[1])
            else:
                print(f"Error: Missing expression for ORIGIN in line: '{line}'")
        elif opcode == "EQU":
            if len(parts) > 2:
                symbol, expression = parts[1], parts[2]
                symbol_table[symbol] = evaluate_expression(expression)
            else:
                print(f"Error: Invalid EQU statement in line: '{line}'")

# Second Pass: Generate Machine Code
def second_pass(assembly_code):
    global address_counter
    address_counter = 0
    machine_code = []

    for line in assembly_code:
        line = line.strip()
        print(f"Processing line (Second Pass): '{line}'")  # Debugging output

        if not line or line.startswith("#"):  # Skip empty lines and comments
            continue

        if ":" in line:  # Handle labels
            parts = line.split(":", 1)
            if len(parts) == 2:
                instruction = parts[1].strip()
                line = instruction  # Process the instruction part
            else:
                print(f"Error: Invalid label format in line: '{line}'")
                continue

        if not line:  # Skip if no instruction remains after label processing
            continue

        parts = line.split()
        if len(parts) == 0:  # Check for empty lines after splitting
            print(f"Skipping empty or malformed line: '{line}'")
            continue

        opcode = parts[0]

        if opcode == "START":
            if len(parts) > 1:
                address_counter = int(parts[1])
            else:
                print(f"Error: Missing operand for START in line: '{line}'")
        elif opcode in opcode_table:
            code_line = f"{address_counter:02X} {opcode_table[opcode]}"
            if len(parts) > 1:
                operand = parts[1]
                if operand.startswith("="):
                    if operand in literal_table:
                        code_line += f" {literal_table[operand]:02X}"
                    else:
                        print(f"Error: Undefined literal {operand} in line: '{line}'")
                elif operand in symbol_table:
                    code_line += f" {symbol_table[operand]:02X}"
                else:
                    print(f"Error: Undefined symbol {operand} in line: '{line}'")
            machine_code.append(code_line)
            address_counter += 1
        elif opcode in ["LTORG", "END"]:
            # Generate code for literals in the current pool
            for literal, address in literal_table.items():
                if address >= address_counter:
                    machine_code.append(f"{address:02X} {literal.strip('=')}")
                    address_counter += 1

    return machine_code

# Helper function to evaluate expressions for ORIGIN and EQU
def evaluate_expression(expression):
    if "+" in expression:
        symbol, offset = expression.split("+")
        return symbol_table[symbol.strip()] + int(offset)
    elif "-" in expression:
        symbol, offset = expression.split("-")
        return symbol_table[symbol.strip()] - int(offset)
    else:
        return int(expression)

# Main function to handle input and process assembly
def assemble_file(file_path):
    try:
        # Read assembly code from file
        with open(file_path, "r") as f:
            assembly_code = f.readlines()

        # First pass: Build Symbol and Literal Tables
        print("First Pass: Building Symbol and Literal Tables...")
        first_pass(assembly_code)
        print("\nSymbol Table:")
        for symbol, address in symbol_table.items():
            print(f"{symbol}: {address}")
        print("\nLiteral Table:")
        for literal, address in literal_table.items():
            print(f"{literal}: {address}")
        print("\nPool Table:")
        print(pool_table)

        # Second pass: Generate Machine Code
        print("\nSecond Pass: Generating Machine Code...")
        machine_code = second_pass(assembly_code)
        print("\nGenerated Machine Code:")
        for line in machine_code:
            print(line)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run assembler with input file
if __name__ == "__main__":
    # Example: Provide your .asm file path here
    input_file = "example.asm"
    assemble_file(input_file)
