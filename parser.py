#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:40:14 2020

@author: nupoor


Requirements
1. Look for string citations
    Conditions for inclusion in data set:
        1. If TCQ, JTWC or TC, citations will look like ( xxx, ####; xxx, ####; ....) 
        2. If IEEE, citations will look like [],[],[],... or []-[]
2. Find frequency of authors from author_names in that data set
3. Find frequency of authors from author_names_contemporary in that data set

"""
import numpy as np
import re
from collections import deque
import xlsxwriter

filenames = np.loadtxt('filenames.txt', dtype='str')

with open('author_names.txt') as f:
    author_names = [word for line in f for word in line.split()]
    
NumOfAuthors = len(author_names)

#Workbook settings
workbook = xlsxwriter.Workbook('output1.xlsx')
worksheet = workbook.add_worksheet()

numOfFiles = len(filenames)
fileContent = []
filenames_updated = []
flag = 0
print("Number of total files:" +str(numOfFiles))
for i in range(numOfFiles):
    #Opening text files for parsing
    with open(filenames[i],'r') as f:
        abc = f.read()  
        flag = 0
    print(filenames[i])
    worksheet.write(i, 0, filenames[i])
    if ('IEEE' in filenames[i]):
        #flag = find_string_citation_ieee(filenames[i])
        #worksheet.write(i, 0, filenames[i])
        list_of_str=re.findall("(\[.{1,3}\]\, .*\])|(\[.{1,3}.*(\, .{1,3}.*[^a-z]\])|(\[.{1,3}\]–\[.{1,3}\]))", abc)
        #worksheet.write(i, 1, str(re.findall("(\[.{1,3}\]\, .*\])|(\[.{1,3}.*(\, .{1,3}.*[^a-z]\])|(\[.{1,3}\]–\[.{1,3}\]))", abc)))
        #worksheet.write(i, 2, len(re.findall("(\[.{1,3}\]\, .*\])|(\[.{1,3}.*(\, .{1,3}.*[^a-z]\])|(\[.{1,3}\]–\[.{1,3}\]))", abc)))
    elif ('JTWC' in filenames[i]):
        #flag = find_string_citation_jtwc(filenames[i])
        #worksheet.write(i, 0, filenames[i])
        list_of_str=re.findall("(\[.{1,3}\,.{1,3}[1-9]\d*\])|(\[.{1,3}\-.{1,3}\])|(\[\bsee\b .*\])|(\[[^\d].*\,.*\])", abc)
        if (len(list_of_str)<1):
            list_of_str=re.findall("(\(.*\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc)
        #list_of_str=re.findall("(\[.{1,3}\,.{1,3}[1-9]\d*\])|(\[.{1,3}\-.{1,3}\])|(\[\bsee\b .*\])|(\[[^\d].*\,.*\])", abc)
        #worksheet.write(i, 1, str(list_of_str))
        #worksheet.write(i, 2, len(list_of_str))
    else:
        #flag = find_string_citation_apa(filenames[i])
        #worksheet.write(i, 0, filenames[i])
        #list_of_strings = re.findall("(\(.*\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc) #works best!! Works for strings that do not start with a number but end with a number (may or may not follow by characters)
        list_of_str = re.findall("(\(.*\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc) #works best!! Works for strings that do not start with a number but end with a number (may or may not follow by characters)
        #worksheet.write(i, 1, str(re.findall("(\(.*\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc)))
        #worksheet.write(i, 2, len(re.findall("(\(.*\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc)))
    
    worksheet.write(i, 1, str(list_of_str))
    worksheet.write(i, 2, len(list_of_str))
    
    if flag == 1:
        filenames_updated.append(filenames[i])

f = open("updates_filenames.txt", "w")
for i in filenames_updated:
    f.write(i)
    f.write('\n')
f.close()
workbook.close()

def find_string_citation_apa(filename):
    with open(filename,'r') as f:
        abc = f.read()  
        flag = 0
        #x = re.findall("(\(.*\n?.*?\;.*\n?.*\))", abc) #works 
        list_of_strings = re.findall("(\(.*\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc) #works best!! Works for strings that do not start with a number but end with a number (may or may not follow by characters)
        print(list_of_strings)
        if list_of_strings:
            flag = 1
        else:
            flag = 0
    f.close()
    return flag

def find_string_citation_ieee(filename):
    with open(filename,'r') as f:
        abc = f.read()  
        flag = 0
       # print(re.findall("(\[.{1,3}\]\, .*\])|(\[.{1,3}.*(\, .{1,3}.*[^a-z]\])|(\[.{1,3}\]–\[.{1,3}\]))", abc))
        list_of_strings = re.findall("(\[.{1,3}\]\, .*\])|(\[.{1,3}.*(\, .{1,3}.*[^a-z]\])|(\[.{1,3}\]–\[.{1,3}\]))", abc) 
        print(list_of_strings)
        if list_of_strings:
            flag = 1
        else:
            flag = 0
    f.close()
    return flag

def find_string_citation_jtwc(filename):
    with open(filename,'r') as f:
        abc = f.read()  
        flag = 0
       # print(re.findall("(\[.{1,3}\]\, .*\])|(\[.{1,3}.*(\, .{1,3}.*[^a-z]\])|(\[.{1,3}\]–\[.{1,3}\]))", abc))
        list_of_strings = re.findall("(\[.{1,3}\,.{1,3}[1-9]\d*\])|(\[.{1,3}\-.{1,3}\])", abc) 
        print(list_of_strings)
        if list_of_strings:
            flag = 1
        else:
            flag = 0
    f.close()
    return flag


  
    with open(filenames[i]) as f:
        file1=[word for line in f for word in line.split()]
    fileContent.append(file1) 
    


for i in range(numOfFiles):
    if 'References' in fileContent[i]:
        index = fileContent[i].index('References')
        print (' '.join(fileContent[i][max(0,index):min(index+99999,len(fileContent[i]))])+'\n'+'\n')
     #   print(filenames[i])
    
    
print(len(fileContent))    
author_count = np.zeros((len(author_names)), int)


import time

start_time = time.time()

coun = -1
author_updated = []
for authors in author_names:
    if '.' not in authors:
        print('Author being looked up:', authors)
        coun+=1
        author_updated.append(authors)
        for files in range(numOfFiles):
            filenames[files]
            file1 = fileContent[files]
            for file_words in file1:
                if file_words == authors:
                    author_count[coun] += 1




    
    
    
'''    line_history = deque(maxlen=25)
    flag = 0
    with open(filename,'r') as f:
        
        for line in f:
            if '(' in line and ')' in line and ';' in line and ',' in line:
                #print(*line_history, line, sep='')
                print(line)
                flag = 1
                
                line_history.clear()
                
    return flag
      #      else:
       #         print('Not found in'+filename+'\n')
       
       
       end_time = time.time()     

elapsed_time = end_time-start_time    
'''
from nltk.tokenize import word_tokenize
with open('2013_TCQ_v22i1_Walton.txt','r') as f:
    abc = f.read()      
        
#x = re.findall("(\(.*\n?.*?\;.*\n?.*\))", abc) #works 
x = re.findall("(\(+\D.*\n?.*\d{4}.*\;+.*\n?.*\d{4}.*\))", abc) #works best!! Works for strings that do not start with a number but end with a number (may or may not follow by characters)
print(x)
        


