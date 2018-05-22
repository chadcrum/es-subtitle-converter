#!/usr/bin/env python3
import shlex, subprocess
from flask import Flask 
import sys
import re
from googletrans import Translator
import os.path
import time

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    root_path = '/mnt/tvmovies/tv/'
    file_output = subprocess.check_output('find ' + root_path + ' -type f ', shell=True)
    output = ''
    print(file_output) 
    for i in file_output.decode().split("\n"):
        if re.search('.en.srt', i):
            output += '<a href="translate/?filename=' + i + '">' + i + '</a></br>'
        else:
            output += i + '</br>'
    return output

@app.route('/translate/')
def translate():
    filename = request.args.get("filename")
    response = translate_file(filename)
    print(response)
    return 'Output file is called ' + response

def translate_file(input_file):
    translator = Translator()
    output_file = input_file.replace('.en.srt', '.ca.srt')
    print('Input file: ' + input_file + ' and Output file: ' + output_file)
    try:
        output_f = open(output_file, 'w')
        with open(input_file) as input_f:
            content = input_f.read()
            for chunk in content.split('\n\n'):
                lines = chunk.split('\n')
                output_f.write(lines[0] + "\n")
                output_f.write(lines[1] + "\n")
                for line in lines[2:]:
                    trans_output = translator.translate(line, src='en', dest='es')
                    print(trans_output)
                    output_f.write(trans_output.text + "\n")
                output_f.write("\n")
    except Exception:
        print('problems')
    output_f.close()
    return output_file


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=9999, debug=True, threaded=True)

