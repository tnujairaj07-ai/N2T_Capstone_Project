import sys

DEST_MAP = {"": "000", "M": "001", "D": "010", "MD": "011", 
            "A": "100", "AM": "101", "AD": "110", "AMD": "111"}

JUMP_MAP = {"": "000", "JGT": "001", "JEQ": "010", "JGE": "011", 
            "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}

COMP_MAP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0010000", "!D": "0001101", "!A": "0010001",
    "-D": "0001111", "-A": "0010011", "D+1": "0011111", "A+1": "0011010",
    "D-1": "0001110", "A-1": "0010010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    "M": "1010000", "!M": "1010001", "-M": "1010011", "M+1": "1011010",
    "M-1": "1010010", "D+M": "1000010", "D-M": "1010011", "M-D": "1000111",
    "D&M": "1000000", "D|M": "1010101"
}

def clean_line(line):
    return line.split("//")[0].strip()

def assemble(file_path, k_val):
    symbol_table = {
        "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
        "SCREEN": 16384, "KBD": 24576
    }
    for i in range(16):
        symbol_table[f"R{i}"] = i

    with open(file_path, 'r') as f:
        lines = f.readlines()

    cleaned_lines = []
    rom_addr = 0
    seen_labels = set()
    
    # PASS 1: Clean lines & extract label symbols
    for line_num, line in enumerate(lines, 1):
        c_line = clean_line(line)
        if not c_line:
            continue
        if c_line.startswith("(") and c_line.endswith(")"):
            label = c_line[1:-1].strip()
            if k_val % 3 == 2 and label in seen_labels:
                print(f"Warning: Duplicate label '{label}' on line {line_num}.")
            seen_labels.add(label)
            symbol_table[label] = rom_addr
        else:
            cleaned_lines.append((line_num, c_line))
            rom_addr += 1

    # PASS 2: Translate instructions & assign variable symbols
    ram_var_addr = 16
    hack_binary = []

    for line_num, line in cleaned_lines:
        if line.startswith("@"):
            val = line[1:]
            if val.isdigit():
                addr = int(val)
            else:
                if val not in symbol_table:
                    symbol_table[val] = ram_var_addr
                    ram_var_addr += 1
                addr = symbol_table[val]
            hack_binary.append(f"{addr:016b}")
        else:
            dest, comp, jump = "", "", ""
            temp = line
            if "=" in temp:
                dest, temp = temp.split("=")
            if ";" in temp:
                comp, jump = temp.split(";")
            else:
                comp = temp

            dest, comp, jump = dest.strip(), comp.strip(), jump.strip()

            if comp not in COMP_MAP or dest not in DEST_MAP or jump not in JUMP_MAP:
                if k_val % 3 == 1:
                    print(f"Line {line_num}: invalid instruction '{line}'")
                    return
                else:
                    raise SyntaxError(f"Line {line_num}: invalid instruction '{line}'")

            c_bits, d_bits, j_bits = COMP_MAP[comp], DEST_MAP[dest], JUMP_MAP[jump]
            hack_binary.append(f"111{c_bits}{d_bits}{j_bits}")

    out_path = file_path.replace(".asm", ".hack")
    with open(out_path, 'w') as f:
        f.write("\n".join(hack_binary) + "\n")
    print(f"Assembly succeeded: {out_path}")

    if k_val % 3 == 0:
        with open("symbols.txt", "w") as f:
            for k, v in sorted(symbol_table.items()):
                f.write(f"{k}: {v}\n")
        print("Generated symbols.txt")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python assembler.py <file.asm> <K_value>")
    else:
        assemble(sys.argv[1], int(sys.argv[2]))