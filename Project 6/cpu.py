"""
Duck Machine model DM2022W CPU
"""

from instr_format import Instruction, OpCode, CondFlag, decode
from typing import Tuple

from memory import Memory
from register import Register, ZeroRegister
from mvc import MVCEvent, MVCObservable

import logging
logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger(__name__)

class ALU(object):
    """The arithmetic logic unit (also called a "functional unit"
    in a modern CPU) executes a selected function but does not
    otherwise manage CPU state. A modern CPU core may have several
    ALUs to boost performance by performing multiple operatons
    in parallel, but the Duck Machine has just one ALU in one core.
    """
    # The ALU chooses one operation to apply based on a provided
    # operation code.  These are just simple functions of two arguments;
    # in hardware we would use a multiplexer circuit to connect the
    # inputs and output to the selected circuitry for each operation.
    ALU_OPS = {
        OpCode.ADD: lambda x, y: x + y,
        # For memory access operations load, store, the ALU
        # performs the address calculation
        OpCode.LOAD: lambda x, y: x + y,
        OpCode.STORE: lambda x, y: x + y,
        # Some operations perform no operation
        OpCode.HALT: lambda x, y: 0,
        OpCode.SUB: lambda x, y: x - y,
        OpCode.MUL: lambda x, y: x * y, 
        OpCode.DIV: lambda x, y: x // y
    }

def exec(self, op: OpCode, in1: int, in2: int) -> Tuple[int, CondFlag]:
    """looks up the operation in the ALU_OPS dictionary and applies function, then returns Condition flag"""
    function = ALU_OPS[op]
    function(in1, in2)
    try:
        function(in1, in2)      # how do i write this part?!
    except:
        return (0, CondFlag.V)
    if function(in1, in2) == 0:
        return CondFlag.Z           # result is 0
    elif function(in1, in2) > 0:
        return CondFlag.P           # result is positive
    elif function(in1, in2) < 0:
        return CondFlag.M           # result is negative

class CPUStep(MVCEvent):
    """CPU is beginning step with PC at a given address"""
    def __init__(self, subject: "CPU", pc_addr: int,
                 instr_word: int, instr: Instruction)-> None:
        self.subject = subject
        self.pc_addr = pc_addr
        self.instr_word = instr_word
        self.instr = instr

class CPU(MVCObservable):
    """Duck Machine central processing unit (CPU)
    has 16 registers (including r0 that always holds zero
    and r15 that holds the program counter), a few
    flag registers (condition codes, halted state),
    and some logic for sequencing execution.  The CPU
    does not contain the main memory but has a bus connecting
    it to a separate memory.
    """
    def __init__(self, memory: Memory):
        super().__init__()
        self.memory = memory  # Not part of CPU; what we really have is a connection
        self.registers = [ ZeroRegister(), Register(), Register(), Register(),
                           Register(), Register(), Register(), Register(),
                           Register(), Register(), Register(), Register(),
                           Register(), Register(), Register(), Register() ]
        self.condition = CondFlag.ALWAYS
        self.halted = False
        self.alu = ALU()

    def step(self):
        """The main part of the CPU's sequencing logic, carries out the fetch/decode/execute cycle""" 
        # fetch
        address = self.registers[15].get()
        instr_word = Memory.get(address)
        # decode
        instr = decode(instr_word)
        # Display the CPU state when we have decoded the instruction, 
        # before we have executed it
        self.notify_all(CPUStep(self, instr_addr, instr_word, instr))
        #execute
        if self.condition & instr.cond > 0:
            src1 = self.registers[instr.reg_target]
            src1.get()
            

    