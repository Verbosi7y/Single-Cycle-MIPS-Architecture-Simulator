# Single-Cycle MIPS Architecture Simulator
### Author: Darwin Xue

Simulation of a single-cycle MIPS CPU Architecture through memory state and instructions in 32-bits to emulate all 5-steps of a MIPS processor.
1. Instruction Fetch
2. Decode
3. Execute
4. Memory
5. Write Back.

## Installation
**IMPORTANT: MAKE SURE YOU ARE USING Python 3.10+, OTHERWISE IT WILL NOT RUN!**

1. If `./input` or `./output` folder is not present, execute `./setup.py` to automatically generate the folders or manually create these two folders.

2. Make sure the `./components` folder exist and these files are inside.
- ALU.py
- ALU_control.py
- control.py
- instruction_register.py
- memory.py
- pc_register.py
- register.py

3. Lastly, make sure `./mips_sim.py` exists to run the simulation.

If any of these components or files are missing, the [repository](https://github.com/Verbosi7y/Single-Cycle-MIPS-Architecture-Simulator) should contain the files necessary.

If the repository is private, please contact me through [GitHub](https://github.com/Verbosi7y) or [email](mailto:x21@umbc.edu).

```bash
./setup.py
```

## Usage

1. It is very important that the `./input` folder contains these two files (Case Sensitive):
- IMemory.txt
- Instructions.txt

Each lines in IMemory.txt MUST BE 32-bits wide and must contain 32 lines in total.

Each lines in Instructions.txt MUST BE 4-bits wide and the total line count must be a multiple of 4 (i.e. 4 lines or 20 lines...)


```bash
./mips_sim.py

```

### README.md
Last Updated: December 13th, 2023
