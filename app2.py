#!/Users/prabhsha/anaconda/bin/python

""" Extract text """
import os
import csv
import xml.etree.ElementTree as ET

# Get the list of files in the directory
file_list = os.listdir('pdfs')
# print(file_list)

csvfile = open('analyze.csv', 'w')  
for file in file_list:
    
    """Iterate over all pdf files"""
    f = file[0:len(file) - 4]  # get just the file name without extension
    extension = file[len(file)-3:len(file)]
    print('extension:  ', extension)
    if extension == 'pdf':
        print(file)  # print filename

        txt_command = 'pdf2txt.py -o txt/' + f + \
            '.txt pdfs/' + file  # txt extraction command
        xml_command = 'pdf2txt.py -t xml -o xml/' + f + \
            '.xml pdfs/' + file  # xml extraction command
    
        os.system(txt_command)      # extract the pdf in txt format and place it in txt folder
        os.system(xml_command)      # extract the pdf in xml format and place it in xml folder

        tree = ET.parse('xml/' + f + '.xml')
        xml_document = tree.getroot()
        words = []

        for text_tag in xml_document.iter('textline'):  # Parse all text
            word_list = []
            word = ''
            font = ''
            font_size = 10
            word_location = ''
            temp_word = {}
            
            for character in text_tag:
                if character.text != '\n' and character.text != ' ' and len(character.text) != 0:
                    word += character.text
                    font_size = character.attrib['size']
                    word_location = character.attrib['bbox']
                    font = character.attrib['font']
                elif word != '':
                    temp_word['word'] = word.replace(',', ' ')
                    temp_word['font_size'] = font_size
                    temp_word['word_location'] = word_location
                    temp_word['font'] = font
                  #   print(temp_word)
                    words.append(temp_word)
                    word = ''
                    temp_word = {}
      #   print(words)
        annotated_words = ''

        for word in words:
              if 'Bold' in word['font']:  #  Capture all bold words
                    annotated_words += word['word'] + ' '
      #   print(annotated_words)
        
        file_data = ''
        with open('txt/' + f + '.txt', encoding="utf-8") as txt_file:
              file_data = txt_file.read().replace('\n', ' ').replace('\r', '').replace(',', ' ')
        txt_file.close()

      #   print(file_data)

        # write the contents to csv file
        csvfile.write(file + ',' + file_data + ',' + annotated_words + '\n')

        







