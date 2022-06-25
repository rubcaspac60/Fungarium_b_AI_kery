import argparse
import pandas as pd
from constants import settings
from utils import helpers



def mains():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--countRows', type=int, required=True)
    parser.add_argument('-a', '--algoType', type=str, required=True)

    args = parser.parse_args()
    num_rows_to_generate = args.countRows
    algo_type = args.algoType

    helpers.generate_dataset(num_rows_to_generate, settings.base, algo_type)






if __name__ == '__main__':
    mains()




    
