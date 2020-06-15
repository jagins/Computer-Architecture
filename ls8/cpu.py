"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        #add ram member = 256 bytes
        self.ram = [0] * 256
        #add registers = 8
        self.registers = [0] * 8
        #add program counter = PC value: 0
        self.pc = 0
        #make a binary operations table
        self.binary_ops = {
            0b10000010: 'LDI',
            0b01000111: 'PRN',
            0b00000001: 'HLT'
        }
    
    #add ram_read(address)
        #return the value stored in the address
    def ram_read(self, address):
        return self.ram[address]
    
    #add ram_write(address, value)
    def ram_write(self, address, value):
        self.ram[address] = value
        
    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8, operation type
            0b00000000, #register number
            0b00001000, #value to store in the register
            0b01000111, # PRN R0 print operation type
            0b00000000, #print whatever value is in register 0
            0b00000001, # HLT exit operation tpe and exit the emulator
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        #loop while true
        while running:
            #get the instruction from ram
            ir = self.ram_read(self.pc)
            
            #check if the instruction is LDI
            if self.binary_ops[ir] == 'LDI':
                #get the register number ramRead(pc + 1)
                register_num = int(self.ram_read(self.pc + 1))
                # #get the value self.reg[] = ramRed(pc + 2)
                value = int(self.ram_read(self.pc + 2))
                self.registers[register_num] = value
                
                #move to next instruction pc += 3
                self.pc += 3
            
            #else if check if the instruction is print
            elif self.binary_ops[ir] == 'PRN':
                register_num = self.ram_read(self.pc + 1)
                print(self.registers[register_num])
                self.pc += 2
            
            elif self.binary_ops[ir] == 'HLT':
                running = False
                self.pc += 1