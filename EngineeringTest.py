# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:39:42 2021

@author: Uppili
"""

import pandas as pd
import fnmatch
import os

def EngineeringTest(filepath, saveFileName):
# Some constants
#filepath = "G:\Engineering Test\Engineering Test Files"
#saveFileName = "Combined.csv"
    savedFilePath = filepath+"\\"+saveFileName

#Delete Combine CSV file if already exist
    if(os.path.exists(savedFilePath) and os.path.isfile(savedFilePath)): 
        os.remove(savedFilePath) 
        print("Combined CSV file deleted") 
    else: 
        print("Combined CSV file not found")

#Read Data Content in the file
    filenames = os.listdir(filepath)

    num = 0
    dfs_combined = []
    for name in filenames:
        #Check for the Filename to add Environment
        if fnmatch.fnmatch(name, 'Asia*.csv'):
            Environment = "Asia Prod"
            df1 = pd.read_csv (filepath+'\\'+ name)
            df1['Environment'] = Environment
        elif fnmatch.fnmatch(name, 'NA*.csv'):
            Environment = "NA Prod"
            df1 = pd.read_csv (filepath+'\\'+ name)
            df1['Environment'] = Environment

        else:        
        #print(f'The {num} file is being merged')
            dfs_combined.append(pd.read_csv(os.path.join(filepath,name)))
        
        dfs_combined.append(df1)    
        
        num += 1    #In order to see which table was merged into

#concat all the dataframe
    dfFinalCombined_Table = pd.concat(dfs_combined)

#Export the dataframe as CSV
    dfFinalCombined_Table.to_csv(filepath + '\\' + saveFileName,index=False)
    print("Exported as csv to" + savedFilePath)
    
EngineeringTest("G:\Engineering Test\Engineering Test Files","Combined.csv")