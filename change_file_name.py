# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 08:50:31 2015

@author: yuri
"""

import os

parent = '/home/yuri/Documents/volga_german/volgagerman/images_sorted'

os.getcwd()
os.chdir('/home/yuri/Documents/volga_german/volgagerman/images_sorted')

folder = os.getcwd()
for root, dirs, files in os.walk(folder, topdown=False):
    print root
    print dirs 
    for dir in dirs:
        print dir 
        target = parent+'/'+dir       
        os.chdir(target)
        folder2 = os.getcwd()
        filenames = next(os.walk(folder2))[2]
        print filenames
        for filename in filenames:
            if 'tif' in filename and '_' not in filename:
                new_filename_split = filename.split('.')
                print new_filename_split                
                new_filename = new_filename_split[0] + '_1.tif'
                print filename                
                print new_filename
                os.rename(filename, new_filename)
                
                
    
              
          
              