"""
    File: memory.py
    Class: Memory
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


class Memory:

    def __init__(self, input_path="input/IMemory.txt", output_path="output/Memory.txt"):
        # State of memory in list
        # 32 words (32 bits)
        # Address range: 00000 - 11111
        self.memory = list()
        self.input_path = input_path
        self.output_path = output_path

        # Input
        self.address = ""
        self.writeData = 0

        # Output
        self.readData = 0

    def loadMemoryFile(self):
        with open(fr"{self.input_path}", "r", encoding="utf8") as mem_file:
            self.memory = mem_file.read().splitlines()
            mem_file.close()

    # Memory.txt contains the current state of the memory
    def writeMemoryFile(self):
        with open(fr"{self.output_path}", "w", encoding="utf8") as out_mem_file:
            n = "\n".join(self.memory)
            out_mem_file.writelines(fr"{n}")
            out_mem_file.close()

    def setAddress(self, addr):
        self.address = addr

    def setWriteData(self, data):
        self.writeData = data
        print(fr"Memory setWriteData(data): {self.writeData}")

    def getReadData(self):
        return self.readData

    def executeReadData(self):
        self.readData = self.memory[int(self.address, 2)]
        print(fr"Memory executeReadData(self)")
        print(fr"Reading Data from: {int(self.address, 2)}")
        print(fr"Memory readData is now: {self.readData}")

    def executeWriteData(self):
        self.memory[int(self.address, 2)] = self.writeData
        print(fr"Writing Data to: {int(self.address, 2)}")

    def printMemory(self):
        print(self.memory)
