# 💡 SLFI — Scripting Language for Idiots

A programming language designed for ultimate simplicity on the outside, and monumental independence on the inside. Currently prototyping via a fast Python-to-C transpiler, moving towards a completely self-hosted ecosystem (custom compiler, linker, object format, and LSP).

> "Simplicity is the ultimate sophistication... or just for idiots."

---

## 🚀 Features & Roadmap

- [ ] **Print and Package:** Enables the language to display text on the terminal and initialize packages.
- [ ] **Variables:** Enables the language to store data.
- [ ] **Conditionals:** Support for `if`, `elif`, and `else`.
- [ ] **Booleans:** Support for `True`, `False`, `0`, and `1`.
- [ ] **Finally Types:** Support for `int`, `string`, and `bool`. No more dynamic typing, sorry for destroying the chaos.

---

## 🛠️ Quick Start (Prototype)

### Prerequisites

You need **Python 3** and a C compiler like **GCC** installed on your system.

### Installation

1. Clone the repository:

   ```fish
   git clone https://github.com/ykaruusmp4/slfi.git
   cd slfi
   ```

2. Install the parser engine:

   ```fish
   pip install lark

   # or use a venv in Arch Linux and Others PEP Operational Systems.
   ```

### Running your first `.slfi` script

1. Create a file named `main.slfi`:

   ```text
   print "Hello from SLFI!";
   ```

2. Compile and run using the prototype driver:

   ```fish
   python slfi.py main.slfi
   # or any other way, the slfi.py just need to be side-by-side if the main.slfi
   ./main
   ```

---

## 📜 License

This project is licensed under the AGPL License - see the LICENSE file for details.
