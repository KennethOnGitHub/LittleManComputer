from typing import List
import re



def asseble(file_path: str) -> List[int]:
    input_file = open(file_path, 'r')
    script = input_file.read()
    input_file.close()

    script = re.split(r' |\n', script)
    return script


print(asseble('test-trinum.txt'))