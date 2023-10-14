import pandas as pd
import numpy as np

df_parts = pd.read_csv("part_data_2.csv",index_col='part_type')

df_parts['mu'] = (np.log(df_parts['loss_low'])+ \
                  np.log(df_parts['loss_high']))/2.0
df_parts['sigma'] = np.sqrt( \
    ((np.log(df_parts['loss_low'])-df_parts['mu'])**2.0 + \
     (np.log(df_parts['loss_high'])-df_parts['mu'])**2.0)/2.0
    )

num_runs = 10000
rec_nums  = np.arange(0,num_runs)
df_losses = pd.DataFrame(columns=df_parts.index, \
                         index = rec_nums)

for part in df_parts.index:
    df_losses[part] = \
        np.random.lognormal(df_parts.loc[part,'mu'], \
                            df_parts.loc[part,'sigma'], \
                            num_runs)
    df_parts.loc[part,'avg_loss'] = df_losses[part].mean()

print('avg expected yearly loss from combining parts A and B:')
print(df_parts.loc['A','avg_loss']+df_parts.loc['B','avg_loss'])
print('avg expected yearly loss from combining parts C and D:')
print(df_parts.loc['C','avg_loss']+df_parts.loc['D','avg_loss'])
