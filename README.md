# 💡 SLFI — Scripting Language for Idiots

A programming language designed for ultimate simplicity on the outside, and monumental independence on the inside. Originally planned as a Python prototype, the compiler is being written entirely from scratch in C, moving towards a completely self-hosted ecosystem (custom compiler, linker, object format, and LSP).

> "Simplicity is the ultimate sophistication... or just for idiots."

---

## 🚀 Features & Roadmap

- [ ] **C Migration:** Core compiler architecture rewritten from Python to pure C.
- [ ] **Print and Package:** Enables the language to display text on the terminal and initialize packages.
- [ ] **Variables:** Enables the language to store data.
- [ ] **Conditionals:** Support for `if`, `elif`, and `else`.
- [ ] **Booleans:** Support for `True`, `False`, `0`, and `1`.
- [ ] **Finally Types:** Support for `int`, `string`, and `bool`. No more dynamic typing, sorry for destroying the chaos.

---

## 🛠️ Quick Start

### Prerequisites

You only need a C compiler like **GCC** or **Clang** installed on your system.

### Installation & Compilation

1. Clone the repository:

   ```fish
   git clone https://github.com
   cd slfi
   ```

2. Compile the native SLFI compiler:

   ```fish
   gcc main.c -o slfi
   ```

### Running your first `.slfi` script

1. Create a file named `main.slfi`:

   ```text
   package main

   init main() {
       print "Hello from SLFI!"; $ This is a Commentary! :3
   }
   ```

2. Compile and run using the native binary (Work In Progress):

   ```fish
   ./slfi main.slfi
   ```

---

## 📜 License

This project is licensed under the AGPLv3 License - see the LICENSE file for details.
