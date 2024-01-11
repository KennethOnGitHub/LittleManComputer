from typing import List
import assembler
from KenQueue import CircularQueue

class CentralProcessingUnit:
    def __init__(self) -> None:
        self.ALU = ArithmeticLogicUnit()
        self.CU = ControlUnit()
        self.RAM = RandomAccessMemory()
        self.IO = InOutBaskets()

        self.initial_steps = [
            self.startCycle,
            self.readRam,
            self.copyMDRtoCIR,
            self.decodeAndExecute,
        ]

        self.steps = CircularQueue(30)
        for step in self.initial_steps:
            self.steps.enqueue(step)

        self.instruction_set = [
                                [#HLT
                                    self.halt
                                ],
                                [#ADD
                                    self.setMARtoOperand, 
                                    self.readRam,
                                    self.addMDRtoAccumulator
                                ], 
                                [#SUB
                                    self.setMARtoOperand,
                                    self.readRam,
                                    self.subMDRfromAccumulator

                                ],
                                [#STA
                                    self.copyACCtoMDR,
                                    self.setMARtoOperand,
                                    self.writeRam
                                ],
                                None,
                                [#LDA
                                    self.setMARtoOperand,
                                    self.readRam,
                                    self.copyMDRtoACC
                                ],
                                [#BRA
                                    self.setPCtoOperand
                                ],
                                [#BRZ
                                    self.brz
                                ],
                                [#BRP
                                    self.brp
                                ],
                                [#INP/OUT
                                    self.inout
                                ]
                            ]

    
    def startCycle(self):
        self.CU.MAR = self.CU.PC
        self.CU.PC += 1
        print("Starting the cycle, copied the PC to the MDR then incremented the PC")
    
    def halt(sef):
        print("Halting"), 
        exit()

    def readRam(self):
        print("Reading RAM")
        self.CU.MDR = self.RAM.getVal(self.CU.MAR)

    def writeRam(self):
        print("Writing RAM")
        self.RAM.setVal(self.CU.MAR, self.CU.MDR)
    
    def copyMDRtoACC(self):
        print("Copying contents of MDR to Accumulator")
        self.ALU.ACC = self.CU.MDR

    def copyMDRtoCIR(self):
        print("Copying contents of MDR to CIR")
        self.CU.CIR = self.CU.MDR

    def setPCtoOperand(self):
        print("Setting PC to CIR operand")
        operand = self.CU.CIR % 100
        self.CU.PC = operand

    def setMARtoOperand(self):
        print("Setting MAR to CIR operand")
        operand = self.CU.CIR % 100
        self.CU.MAR = operand
    
    def copyACCtoMDR(self):
        print("Copying contents of Accumulator to MDR")
        self.CU.MDR = self.ALU.ACC
    
    def copyMDRtoACC(self):
        print("Copying contents of MDR to Accumulator")
        self.ALU.ACC = self.CU.MDR
    
    def addMDRtoAccumulator(self):
        print("Adding value in MDR to Accumulator")
        self.ALU.ACC = self.ALU.add(self.ALU.ACC, self.CU.MDR)
    
    def subMDRfromAccumulator(self):
        print("Subtracting value in MDR to Accumulator")
        self.ALU.ACC = self.ALU.sub(self.ALU.ACC, self.CU.MDR)

    def request_input(self): #a CPU thing, but exists for the simulation to work
        self.IO.IN = int(input("Enter Input: "))
    
    def setACCtoInput(self):
        print("Setting value in Accumulator to value in Input")
        self.ALU.ACC = self.IO.IN

    def appendOutput(self):
        print("Outputting value")
        self.IO.OUT.append(self.ALU.ACC)

    def decodeAndExecute(self):
        print("Decoding instruction and starting execution")
        operator = self.CU.CIR // 100
        # operand = self.CU.CIR - operator * 100
        # self.steps += self.instruction_set[operator]
        # self.steps += self.initial_steps
        for step in self.instruction_set[operator]:
            print("step name = " + step.__name__)
            self.steps.enqueue(step)
        
        for step in self.initial_steps:
            self.steps.enqueue(step)
            


################################################## I don't much like this tbh, no one will know, but I don't like it. I don't like how they are their own "cpu actions" I could make a class for each LMC instruction and then have a "cpu actions" value that would change depending on a condition (like if the operand is 0 or 1 for inputs or the value of the ACC for the branching operations, but I really want to do other stuff) 
    def brz(self):
        if self.ALU.isEqual(self.ALU.ACC, 0):
            self.setPCtoOperand()

    def brp(self):
        if not self.ALU.isLess(self.ALU.ACC, 0):
            self.setPCtoOperand()

    def inout(self):
        if self.CU.CIR % 100 == 1:
            self.request_input()
            self.setACCtoInput()
        else:
            self.appendOutput()
####################################################

class ArithmeticLogicUnit:
    def __init__(self) -> None:
        self.ACC:int = 0

    def add(self, num1, num2) -> int:
        return num1 + num2
    
    def sub(self, num1, num2) -> int:
        return num1 - num2

    def isEqual(self, num1, num2) -> bool:
        return num1 == num2
    
    def isLess(self, num1, num2) -> bool:
        return num1 < num2

class ControlUnit:
    def __init__(self) -> None:
        self.PC:int = 0
        self.MAR:int = 0
        self.MDR:int = 0
        self.CIR:int = 0

    def startCycle(self) -> None:
        pass

class RandomAccessMemory:
    def __init__(self) -> None:
        self.mem:int = [0 for i in range(100) ]

    def getVal(self, address: int):
        return self.mem[address]

    def setVal(self, address: int, val: int) -> None:
        self.mem[address] = val

class InOutBaskets:
    def __init__(self) -> None:
        self.IN = 0
        self.OUT: List[int] = []


def main():
    CPU = CentralProcessingUnit()

    script_path: str = input("Enter script name: ")
    script_path = "scripts/" + script_path
    script: List[int] = assembler.asseble(script_path)

    for index, instruction in enumerate(script):
        CPU.RAM.setVal(index, instruction)
    
    def printCPU(): #place in CPU?
        print("PC - " + str(CPU.CU.PC))
        print("MAR - " + str(CPU.CU.MAR))
        print("." * 20)
        print("MDR - " + str(CPU.CU.MDR))
        print("CIR - " + str(CPU.CU.CIR))
        print("ACC - " + str(CPU.ALU.ACC))

        print('.' * 20 + '\nRAM')

        for row in range(10):
            startIndex = row*10
            endIndex = startIndex + 10
            print(CPU.RAM.mem[startIndex:endIndex])
        print("INP - " + str(CPU.IO.IN))
        print("OUT - " + str(CPU.IO.OUT))

    printCPU()

    run = True
    autostep: bool = False
    currentStep = 0
    while run:
        # CPU.steps[currentStep]()
        # currentStep += 1
        step = CPU.steps.dequeue()
        step()

        printCPU()

        # print([ x.__name__ for x in CPU.steps ])
        # print("CIR: " + str(CPU.CU.CIR) + " CIR % 100 = " +  str(CPU.CU.CIR % 100))
        
        if not autostep:
            userInput = input("Enter Command: ")
            match userInput:
                case "HLT":
                    print("Ending program")
                    run = False
                case "SSTEP":
                    pass
                case "LSTEP":
                    pass
                case "AUTO":
                    print("Autostepping...")
                    autostep = True
        print("*" * 20)
  
if __name__ == '__main__':
    main()