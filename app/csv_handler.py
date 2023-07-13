import pandas as pd
import logging
import os

async def store_csv(file, filename):
    bytes_data = await file.read()

    with open(f'./uploads/{filename}', 'wb') as binary_file: 
        binary_file.write(bytes_data)
    
    logging.info(f'File {filename} uploaded.')


def get_head(filename):
    dataframe = pd.read_csv(f'./uploads/{filename}')
    return dataframe.columns.values.tolist()


def remove_csv(filename):
    os.remove(f'./uploads/{filename}')
    logging.info(f'File {filename} removed.')


def get_csv(filename, filter, sort):
    dataframe = pd.read_csv(f'./uploads/{filename}')

    if filter:
        dataframe = dataframe.filter(items=filter)
    if sort:
        dataframe = dataframe.sort_values(by=sort)
    
    return dataframe.to_csv(index=False)