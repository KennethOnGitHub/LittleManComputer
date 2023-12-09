
import settings


def main():
    ALU = ArithmeticLogicUnit()
    CU = ControlUnit()
    RAM = RandomAccessMemory()

    def startCycle():
        CU.MAR = CU.PC
        CU.PC += 1
        print("Started the cycle, copied the PC to the MDR then incremented the PC")

    def queryRam():
        CU.MDR = RAM.getVal(CU.MAR)
    
    def copyMDRtoACC():
        ALU.ACC = CU.MDR

    def copyMDRtoCIR():
        CU.CIR = CU.MDR
    
    def decode():
        operator = CU.CIR // 100
        operand = CU.CIR - operator * 100


    steps = [
        startCycle,
        queryRam,
        copyMDRtoACC,
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

        print("OUT - ")

    printCPU()

    run = True
    currentStep = 0
    while run:
        printCPU()

        
        # match currentStep:
        #     case 0:
        #         print("Starting fetch")
        #     case 4:
        #         print("Starting decode")

        steps[currentStep]()
        currentStep += 1

        

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

    def add(num1, num2) -> int:
        return num1 + num2
    
    def sub(num1, num2) -> int:
        return num1 - num2

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

    def setVal(address: int):
        pass

def cycle():
    pass


  
if __name__ == '__main__':
    main()