#!/Users/prabhsha/anaconda/bin/python

""" Extract text """
import os
import subprocess
import xml.etree.ElementTree as ET

# Get the list of files in the directory
file_list = os.listdir('pdfs')
# print(file_list)

for file in file_list:
    """Iterate over all pdf files"""
    f = file[0:len(file)-4]
    print(file) # print filename

    txt_command = 'pdf2txt.py -o txt/' + f + '.txt pdfs/' + file  # txt extraction command
    xml_command = 'pdf2txt.py -t xml -o xml/' + f + '.xml pdfs/' + file # xml extraction command
    os.system(txt_command)
    os.system(xml_command)


    tree = ET.parse('xml/' + f + '.xml')
    xml_document = tree.getroot()
    
    for text_tag in xml_document.iter('textline'):
          word_list = []
          word = ''
          font = ''
          font_size = 10
          word_location = ''
          temp_word = {}
          for character in text_tag:
                if character.text != '\n' and character.text != ' ' and character.text != '':
                      word += character.text
                      font_size = character.attrib['size']
                      word_location = character.attrib['bbox']
                elif word != '':
                      temp_word['word'] = word
                      temp_word['font_size'] = font_size
                      temp_word['word_location'] = word_location
                      
                      print(temp_word)
                      word = ''
                      temp_word = {}
          # print(text_tag)


  # os.system()


