"""
    File: control.py
    Class: Control
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


class Control:

    def __init__(self):
        self.control_var = {
            "RegDst": 0,
            "Jump": 0,
            "Branch": 0,
            "MemRead": 0,
            "MemtoReg": 0,
            "ALUOp": [0, 0],
            "MemWrite": 0,
            "ALUSrc": 0,
            "RegWrite": 0,
        }

        self.curr_op = 0

    def printControls(self):
        print(self.control_var)

    def setCtrl(self, attribute_name, value):
        self.control_var[attribute_name] = value

    def setOPCode(self, val):
        self.curr_op = val

    def getCtrl(self, attribute_name):
        return self.control_var[attribute_name]

    def printOPCodeType(self):
        match self.curr_op:
            case 0:
                print("R-Type")
            case 8:
                print("addi")
            case 35:
                print("lw")
            case 43:
                print("sw")
            case 4:
                print("beq")
            case 2:
                print("j")

    def defineCtrlPara(self):
        print(fr"Current OPCode Value: {self.curr_op}")
        match self.curr_op:
            case 0:
                print("Setting R-Type...")
                self.control_var["RegDst"] = 1
                self.control_var["ALUSrc"] = 0
                self.control_var["MemtoReg"] = 0
                self.control_var["RegWrite"] = 1
                self.control_var["MemRead"] = 0
                self.control_var["MemWrite"] = 0
                self.control_var["Branch"] = 0
                self.control_var["ALUOp"] = [1, 0]
                self.control_var["Jump"] = 0
            case 9:
                print("Setting addiu...")
                self.control_var["RegDst"] = 0
                self.control_var["ALUSrc"] = 1
                self.control_var["MemtoReg"] = 0
                self.control_var["RegWrite"] = 1
                self.control_var["MemRead"] = 0
                self.control_var["MemWrite"] = 0
                self.control_var["Branch"] = 0
                self.control_var["ALUOp"] = [0, 0]
                self.control_var["Jump"] = 0
            case 35:
                print("Setting lw...")
                self.control_var["RegDst"] = 0
                self.control_var["ALUSrc"] = 1
                self.control_var["MemtoReg"] = 1
                self.control_var["RegWrite"] = 1
                self.control_var["MemRead"] = 1
                self.control_var["MemWrite"] = 0
                self.control_var["Branch"] = 0
                self.control_var["ALUOp"] = [0, 0]
                self.control_var["Jump"] = 0
            case 43:
                print("Setting sw...")
                self.control_var["ALUSrc"] = 1
                self.control_var["RegWrite"] = 0
                self.control_var["MemRead"] = 0
                self.control_var["MemWrite"] = 1
                self.control_var["Branch"] = 0
                self.control_var["ALUOp"] = [0, 0]
                self.control_var["Jump"] = 0
            case 4:
                print("beq")
                self.control_var["ALUSrc"] = 0
                self.control_var["RegWrite"] = 0
                self.control_var["MemRead"] = 0
                self.control_var["MemWrite"] = 0
                self.control_var["Branch"] = 1
                self.control_var["ALUOp"] = [0, 1]
                self.control_var["Jump"] = 0
            case 2:
                print("j")
                self.control_var["RegWrite"] = 0
                self.control_var["MemRead"] = 0
                self.control_var["MemWrite"] = 0
                self.control_var["Branch"] = 0
                self.control_var["Jump"] = 1
        print(self.control_var)
