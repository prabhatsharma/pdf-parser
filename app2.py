#!/Users/prabhsha/anaconda/bin/python

""" Extract text """
import os
import subprocess

# Get the list of files in the directory
file_list = os.listdir('pdfs')
# print(file_list)

for file in file_list:
      # print(file)
      f = file[0:len(file)-4]
      print(f)
      txt_command = 'pdf2txt.py -o txt/' + f + '.txt pdfs/' + file
      print(txt_command)
      os.system(txt_command)

  # os.system()


