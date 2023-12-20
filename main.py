import settings
from typing import List


def main():
    ALU = ArithmeticLogicUnit()
    CU = ControlUnit()
    RAM = RandomAccessMemory()

    IN_Basket: int = 0
    OUT_Basket: List[int] = []

    currentStep = 0

    #Load the script into RAM
    scriptFile = open('testscript.txt', 'r') 
    script = scriptFile.read()
    for index in range(int(len(script) / 4)):
        codeStart = index*4
        codeLen = 3
        value = int(script[codeStart: codeStart + codeLen])
        RAM.setVal(index, value)
    scriptFile.close()
    
        
    def startCycle():
        CU.MAR = CU.PC
        CU.PC += 1
        print("Started the cycle, copied the PC to the MDR then incremented the PC")

    def readRam():
        CU.MDR = RAM.getVal(CU.MAR)

    def writeRam():
        RAM.setVal(CU.MAR, CU.MDR)
    
    def copyMDRtoACC():
        ALU.ACC = CU.MDR

    def copyMDRtoCIR():
        CU.CIR = CU.MDR

    def request_input():
        IN_Basket = input("Enter Input: ")
    
    def HLT(operand): #this feels shite, maybe I could use a class but idk it might not be better :/
        pass
    def ADD(operand):
        CU.MAR = operand
        readRam()
        ALU.ACC = ALU.add(ALU.ACC, CU.MDR)
    def SUB(operand):
        CU.MAR = operand
        readRam()
        ALU.ACC = ALU.sub(ALU.ACC, CU.MDR)
    def STA(operand):
        CU.MDR = ALU.ACC
        CU.MAR = operand
        writeRam()
    def LDA(operand):
        CU.MAR = operand
        readRam()
        ALU.ACC = CU.MDR
    def BRA(operand):
        CU.CIR = operand
    def BRZ(operand):
        if ALU.isEqual(0, ALU.ACC):
            CU.CIR = operand
    def BRP(operand):
        if not ALU.isLess(ALU.ACC, 0):
            CU.CIR = operand
    def INPOUT(operand):
        if operand == 1:
            request_input()
            ALU.ACC = IN_Basket
        elif operand == 2:
            OUT_Basket.append(ALU.ACC)
    operations = [
        HLT,
        ADD,
        SUB,
        STA,
        None,
        LDA,
        BRA,
        BRZ,
        BRP,
        INPOUT,
    ]

    def decode():
        operator = CU.CIR // 100
        operand = CU.CIR - operator * 100
        operations[operator](operand)


    steps = [
        startCycle,
        readRam,
        copyMDRtoCIR,
        decode,
    ]

    def printCPU():
        print("*" * 20)
        print("PC - " + str(CU.PC))
        print("MAR - " + str(CU.MAR))
        print("." * 20)
        print("MDR - " + str(CU.MDR))
        print("CIR - " + str(CU.CIR))
        print("ACC - " + str(ALU.ACC))

        print('.' * 20 + '\nRAM')

        for row in range(10):
            startIndex = row*10
            endIndex = startIndex + 10
            print(RAM.mem[startIndex:endIndex])
        print("INP - " + str(IN_Basket))
        print("OUT - " + str(OUT_Basket))

    printCPU()

    run = True
    while run:
        currentStep = currentStep % 4
        steps[currentStep]()
        currentStep += 1
        printCPU()

        
        # match currentStep:
        #     case 0:
        #         print("Starting fetch")
        #     case 4:
        #         print("Starting decode")

        

        userInput = input("Enter Command: ")
        match userInput:
            case "HLT":
                print("Ending program")
                run = False
            case "CON":
                pass

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

def cycle():
    pass


  
if __name__ == '__main__':
    main()