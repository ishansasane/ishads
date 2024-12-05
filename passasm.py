# MNEUMONIC TABLE
MNEMONIC_TABLE = {
    "STOP": "00",
    "ADD": "01",
    "SUB": "02",
    "MULT": "03",
    "MOVEM": "04",
    "MOVER": "05"
}

# Initialize Tables
SYMBOL_TABLE = []
LITERAL_TABLE = []

def process_line(line, lc):
    tokens = line.split()
    if not tokens:
        return lc

    first_word = tokens[0]

    # START directive
    if first_word == "START":
        lc = int(tokens[1])
        print(f"\n(AD, 01) (C, {lc})")
        return lc

    # END directive
    if first_word == "END":
        print(f"\n{lc}) (AD, 02)")
        process_literals(lc)
        return lc

    # Imperative statement
    if first_word in MNEMONIC_TABLE:
        print(f"\n{lc}) (IS, {MNEMONIC_TABLE[first_word]})", end="")
        lc += 1
        handle_operands(tokens[1:])
        return lc

    # Declarative statements (DC, DS)
    if len(tokens) > 1 and tokens[1] in ["DC", "DS"]:
        lc = handle_declarative(tokens, lc)
        return lc

    # Symbol declaration
    add_to_symbol_table(first_word, lc)
    return lc

def handle_operands(operands):
    if operands:
        reg_map = {"AREG": 1, "BREG": 2, "CREG": 3, "DREG": 4}
        if operands[0] in reg_map:
            print(f" (R, {reg_map[operands[0]]})", end="")

        if len(operands) > 1:
            second_operand = operands[1]
            if second_operand.startswith("="):  # Literal
                add_to_literal_table(second_operand)
            else:  # Symbol
                add_to_symbol_table(second_operand)

def handle_declarative(tokens, lc):
    symbol_name = tokens[0]
    directive = tokens[1]
    value = tokens[2]
    add_to_symbol_table(symbol_name, lc)

    if directive == "DC":
        print(f"\n{lc}) (DL, 01) (C, {value})")
        lc += 1
    elif directive == "DS":
        print(f"\n{lc}) (DL, 02) (C, {value})")
        lc += int(value)

    return lc

def add_to_symbol_table(name, address=None):
    for sym in SYMBOL_TABLE:
        if sym["name"] == name:
            if address is not None:
                sym["address"] = address
            return
    SYMBOL_TABLE.append({"name": name, "address": address})

def add_to_literal_table(literal):
    for lit in LITERAL_TABLE:
        if lit["name"] == literal:
            return
    LITERAL_TABLE.append({"name": literal, "address": None})

def process_literals(lc):
    for lit in LITERAL_TABLE:
        if lit["address"] is None:
            lit["address"] = lc
            print(f"{lc}) Literal {lit['name']} is processed")
            lc += 1

def print_tables():
    print("\n----------------------------------------------")
    print("\n\tSYMBOL TABLE")
    print("SRNO.\tSNAME\tSADDR")
    for i, sym in enumerate(SYMBOL_TABLE, start=1):
        print(f"{i}\t{sym['name']}\t{sym['address']}")

    print("\n----------------------------------------------")
    print("\n\tLITERAL TABLE")
    print("LRNO.\tLNAME\tLADDR")
    for i, lit in enumerate(LITERAL_TABLE, start=1):
        print(f"{i}\t{lit['name']}\t{lit['address']}")

# Main Function
def main():
    lc = 0
    try:
        with open("example.asm", "r") as file:
            for line in file:
                lc = process_line(line.strip(), lc)
    except FileNotFoundError:
        print("ERROR: File not found.")

    print_tables()

if __name__ == "__main__":
    main()
