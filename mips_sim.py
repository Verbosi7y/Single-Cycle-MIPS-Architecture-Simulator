import sys
from os.path import *
from components.register import Register
from components.memory import Memory
from components.instruction_register import Instruction
from components.pc_register import ProgramCounter
from components.control import Control
from components.ALU_control import ALUControl
from components.ALU import ALU

"""
    File: mips_sim.py
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


# Verify if files exists before running
def verifyFiles(in_paths, com_paths):
    exit_bool = 0

    # Verify input files
    for path in in_paths:
        if not exists(in_paths[path]):
            print(fr"File Error: {in_paths[path]} is missing!\n")
            exit_bool = 1

    # Verify if components exists
    for path in com_paths:
        if not exists(com_paths[path]):
            print(fr"File Error: {com_paths[path]} is missing!\n")
            exit_bool = 1

    if exit_bool:
        print("Exiting program...")
        sys.exit(1)


def start():
    input_paths = {
        "imemory_path": "input/IMemory.txt",
        "instructions_path": "input/Instructions.txt",
    }

    output_paths = {
        "memory_path": "output/Memory.txt",
        "register_path": "output/Registers.txt",
    }

    component_paths = {
        "instruction_mem_path": "components/instruction_register.py",
        "pc_reg_path": "components/pc_register.py",
        "reg_path": "components/register.py"
    }

    verifyFiles(input_paths, component_paths)

    # Init. each component
    instruction_comp = Instruction()
    instruction_comp.loadInstructionFile()
    program_counter_comp = ProgramCounter()
    memory_comp = Memory()
    memory_comp.loadMemoryFile()
    register_comp = Register()
    control_comp = Control()
    alu_ctrl_comp = ALUControl()
    alu_comp = ALU()

    # Print Test (IGNORE)
    instruction_comp.printRegister()
    memory_comp.printMemory()
    register_comp.printRegister()
    control_comp.printControls()

    while True:
        # Step 1: Instruction Fetch (IF)
        instructionFetch(instruction_comp, program_counter_comp)

        # Step 2: Instruction Decode (ID)
        decode(alu_comp, alu_ctrl_comp, control_comp, instruction_comp, memory_comp, register_comp)

        # Step 3: Execute (EX)
        execute(alu_comp, alu_ctrl_comp)

        # Step 4: Memory (MEM)
        memory(alu_comp, control_comp, memory_comp, register_comp)

        # Step 5: Write Back (WB)
        writeBack(alu_comp, control_comp, memory_comp, register_comp)

        # Program Counter
        programCounterExecute(alu_comp, control_comp, instruction_comp, program_counter_comp)


def exitProgram(mem_comp, reg_comp):
    print(fr"----------FILE OUTPUT----------")
    mem_comp.writeMemoryFile()
    reg_comp.writeRegisterFile()
    print("Halting... exiting programing...")
    sys.exit(0)


def programCounterExecute(alu_comp, ctrl_comp, instruct_comp, pc_comp):
    curr_pc = pc_comp.getCounter() + 4
    sign_extend = ('0' * 14) + instruct_comp.getIType()["immediate"] + ('0' * 2)

    pc_src_ctrl = ctrl_comp.getCtrl("Branch") and alu_comp.getZero()
    pc_src_val = 0

    # pc_src_ctrl MUX
    # Branch = 1 and Zero = 1
    if pc_src_ctrl:
        pc_src_val = curr_pc + int(sign_extend, 2)
    # Branch or Zero != 0
    else:
        pc_src_val = curr_pc

    print(fr"pc_src_ctrl: {pc_src_ctrl}")
    print(fr"pc_src_val: {pc_src_val}")

    jmp_mux = ctrl_comp.getCtrl("Jump")
    # Jump MUX
    # Jump = 1
    if jmp_mux:
        pc_4bits_upper = '{:032b}'.format(pc_comp.getCounter())[0:4]
        curr_pc = pc_4bits_upper + instruct_comp.getCurrentInstruction()[6:32] + ('0' * 2)
        print(fr"JMP_MUX: {curr_pc}")
        pc_comp.setCounter(int(curr_pc, 2))
    # Jump = 0
    else:
        pc_comp.setCounter(pc_src_val)

    print(fr"Next PC: {pc_comp.getCounter()}")


def writeBack(alu_comp, ctrl_comp, mem_comp, reg_comp):
    # RegWrite == 1
    if ctrl_comp.getCtrl("RegWrite"):
        print(fr"MemtoReg: {ctrl_comp.getCtrl('MemtoReg')}")

        # MemtoReg == 1
        if ctrl_comp.getCtrl("MemtoReg"):
            reg_comp.setWriteData(int(mem_comp.getReadData(), 2))
        # MemtoReg == 0
        else:
            reg_comp.setWriteData(int(alu_comp.getResult(), 2))

        reg_comp.executeWriteData()


def memory(alu_comp, ctrl_comp, mem_comp, reg_comp):
    # Set Data Memory
    mem_comp.setAddress(alu_comp.getResult())
    mem_comp.setWriteData('{:032b}'.format(reg_comp.getReadData2()))

    # MemWrite == 1
    if ctrl_comp.getCtrl("MemWrite"):
        mem_comp.executeWriteData()

    # MemRead == 1
    if ctrl_comp.getCtrl("MemRead"):
        mem_comp.executeReadData()


def execute(alu_comp, alu_ctrl_comp):
    alu_comp.ALU32Bit(alu_ctrl_comp.getALUCtrl())


def decode(alu_comp, alu_ctrl_comp, ctrl_comp, instruct_comp, mem_comp, reg_comp):
    # Halt Condition
    if instruct_comp.getOPCode() == "111111":
        exitProgram(mem_comp, reg_comp)

    # Set the control signals
    ctrl_comp.setOPCode(int(instruct_comp.getOPCode(), 2))
    ctrl_comp.defineCtrlPara()

    # Set Address to Read Register 1 & 2
    reg_comp.setReadRegisters(instruct_comp.getRS(), instruct_comp.getRT())

    # RegDst MUX for Write Register
    # RegDst = 1
    if ctrl_comp.getCtrl("RegDst"):
        reg_comp.setWriteRegister(instruct_comp.getRType()["rd"])
    # RegDst = 0
    else:
        reg_comp.setWriteRegister(instruct_comp.getRT())

    # Set Read Data 1 & 2
    reg_comp.readData()

    # Set ALU Control
    alu_ctrl_comp.defineALUControl(instruct_comp.getOPCode(),
                                   instruct_comp.getRType()["funct"],
                                   ctrl_comp.getCtrl("ALUOp"))

    # Set ALU Data Bus
    sign_extended = ('0' * 16) + instruct_comp.getIType()["immediate"]
    print(fr"Immediate: {instruct_comp.getIType()['immediate']}")
    print(fr"Sign Extended: {sign_extended}")

    # ALUSrc = 1
    if ctrl_comp.getCtrl("ALUSrc"):
        alu_comp.setBuses(reg_comp.getReadData1(), int(instruct_comp.getIType()["immediate"], 2))
    # ALUSrc = 0
    else:
        alu_comp.setBuses(reg_comp.getReadData1(), reg_comp.getReadData2())


def instructionFetch(instruction_comp, pc_comp):
    print(fr"----------NEW INSTRUCTION FETCH----------")
    instruction_comp.setCurrentInstruction(pc_comp)
    print(instruction_comp.getCurrentInstruction())


if __name__ == "__main__":
    start()
