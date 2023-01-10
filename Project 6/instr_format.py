"""
Instruction format for the Duck Machine 2022W (DM2022W),
a simulated computer modeled loosely on the ARM processor
found in many cell phones and the Raspberry Pi.

Instruction words are unsigned 32-bit integers
with the following fields (from high-order to low-order bits).  
All are unsigned except offset, which is a signed value in 
range -2^11 to 2^11 - 1. 

See docs/duck_machine.md for details. 
"""
from bitfield import BitField
from enum import Enum, Flag

# The field bit positions
reserved = BitField(31,31)
instr_field = BitField(26, 30)
cond_field = BitField(22, 25)
reg_target_field = BitField(18, 21)
reg_src1_field = BitField(14, 17)
reg_src2_field = BitField(10, 13)
# the offset field is signed and can be negative
offset_field = BitField(0, 9)

# The following operation codes control both the ALU and some
# other parts of the CPU.  
# ADD, SUB, MUL, DIV, SHL, SHR are ALU-only operations
# HALT, LOAD, STORE involve other parts of the CPU

class OpCode(Enum):
    """The operation codes specify what the CPU and ALU should do."""
    # CPU control (beyond ALU)
    HALT = 0    # Stop the computer simulation (in Duck Machine project)
    LOAD = 1    # Transfer from memory to register
    STORE = 2   # Transfer from register to memory
    # ALU operations
    ADD = 3     # Addition
    SUB = 5     # Subtraction
    MUL = 6     # Multiplication
    DIV = 7     # Integer division (like // in Python)

class CondFlag(Flag):
    """The condition mask in an instruction and the format
    of the condition code register are the same, so we can 
    logically and them to predicate an instruction. 
    """
    M = 1  # Minus (negative)
    Z = 2  # Zero
    P = 4  # Positive
    V = 8  # Overflow (arithmetic error, e.g., divide by zero)
    NEVER = 0
    ALWAYS = M | Z | P | V
    def __str__(self):
        """
        If the exact combination has a name, we return that.
        Otherwise, we combine bits, e.g., ZP for non-negative.
        """
        for i in CondFlag:
            if i is self:
                return i.name
        # No exact alias; give name as sequence of bit names
        bits = []
        for i in CondFlag:
            # The following test is designed to exclude
            # the special combinations 'NEVER' and 'ALWAYS'
            masked = self & i
            if masked and masked is i:
                bits.append(i.name)
        return "".join(bits)

# Registers are numbered from 0 to 15, and have names
# like r3, r15, etc.  Two special registers have additional
# names:  r0 is called 'zero' because on the DM2022W it always
# holds value 0, and r15 is called 'pc' because it is used to
# hold the program counter.
#
NAMED_REGS = {
    "r0": 0, "zero": 0,
    "r1": 1, "r2": 2, "r3": 3, "r4": 4, "r5": 5, "r6": 6, "r7": 7, "r8": 8,
    "r9": 9, "r10": 10, "r11": 11, "r12": 12, "r13": 13, "r14": 14,
    "r15": 15, "pc": 15
    }

# A complete DM2022W instruction word, in its decoded form.  In DM2022W
# memory an instruction is just an int.  Before executing an instruction,
# we decoded it into an Instruction object so that we can more easily
# interpret its fields.
#
class Instruction(object):
    """An instruction is made up of several fields, which 
    are represented here as object fields.
    """
    def __init__(self, op: OpCode, cond: CondFlag,
                     reg_target: int, reg_src1: int,
                     reg_src2: int,
                     offset: int):
        """Assemble an instruction from its fields. """
        self.op = op
        self.cond = cond
        self.reg_target = reg_target
        self.reg_src1 = reg_src1
        self.reg_src2 = reg_src2
        self.offset = offset
        return

    def __str__(self):
        """String representation looks something like assembly code"""
        if self.cond is CondFlag.ALWAYS:
            cond_codes = ""
        else:
            cond_codes = "/{}".format(self.cond)

        return "{}{:4}  r{},r{},r{}[{}]".format(
            self.op.name, cond_codes,
            self.reg_target, self.reg_src1,
            self.reg_src2, self.offset)

def decode(word: int) -> Instruction:
    """Decode a memory word (32 bit int) into a new Instruction.
            
    Args:
        word: a 32-bit int, the instruction to be decoded
    """
    reserved_word = reserved.extract(word)
    instr_field_word = instr_field.extract(word)
    cond_field_word = cond_field.extract(word)
    reg_target = reg_target_field.extract(word)
    reg_src1 = reg_src1_field.extract(word)
    reg_src2 = reg_src2_field.extract(word)
    offset_word = offset_field.extract_signed(word)

    decoded_word = Instruction(instr_field_word, cond_field_word, reg_target, reg_src1, reg_src2, offset_word)

    return decoded_word

def encode(self) -> int:
    """Encode instruction as 32-bit integer"""
    return f'0{self.op}+{self.cond}+{self.reg_target}+{self.reg_src1}+{self.reg_src2}+{self.offset}'

    