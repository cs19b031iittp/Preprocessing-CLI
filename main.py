from fileinput import filename
import pyfiglet
import argparse
import os
import numpy as np
import pandas as pd

from data_description import *
from imputation import *
from categorical import *
from feature_scaling import *

join = os.path.join

def isValidFile(file):
    assert os.path.exists(join(os.getcwd(), file)) and file[-3:] == 'csv'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A tool for all your preprocessing needs!')
    parser.add_argument('--file', type=str, required=True,
                        help='Pass your csv file')
    args = parser.parse_args()

    # Check if file exists
    try:
        isValidFile(args.file)
    except:
        print("File does not exist. Enter a file with csv format")
        exit()

    print(pyfiglet.figlet_format("Dataset Preprocessing!!"))

    # Read file
    df = pd.read_csv(args.file)
    print('Columns present in the given dataset: ')
    print(', '.join(df.columns))
    print()

    # Ask for target variable
    target = ''

    while True:
        target = input('Which is the target variable (-1 to exit): ')
        if target != '-1':
            if target not in df.columns:
                print('Enter a column name from the list of columns')
            else:
                break
        else:
            exit()

    print()

    data = df.drop([target], axis=1).copy()

    while True:
        print('Tasks (Preprocessing)')
        print()
        print('1. Data Description')
        print('2. Handling NULL values')
        print('3. Encoding Categorical Data')
        print('4. Feature scaling of the dataset')
        print('5. Download the modified dataset')
        print()

        task = 0
        while True:
            try:
                task = int(input('What do you want to do? (-1 to exit): '))
                assert task in [-1, 1, 2, 3, 4, 5]
                break
            except:
                print('Enter a valid digit from the above')

        if task == -1:
            break # Exits program
        print()
        
        while True:
            if task == 1: # Data Description
                print('Tasks (Data Description)')
                print()
                print('1. Describe a specific column')
                print('2. Show properties of each column')
                print('3. Show the dataset')
                print()

                while True:
                    resp = int(input("What do you want to do? (-1 to go back): "))
                    if resp not in [-1, 1, 2, 3]:
                        print('Enter a valid digit')
                    else:
                        break
                
                if resp == -1:
                    break

                print()
                if resp == 1:
                    print('Columns:', ', '.join(data.columns))
                    while True:
                        col = input('Which column?: ')
                        if col not in data.columns:
                            print('Enter valid column name')
                        else:
                            break
                    
                    print()
                    specific_column(data, col)
                    print()

                if resp == 2:
                    all_columns(data)
                    print()
                
                if resp == 3:
                    while True:
                        rows = int(input("How many rows (>0) to print?: "))
                        if rows <= 0:
                            print(">0 rows")
                        else:
                            break
                    
                    print_rows(data, rows)
                    print()
            
            elif task == 2: # Handling NULL values
                print('Tasks (Handling NULL values)')
                print()
                print('1. Show number of NULL values')
                print('2. Remove columns')
                print('3. Fill NULL values (with mean)')
                print('4. Fill NULL values (with median)')
                print('5. Fill NULL values (with mode)')
                print('6. Show the dataset')
                print()

                while True:
                    resp = int(input("What do you want to do? (-1 to go back): "))
                    if resp not in [-1, 1, 2, 3, 4, 5, 6, 7]:
                        print('Enter a valid digit')
                    else:
                        break
                
                if resp == -1:
                    break
                
                print()

                if resp == 1:
                    print('Number of NULL values in each column')
                    print()
                    print(data.isnull().sum())
                    print()
                
                elif resp == 2:
                    print('Columns:', ', '.join(data.columns))
                    print('Enter columns separated by space')
                    cols = input('Which columns to remove?: ').split()
                    data = removeColumns(data, cols)
                    print()

                elif resp == 3:
                    print('Columns:', ', '.join(data.columns))
                    col = input('Which column?: ')
                    data = impute(data, col, 'mean')
                    print()
                
                elif resp == 4:
                    print('Columns:', ', '.join(data.columns))
                    col = input('Which column?: ')
                    data = impute(data, col, 'median')
                    print()
                
                elif resp == 5:
                    print('Columns:', ', '.join(data.columns))
                    col = input('Which column?: ')
                    impute(data, col, 'mode')
                    print()
                
                elif resp == 6:
                    while True:
                        rows = int(input("How many rows (>0) to print?: "))
                        if rows <= 0:
                            print(">0 rows")
                        else:
                            break
                    
                    print_rows(data, rows)
                    print()
        
            elif task == 3: # Encoding Categorical Data
                print('Tasks (Encoding Categorical Data)')
                print()
                print('1. Show Categorical columns')
                print('2. Perform One Hot Encoding')
                print('3. Show the dataset')
                print()

                while True:
                    resp = int(input("What do you want to do? (-1 to go back): "))
                    if resp not in [-1, 1, 2, 3]:
                        print('Enter a valid digit')
                    else:
                        break
                
                if resp == -1:
                    break

                print()

                if resp == 1:
                    print('Categorical columns')
                    print()
                    print(getCategoricalColumns(data))
                    print()
                
                elif resp == 2:
                    print('Columns:', ', '.join(data.columns))
                    print('Enter columns separated by space')
                    cols = input('Which columns to encode?: ').split()
                    data = oneHotEncoding(data, cols)
                    print()
            
                elif resp == 3:
                    while True:
                        rows = int(input("How many rows (>0) to print?: "))
                        if rows <= 0:
                            print(">0 rows")
                        else:
                            break
                    
                    print_rows(data, rows)
                    print()
                
            elif task == 4: # Feature scaling of the dataset
                print('Tasks (Feature scaling of the dataset)')
                print()
                print('1. Perform Normalization (MinMax Scaler)')
                print('2. Perform Standardization (Standard Scaler)')
                print('3. Show the dataset')
                print()

                while True:
                    resp = int(input("What do you want to do? (-1 to go back): "))
                    if resp not in [-1, 1, 2, 3]:
                        print('Enter a valid digit')
                    else:
                        break

                if resp == -1:
                    break

                print()

                if resp == 1:
                    print('Tasks (Normalization)')
                    print()
                    print('1. Normalize a specific column')
                    print('2. Normalize all columns')
                    print()

                    while True:
                        resp = int(input("What do you want to do? (-1 to go back): "))
                        if resp not in [-1, 1, 2]:
                            print('Enter a valid digit')
                        else:
                            break
                    
                    if resp == -1:
                        break

                    print()

                    if resp == 1:
                        print('Columns:', ', '.join(data.columns))
                        col = input('Which column?: ')
                        data = minMaxScalerColumn(data, col)
                        print()

                    elif resp == 2:
                        data = minMaxScaler(data)
                        print()
                    
                elif resp == 2:
                    print('Tasks (Standardization)')
                    print()
                    print('1. Standardize a specific column')
                    print('2. Standardize all columns')
                    print()

                    while True:
                        resp = int(input("What do you want to do? (-1 to go back): "))
                        if resp not in [-1, 1, 2]:
                            print('Enter a valid digit')
                        else:
                            break
                    
                    if resp == -1:
                        break

                    print()

                    if resp == 1:
                        print('Columns:', ', '.join(data.columns))
                        col = input('Which column?: ')
                        data = standardScalerColumn(data, col)
                        print()

                    elif resp == 2:
                        data = standardScaler(data)
                        print()
                    
                elif resp == 3:
                    while True:
                        rows = int(input("How many rows (>0) to print?: "))
                        if rows <= 0:
                            print(">0 rows")
                        else:
                            break
                    
                    print_rows(data, rows)
                    print()
                
            elif task == 5: # Download the dataset
                print('Tasks (Download the dataset)')
                print()
                print('1. Download the dataset')
                print()

                while True:
                    resp = int(input("What do you want to do? (-1 to go back): "))
                    if resp not in [-1, 1]:
                        print('Enter a valid digit')
                    else:
                        break
                
                if resp == -1:
                    break

                print()

                if resp == 1:
                    # Ask filename
                    filename = input('Filename: ')
                    # Save the dataset
                    data.to_csv(filename, index=False)
                    print('Dataset saved')
                    print()





