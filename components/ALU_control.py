"""
    File: ALU_control.py
    Class: ALUControl
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


class ALUControl:

    def __init__(self):
        # Output
        self.alu_ctrl = "0000"

    def getALUCtrl(self):
        return self.alu_ctrl

    def defineALUControl(self, opcode, funct, aluop):
        # R-Type
        if opcode == "000000":
            match funct:
                # addu, R-Type
                case "100001":
                    self.alu_ctrl = "0010"
                    print(fr"addu, R-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
                # subu, R-Type
                case "100011":
                    self.alu_ctrl = "0110"
                    print(fr"subu, R-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
                # and, R-Type
                case "100100":
                    self.alu_ctrl = "0000"
                    print(fr"and, R-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
                # or, R-Type
                case "100101":
                    self.alu_ctrl = "0001"
                    print(fr"or, R-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
                # nor, R-Type
                case "100111":
                    self.alu_ctrl = "1110"
                    print(fr"nor, R-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
        # addiu, I-Type
        elif opcode == "001001":
            self.alu_ctrl = "0010"
            print(fr"addiu, I-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
        # beq, I-Type
        elif opcode == "000100":
            self.alu_ctrl = "0110"
            print(fr"beq, I-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
        # lw I-Type
        elif opcode == "100011":
            self.alu_ctrl = "0010"
            print(fr"lw, I-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
        # sw I-Type
        elif opcode == "101011":
            self.alu_ctrl = "0010"
            print(fr"sw, I-Type, {opcode}, {funct}, {aluop}, {self.alu_ctrl}")
        # j or halt, J-Type
        elif opcode == "000010" or opcode == "111111":
            print(fr"J-Type Hit! Will either JUMP or HALT!")
        else:
            print(fr"Error: Incorrect opcode!")
