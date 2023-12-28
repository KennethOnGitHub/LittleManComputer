from typing import List
import re

mnemonics = {
    'HLT': 000,
    'ADD': 100,
    'SUB': 200,
    'STA': 300,
    'LDA': 500,
    'BRA': 600,
    'BRA': 700,
    'BRP': 800,
    'INP': 901,
    'OUT': 902,
    'DAT': 0, #acts as a "nothing value"
    }



def asseble(file_path: str) -> List[int]:
    input_file = open(file_path, 'r')
    script = input_file.read()
    input_file.close()

    line_split_script = script.split('\n')

    print(line_split_script)

    tokenised_script = [[token for token in line.split(' ') if token != ''] for line in line_split_script if line != '']
    for line in tokenised_script:
        print(line)

    #A dictionary where value is the address where the label is last found
    labels = {

    }

    assembled_script:List[int] = []
    
    #First pass, where we just get the operator (the first digit) and index the labels
    for linenum, line in enumerate(tokenised_script):


        if len(line) > 3:
            raise Exception("Line {} has {} tokens, exceeding maximum of 3".format(linenum, len(line)))

        if line[0] in mnemonics.keys():
            assembled_script.append(mnemonics[line[0]])
        elif line[1] in mnemonics.keys():
            labels[linenum] = linenum
            assembled_script.append(mnemonics[line[1]])
       

    #Second pass, where we get the operand (the last two digits) using the labels
    for i, v in enumerate(assembled_script):
        original_line = tokenised_script[i]

        operand = original_line[-1]

        #input and output have no operands
        if operand == 'INP' or operand == 'OUT':
            continue








    return assembled_script


print(asseble('assemblytest.txt'))  