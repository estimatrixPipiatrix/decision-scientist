import subprocess
import pandas as pd
import numpy as np

subprocess.call("./retrieve_data.R",shell=True)
pay_gap = pd.read_csv('pay_gap.csv')

# all data is from 2012 so we drop the 'year' column
to_drop = np.array([0,1,17,18,19,20,21,22,23])
pay_gap = pay_gap.drop(pay_gap.columns[to_drop],axis=1)

# rename exp1 to pexp = potential experience
pay_gap = pay_gap.rename({'exp1':'pexp'},axis=1)
# convert ln(hourly wage) to hourly wage
pay_gap['lnw'] = np.exp(pay_gap['lnw'])
pay_gap = pay_gap.rename({'lnw':'hrwage'},axis=1)

# meanings of the other fields:
# hsd8   = whether max education was less than 8th grade
# hsd911 = same but between grades 9 and 11
# hsg    = high school graduation
# cg     = college graduate
# ad     = advanced degree
# mw     = person lives in the US midwest
# so     = lives in southwest
# we     = lives in west
pay_gap.to_csv('pay_gap_cleaned.csv',index=False)
