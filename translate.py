#!/usr/bin/env python3
import sys
import re
from googletrans import Translator
import os.path
import time

def main():
    if len(sys.argv) < 2:
        print('Where da filename be yo? - ./script.py input-filename')
        sys.exit(2)
    translator = Translator()
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print('man that fing file ' + input_file + ' does not mafukin exist and hist!')
        sys.exit()
    output_file = input_file.replace('.en.', '.es.')
    print('Input file: ' + input_file + ' and Output file: ' + output_file)
    output_f = open(output_file, 'w')
    with open(input_file) as input_f:
        for line in input_f:
            #if re.match('^[A-Za-z]', line):
            if not re.match('(^[0-9]+$|^[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+|^$)', line):
                trans_output = translator.translate(line, src='en', dest='es')
                output_f.write(trans_output.text)
                print(trans_output.text)
            elif re.match('^[0-9]+$', line):
                output_f.write('\n' + line) 
            else:
                output_f.write(line)

    output_f.close()


if __name__== "__main__":
    main()
