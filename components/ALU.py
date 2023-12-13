"""
    File: ALU.py
    Class: ALU
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


def singleBitALU(binvert, cin, operation, a, b):
    c = (not b if binvert else b)

    match int(operation, 2):
        # 0000, and
        case 0:
            return a and c, cin
        # 0001, or
        case 1:
            return a or c, cin
        # 0010, add
        case 2:
            total = a + c + cin
            if not total:
                return 0, 0
            if total == 1:
                return 1, 0
            if total == 2:
                return 0, 1
            if total == 3:
                return 1, 1
        # 0110, sub (using adder)
        case 6:
            total = a + c + cin
            if not total:
                return 0, 0
            if total == 1:
                return 1, 0
            if total == 2:
                return 0, 1
            if total == 3:
                return 1, 1
        # 1110, nor
        case 14:
            return int(not (a | b)), cin


class ALU:

    def __init__(self):
        # Input
        self.busA = ""
        self.busB = ""
        self.writeData = ""

        # Output
        self.output = ""
        self.zero = 0

    def setBuses(self, dataA, dataB):
        self.busA = '{:032b}'.format(dataA)
        self.busB = '{:032b}'.format(dataB)
        print(fr"BusA: {self.busA}")
        print(fr"BusB: {self.busB}")

    def setWriteData(self, data):
        self.writeData = data

    def getResult(self):
        return self.output

    def getZero(self):
        return self.zero

    def ALU32Bit(self, operation):
        print(fr"BusA: {self.busA}")
        print(fr"BusB: {self.busB}")
        print(fr"Operation: {operation}")
        # Set cin to 1 if sub because binvert is 1 if op == sub
        cin = 1 if operation == '0110' else 0
        binvert = cin
        result = [0] * 32

        for i in range(32):
            output = singleBitALU(binvert, cin, operation, int(self.busA[31-i]), int(self.busB[31-i]))
            result[31-i] = (str(output[0]))
            cin = output[1]

        self.output = ''.join(result)
        self.zero = 0 if not self.output else 1
        print(fr"Output: {self.output}")
        print(fr"Zero: {self.zero}")
