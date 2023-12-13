"""
    File: register.py
    Class: Register
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


class Register:

    def __init__(self, output_path=fr"output/Registers.txt"):
        # PATH
        self.output_path = output_path

        # 32-bit values of 32 registers (R0 - R31)
        self.registers = {}
        self.initRegisters()

        # Input
        self.readRegister1 = ""
        self.readRegister2 = ""
        self.writeRegister = ""
        self.writeData = ""

        # Output
        self.readData1 = ""
        self.readData2 = ""

    def initRegisters(self):
        self.registers = {fr"R{str(val)}": 0 for val in range(32)}

    # Registers.txt contains the current state of the memory
    def writeRegisterFile(self):
        with open(fr"{self.output_path}", "w", encoding="utf8") as out_reg_file:
            reg_list = list(self.registers.values())
            reg_bin = ['{:032b}'.format(reg_list[x]) for x in range(32)]
            n = "\n".join(reg_bin)
            out_reg_file.writelines(fr"{n}")
            out_reg_file.close()

    def printRegister(self):
        print(self.registers)

    def setReadRegisters(self, regAddr1, regAddr2):
        self.readRegister1 = regAddr1
        self.readRegister2 = regAddr2
        print(fr"readRegister1: {self.readRegister1}")
        print(fr"readRegister2: {self.readRegister2}")

    def setWriteRegister(self, regAddr1):
        self.writeRegister = regAddr1
        print(fr"Register setWriteRegister: {self.writeRegister}")

    def setWriteData(self, data):
        self.writeData = data
        print(fr"Register setWriteData(data): {self.writeRegister}")
        print(fr"Corresponding Reg Data is: {self.writeData}")

    def executeWriteData(self):
        self.registers["R" + str(int(self.writeRegister, 2))] = self.writeData
        print(fr"Write Data[R{str(int(self.writeRegister, 2))}]: {self.registers['R' + str(int(self.writeRegister, 2))]}")

    def getReadData1(self):
        return self.readData1

    def getReadData2(self):
        return self.readData2

    def readData(self):
        self.readData1 = self.registers[fr"R{int(self.readRegister1, 2)}"]
        self.readData2 = self.registers[fr"R{int(self.readRegister2, 2)}"]
        print(fr"readData()")
        print(fr"readData1: {self.readData1}")
        print(fr"readData2: {self.readData2}")
