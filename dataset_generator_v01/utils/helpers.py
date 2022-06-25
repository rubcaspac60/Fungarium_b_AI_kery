import random
import pandas as pd
import numpy as np
import datetime


def generate_additive_weight():
    pass

def generate_substrate_weight():
    pass
def validate_all_weights_sums():
    pass




def generate_record(base, algo_type='naive'):
    assert base, "No base provided"
    if algo_type=='naive':
        return {
        'strains' : random.choice(list(base['strains'].values())), 
        'gene_edit' : random.choice(base['gene_edit']), 
        'spawn_type' : random.choice(list(base['spawn_type'].values())), 
        'spawn_weight' : random.randint(50, 100), 
        
        'substrate_1' : random.choice(list(base['substrate_1'].values())), 
        'substrate_weight_1' : random.randint(50, 100), 
        'substrate_2' : random.choice(list(base['substrate_2'].values())), 
        'substrate_weight_2' : random.randint(200, 300), 
        'substrate_3' : random.choice(list(base['substrate_3'].values())), 
        'substrate_weight_3' : random.randint(50, 100),
        'substrate_4' : random.choice(list(base['substrate_4'].values())), 
        'substrate_weight_4' : random.randint(200, 300), 

        'additive_1' : random.choice(list(base['additive_1'].values())), 
        'additive_2' : random.choice(list(base['additive_2'].values())),
        'additive_3' : random.choice(list(base['additive_3'].values())),
        'water_absorption' : round(random.uniform(0.3,0.6),2), 

        'bacteria' : random.choice(base['bacteria']), 
        'Temp_Growtent' : random.randint(18,28), 
        'Humidity_Growtent' : random.uniform(0.6,0.95), 
        'Time_Growtent' : random.randint(5,25), 
        'CO2_conc' : random.choice([x for x in range(500,5000, 500)]), 
        'Press_type' : random.choice(list(base['Press_type'].values())), 
        'Temp_Press' : random.choice([x for x in range(70, 90, 5)]), 
        'Force_Press' : random.randint(10,80), 
        'Time_Ovendrying' : random.choice([x for x in range(5,72, 12)]), 
        'Temp_Ovendrying' : random.choice([x for x in range(70, 90, 5)]),
        'Vacc_Overdrying' : round(random.uniform(0.001, 0.1), 3)
        }
    elif algo_type=='expert':
        substrate_weights = generate_randoms_to_limit(4, 900)
        additive_weights =  generate_randoms_to_limit(3, 900)

        return {
        'strains' : random.choice(list(base['strains'].values())), 
        'gene_edit' : random.choice(base['gene_edit']), 
        'spawn_type' : random.choice(list(base['spawn_type'].values())), 
        'spawn_weight' : random.randint(50, 100), 
        
        'substrate_1' : random.choice(list(base['substrate_1'].values())), 
        'substrate_weight_1' : round(substrate_weights[0], 0), 
        'substrate_2' : random.choice(list(base['substrate_2'].values())), 
        'substrate_weight_2' : round(substrate_weights[1], 0), 
        'substrate_3' : random.choice(list(base['substrate_3'].values())), 
        'substrate_weight_3' : round(substrate_weights[2], 0),
        'substrate_4' : random.choice(list(base['substrate_4'].values())), 
        'substrate_weight_4' : round(substrate_weights[3], 0), 

        'additive_1' : random.choice(list(base['additive_1'].values())),
        'additive_weight_1' :  round(additive_weights[0], 0), 
        'additive_2' : random.choice(list(base['additive_2'].values())),
        'additive_weight_2' :  round(additive_weights[1], 0), 
        'additive_3' : random.choice(list(base['additive_3'].values())),
        'additive_weight_3' :  round(additive_weights[2], 0), 

        'water_absorption' : round(random.uniform(0.3,0.6),2), 

        'bacteria' : random.choice(base['bacteria']), 
        'Temp_Growtent' : random.randint(18,28), 
        'Humidity_Growtent' : round(random.uniform(0.6,0.95), 2), 
        'Time_Growtent' : random.randint(5,25), 
        'CO2_conc' : random.choice([x for x in range(500,5000, 500)]), 
        'Press_type' : random.choice(list(base['Press_type'].values())), 
        'Temp_Press' : random.choice([x for x in range(70, 90, 5)]), 
        'Force_Press' : random.randint(10,80), 
        'Time_Ovendrying' : random.choice([x for x in range(5,72, 12)]), 
        'Temp_Ovendrying' : random.choice([x for x in range(70, 90, 5)]),
        'Vacc_Overdrying' : round(random.uniform(0.001, 0.1), 3)
        }
    else:
        return {'Note':'No algo type provided'}


def generate_dataset(nrows:int, base:str, algo_type:str):
    day = datetime.datetime.today().strftime('%A, %B, %d _%M%S')
    
    if (nrows and base):
        df = pd.DataFrame([generate_record(base=base, algo_type=algo_type) for _ in range(nrows)])
        df.to_csv(f'GEN_{day}_{algo_type}_{nrows}.csv', index=False)
        df.describe().to_csv(f'STATS_{day}_{algo_type}_{nrows}.csv', index=False)
        print(f"Dataset CSV created with {nrows} rows and {algo_type} mode")

def generate_randoms_to_limit(n, total_sum):
#     nums = np.random.rand(n)
    nums = [round(x, 2) for x in np.random.rand(n)] 
    result = nums/np.sum(nums) *total_sum
    return result



def main():
    pass

if __name__ == '__main__':
    main()



