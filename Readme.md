# Nand to Tetris I (ETCCNT301) — Capstone Project: Make the Computer Draw a Box

**Course:** Nand to Tetris I (ETCCNT301)  
**Institution:** School of Engineering & Technology, K.R. Mangalam University
**Name:** `Tanuj`  
**Roll Number:** `2501730312`  
**Personal Parameter ($K$):** `12` (Last 2 digits of roll number)

---

## 1. Project Overview

This repository contains the complete implementation of the **Hack Computer Stack** built from the ground up across three integrated layers:

1. **Part A — Hardware Architecture (HDL):** Building the central processing unit (`CPU.hdl`), memory-mapped I/O system (`Memory.hdl`), and top-level computer (`Computer.hdl`).
2. **Part B — Two-Pass Hack Assembler (Python):** Developing `assembler.py` to translate symbolic Hack assembly (`.asm`) into 16-bit binary machine code (`.hack`), complete with symbol-table export (`symbols.txt`).
3. **Part C — Interactive Graphics Assembly Program (`Box.asm`):** Writing a low-level Hack assembly routine that polls the keyboard memory map (`KBD`) and dynamically renders a customized black rectangle on the simulated screen (`SCREEN`).

---

## 2. Personalized Project Parameters ($K = 12$)

All hardware and software dimensions in this project are derived from the personal parameter **$K = 12$** (from roll number `2501730312`):

| Parameter | Formula | Calculated Value | Description |
| :--- | :--- | :--- | :--- |
| **Personal Number ($K$)** | Last 2 digits of Roll No. | `12` | Core project seed value |
| **Part B Extra Feature** | $K \bmod 3$ | `0` (`12 % 3 = 0`) | Exports all labels and variables with addresses to `symbols.txt` |
| **Box Start Row** | Row $K$ | `Row 12` | Vertical offset from top of screen |
| **Screen Base Address** | `16384 + (32 * K)` | `16768` (`16384 + 384`) | Starting word address in Screen RAM |
| **Box Height** | Fixed specification | `20 rows` (`20 pixels`) | Outer loop iteration count |
| **Box Width (Words)** | `(K mod 4) + 1` | `1 word` (`16 pixels`) | Inner loop word count per row (`(12 % 4) + 1 = 1`) |
| **Row Stride Offset** | `32 - Words_Per_Row` | `31 words` | Memory jump to reach the start of the next screen line |

---

## 3. Repository Structure

```text
capstone/
├── CPU.hdl           # Part A: Hack Central Processing Unit
├── Memory.hdl        # Part A: RAM16K + Screen + Keyboard memory map
├── Computer.hdl      # Part A: Top-level chip connecting ROM32K, CPU, and Memory
├── assembler.py      # Part B: Two-pass Python assembler with symbol table export
├── symbols.txt       # Part B: Auto-generated symbol & address mapping (K mod 3 == 0)
├── Box.asm           # Part C: Interactive Hack assembly program to draw the box
├── Box.hack          # Part C: Compiled 16-bit binary machine code for Box.asm
└── README.md         # Project documentation