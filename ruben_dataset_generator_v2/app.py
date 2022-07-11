import argparse
from constants import settings
from utils import helpers



def mains():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--countRows', type=int, required=True)
    parser.add_argument('-a', '--algoType', type=str, required=True)

    args = parser.parse_args()
    num_rows_to_generate = args.countRows
    algo_type = args.algoType

    generics = helpers.generate_generic_dataset(num_rows_to_generate, settings.base, algo_type)
    # bias_physical = helpers.create_bias(generics)
    naive_physical = helpers.generate_physicals_dataset(num_rows_to_generate, settings.base, algo_type)







if __name__ == '__main__':
    mains()




    
