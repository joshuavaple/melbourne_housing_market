import os
import pathlib
import sys 

PACKAGE_PARENT = pathlib.Path.cwd() 
SRC_DIR = os.path.join(PACKAGE_PARENT, 'src')
sys.path.append(SRC_DIR)

RAW_DATA_LOC = r'..\data\01_raw'
CSV_FILE_NAME = 'Melbourne_housing_FULL.csv'
CSV_FILE_PATH = os.path.join(RAW_DATA_LOC, CSV_FILE_NAME)

if __name__ == '__main__':
    print(PACKAGE_PARENT)
    print(SRC_DIR)
    print(CSV_FILE_PATH)
