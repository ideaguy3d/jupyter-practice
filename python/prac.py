import pandas as panda

df08 = panda.read_csv('../data/data_08_v4.csv')
df18 = panda.read_csv('../data/data_18_v4.csv')

mpg_columns = ['city_mpg', 'hwy_mpg', 'cmb_mpg']
for c in mpg_columns:
    debug = 1
    if df08[c] == 'dec' or df18[c] == 'dec':
        df08[c] = 12; df18[c] = 12
    elif df08[c] == 'nov' or df18[c] == 'nov':
        df08[c] = 11; df18[c] = 11
    elif df08[c] == 'oct' or df18[c] == 'oct':
        df08[c] = 10; df18[c] = 10
    elif df08[c] == 'sep' or df18[c] == 'sep':
        df08[c] = 9; df18[c] = 9
    df08[c] = df08[c].astype(float)
    df18[c] = df18[c].astype(float)
    
s = ['city_mpg', 'hwy_mpg']

d = [
	{'city_mpg': 45, 'hwy_mpg': 99},
	{'city_mpg': 'dec', 'hwy_mpg': 29},
	{'city_mpg': 15, 'hwy_mpg': 'nov'}
]









#