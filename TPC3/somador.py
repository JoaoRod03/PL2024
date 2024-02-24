import re
import sys


def sum(file_path):
    sum = 0
    on_off = False
    with open(file_path, 'r') as f:
        for line in f:
            parts = re.split(r' ', line, flags=re.IGNORECASE)
            for i, word in enumerate(parts):
                word = word.strip()
                if word.lower() == "on":
                    on_off = True
                elif word.lower() == "off":
                    on_off = False
                elif word == "=":
                    print("Somatório atual: " + str(sum))
                else:
                    if on_off:
                        numeros = re.findall(r'\d+', word)
                        for numero in numeros:
                            sum += int(numero)
    print("Somatório final: " + str(sum))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python somador.py <file_path>")
    else:
        sum(sys.argv[1])
