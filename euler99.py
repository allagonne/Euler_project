#!/usr/bin/env python3
#
#euler99 / Largest exponential

import time
import pandas as pd
import numpy as np

# Debut du decompte du temps
start_time = time.time()

## the trick is to take the logarithm of every number, and take the maximum
df = pd.read_csv('p099_base_exp.txt', sep=',', names = ['base', 'exp'], dtype = 'int')
df['log'] = np.log10(df['base']) * df['exp']
highest_log = df[df['log'] == df['log'].max()]
print(highest_log) ## add 1 since pandas dataframes start at index 0

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))