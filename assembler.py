from typing import List, Dict

mnemonics = {
    'HLT': 000,
    'ADD': 100,
    'SUB': 200,
    'STA': 300,
    'LDA': 500,
    'BRA': 600,
    'BRZ': 700,
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

    tokenised_script = [[token for token in line.split(' ') if token != ''] for line in line_split_script if line != '']

    labels: Dict[str, int] = {

    }

    label_pointers: Dict[str, List[int]]= {

    }

    assembled_script:List[int] = []
    #First pass, where we just get the operator (the first digit) and index the labels
    for linenum, line in enumerate(tokenised_script):


        if len(line) > 3:
            raise Exception("Line {} has {} tokens, exceeding maximum of 3".format(linenum, len(line)))

        command_index:int = None
        for i in range(2):
            if line[i] in mnemonics:
                command_index = i
                code = mnemonics[line[i]]
                assembled_script.append(code)
                break

            
        if command_index == None:
            raise Exception("Line {} does not have a command word (LDA, STA, etc)".format(linenum))
        
        is_labelled:bool = command_index == 1
        if is_labelled:
            label = line[0]
            labels[label] = linenum
        
        has_pointer:bool = command_index < (len(line) - 1)
        if has_pointer:
            pointer = line[-1]

            if pointer.isnumeric():
                assembled_script[linenum] += int(pointer)
                continue

            if pointer in label_pointers:
                label_pointers[pointer].append(linenum)
            else:
                label_pointers[pointer] = [linenum]


    if not set(label_pointers.keys()) <= set(labels.keys()):

        difference = set(label_pointers.keys()) - set(labels.keys())
        raise Exception("Pointers {} exist which do not have a corresponding label".format(difference))
    
    #Second pass where we then go back and "connect" the pointers to their labels
    for _, (label_name, label_address) in enumerate(labels.items()):
        for address in label_pointers[label_name]:
            assembled_script[address] += label_address

    return assembled_script