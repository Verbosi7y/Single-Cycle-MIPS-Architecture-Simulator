"""
    File: pc_register
    Class: ProgramCounter
"""
"""
    Author: Darwin Xue
    Email: x21@umbc.edu
    Class: Computer Science 411: Computer Architecture
    Professor: Dr. Chenchen Liu

    Project: Single-Cycle MIPS Architecture Simulator
    Version: 1.00

    Description: Simulation of a single-cycle MIPS CPU Architecture
                 through memory state and instructions in 32-bits to
                 emulate all 5-steps of a MIPS processor.
                 Instruction Fetch, Decode, Execute, Memory, and Write Back.

    Instruction Mnemonics:
        Data Transfers: LW, SW
        Arithmetic/logical: ADDU, ADDIU, SUBU, AND, OR, NOR
        Control: BEQ, J
        Special Purpose: HALT (to halt the simulation)
"""


class ProgramCounter:

    def __init__(self):
        # Fetch address of next instruction by incrementing program_counter_reg by 4
        # PC + 4
        self.program_counter_reg = 0

    def printCounter(self):
        print(self.program_counter_reg)

    def getCounter(self):
        return self.program_counter_reg

    def setCounter(self, val):
        self.program_counter_reg = val
