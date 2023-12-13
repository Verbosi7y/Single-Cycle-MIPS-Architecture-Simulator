"""
    File: instruction_register.py
    Class: Instruction
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


class Instruction:
    def __init__(self, input_path="input/Instructions.txt"):
        # Instructions are in byte (4 bytes each)
        self.instruction_reg = list()
        self.curr_instruction = ""
        self.instruction_path = input_path

    def loadInstructionFile(self):
        with open(fr"{self.instruction_path}", 'r') as instruct_file:
            self.instruction_reg = instruct_file.read().splitlines()
            instruct_file.close()

    def printRegister(self):
        print(self.instruction_reg)

    def setCurrentInstruction(self, pc_comp):
        self.curr_instruction = "".join(self.instruction_reg[pc_comp.getCounter():pc_comp.getCounter()+4])

    def getCurrentInstruction(self):
        return self.curr_instruction

    def getInstruction(self, address):
        return self.instruction_reg[address]

    def getInstructionRange(self, start, end):
        return self.instruction_reg[start:end]

    def getOPCode(self):
        return self.curr_instruction[0:6]

    def getRS(self):
        return self.curr_instruction[6:11]

    def getRT(self):
        return self.curr_instruction[11:16]

    def getRType(self):
        return {
            'op': self.curr_instruction[0:6],
            'rs': self.curr_instruction[6:11],
            'rt': self.curr_instruction[11:16],
            'rd': self.curr_instruction[16:21],
            'shamt': self.curr_instruction[21:26],
            'funct': self.curr_instruction[26:32]
        }

    def getIType(self):
        return {
            'op': self.curr_instruction[0:6],
            'rs': self.curr_instruction[6:11],
            'rt': self.curr_instruction[11:16],
            'immediate': self.curr_instruction[16:32],
        }
