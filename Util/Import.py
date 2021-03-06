import pandas as pd
import json
import os


def load_new_file(filename):
    """
    Function for loading vectorised Twitter data (in data directory) into Pandas DataFrame
    :param filename: str. path to text file in json format
    :return: Pandas DataFrame
    """
    # try:
    #     if filename[-4:] != '.txt':
    #         raise TypeError('Use .txt file not .csv')
    # except:
    #     raise ValueError('Filename could not be processed. '
    #                      'Check it is a path to .txt file of Twitter data in json format')
    #
    # with open(filename, mode='r+t', encoding='utf-8') as f:
    #     data = json.load(f)

    data = pd.read_json(filename, orient='index')

    # data = pd.DataFrame(data['tweets'])
    # data['text'] = data['text'].map(lambda x: x.encode('unicode-escape'))
    # data['date'] = data['date'].map(lambda x: int(x/1000))
    data['date'] = pd.to_datetime(data['date'], unit='s')

    return data


def load_original_file(filename):
    """
    Function for loading Twitter (in Twitter directory) data into Pandas DataFrame
    :param filename: str. path to text file in json format
    :return: Pandas DataFrame
    """
    try:
        if filename[-4:] != '.txt':
            raise TypeError('Use .txt file not .csv')
    except:
        raise ValueError('Filename could not be processed. '
                         'Check it is a path to .txt file of Twitter data in json format')

    with open(filename, mode='r') as f:
        data = json.load(f)

    data = pd.DataFrame(data['tweets'])
    data['date'] = data['date'].map(lambda x: int(x/1000))
    data['date'] = pd.to_datetime(data['date'], unit='s')

    return data


def get_files(data_directory='./data'):
    """
    Function for getting list of text files
    :param data_directory: path to directory of data
    :return: list of directories
    """
    dir_list = []

    if not data_directory.endswith('/'):
        data_directory += '/'

    for file in os.listdir(data_directory):
        if file.endswith(".txt"):
            dir_list.append(data_directory+file)

    return dir_list
