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

df_losses_copy = df_losses.copy()

df_losses_copy['A_plus_B'] = \
    df_parts.loc['A','prob_fail']*df_losses['A'] + \
    df_parts.loc['B','prob_fail']*df_losses['B']
df_losses_copy['C_plus_D'] = \
    df_parts.loc['C','prob_fail']*df_losses['C'] + \
    df_parts.loc['D','prob_fail']*df_losses['D']

AEL_AB = df_losses_copy['A_plus_B'].mean()
AEL_CD = df_losses_copy['C_plus_D'].mean()

print('avg expected yearly loss from A plus B:', \
    np.round(AEL_AB,2))
print('avg expected yearly loss from C plus D:', \
    np.round(AEL_CD,2))
