base = {

'strains' : {1:"xxxxx",2:"yyyyyyy",3:"zzzzzzzz"},
'gene_edit' : [0,1], #0 is No , 1 is Yes   Please keep at 0 for now at all times. 
'spawn_type' : {1:"Barley",2:"Buckwheat",3:"Bulgur",4:"Oatmeal",5:"BierTreber"}, # bulgur is broken wheat
'spawn_weight' : 100 ,   # weight is in grams
'substrate_1' : {1:"Straw",2:"Rapstraw",3:"Hemp",4:"Sawdust",5:"Biertreber",6:"Grass", 7:"Vegiplants"} ,
'substrate_weight_1' : 900 ,#grams
'substrate_2' : {1:"Straw",2:"Rapstraw",3:"Hemp",4:"Sawdust",5:"Biertreber",6:"Grass", 7:"Vegiplants"}, 
'substrate_weight_2' : 900 ,#grams
'substrate_3' : {1:"Straw",2:"Rapstraw",3:"Hemp",4:"Sawdust",5:"Biertreber",6:"Grass", 7:"Vegiplants"} ,
'substrate_weight_3' : 900 ,#grams
'substrate_4' : {1:"Straw",2:"Rapstraw",3:"Hemp",4:"Sawdust",5:"Biertreber",6:"Grass", 7:"Vegiplants"} ,
'substrate_weight_4' : 900 ,#grams
'additive_1' : {1:"cellulose",2:"CaCO", 3:"CaSO4"},
'additive_weigth_1' : 0.03 ,# weight is in grams
'additive_2' : {1:"cellulose",2:"CaCO", 3:"CaSO4"},
'additive_weigth_2' : 0.03, # weight is in grams
'additive_3' : {1:"cellulose",2:"CaCO", 3:"CaSO4"},
'additive_weigth_3' : 0.03 ,# weight is in grams
'water_absorption' : 0.3 ,# is random number between LIMITS (0.3-0.6)
'bacteria' : [0,1], # 0 : No , 1 : Yes  Please keep at 0 for now at all times. 
'Temp_Growtent' : 25 ,# Celcius LIMITS (18-28)
'Humidity_Growtent' : 0.9 ,# this is relative humidity LIMITS (0.6-0.95)
'Time_Growtent' : 10, # days LIMITS (5-25)
'CO2_conc' : 200 ,# ppm in atmosphere. LIMITS (0-5000, steps of 500)
'Press_type' : {0:"Non-Pressed",1:"Cold-Pressed",2:"Hot-Pressed"},
'Temp_Press' : 40, # Celcius LIMITS (25-80)
'Force_Press' : 30 ,# kilo Newtons (kN) LIMITS (10-80)
'Time_Ovendrying' : 7 ,# hrs LIMITS (5-72, steps of 12)
'Temp_Ovendrying' : 70 , # Celcius LIMITS (70-90, steps of 5 degrees)
'Vacc_Overdrying' : -0.001 #atm LIMITS (0.001 - 0.1)

}
