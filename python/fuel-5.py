import pandas as panda

df08 = panda.read_csv('../data/data_08_v4.csv')
df18 = panda.read_csv('../data/data_18_v4.csv')


def random_practice():
	counter = 0
	for f in df18['city_mpg']:
		counter += 1
		if f == 'Dec':
			debug = 1
	# 1 by 1
	df18_dec = df18[df18.city_mpg == 'Dec']
	df18_nov = df18[df18.city_mpg == 'Nov']
	df18_oct = df18[df18.city_mpg == 'Oct']
	df18_sep = df18[df18.city_mpg == 'Sep']
	
	def sanit():
		debug = 1
		if 'Dec' in df08[c] or 'Dec' in df18[c]:
			df08[c] = 12
			df18[c] = 12
		elif 'Nov' in df08[c] or 'Nov' in df18[c]:
			df08[c] = 11
			df18[c] = 11
		elif 'Oct' in df08[c] or 'Oct' in df18[c]:
			df08[c] = 10
			df18[c] = 10
		elif 'Sep' in df08[c] or 'Sep' in df18[c]:
			df08[c] = 9
			df18[c] = 9


def sanit2(e):
	if e == 'Dec':
		return 12
	elif e == 'Nov':
		return 11
	elif e == 'Oct':
		return 10
	elif e == 'Sep':
		return 9
	return e


# using .str.contains()
pattern = 'Dec|Nov|Oct|Sep'
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#evaluation-order-matters
# copies of slices from dataframes
# mask = "a copy of a slice from a dataframe"... I think.
# so these are all "masks"... I think.
df18_city_mpg_err = df18[df18.city_mpg.str.contains(pattern, regex=True)]
df18_hwy_mpg_err = df18[df18.hwy_mpg.str.contains(pattern, regex=True)]
df18_cmb_mpg_err = df18[df18.cmb_mpg.str.contains(pattern, regex=True)]

df1 = df18_city_mpg_err.copy()
df2 = df18_hwy_mpg_err.copy()
df3 = df18_cmb_mpg_err.copy()
df_masks = df1.append(df2).append(df3)

mpg_columns = ['city_mpg', 'hwy_mpg', 'cmb_mpg']
for c in mpg_columns:
	df1[c] = df1[c].apply(sanit2)
	df2[c] = df2[c].apply(sanit2)
	df3[c] = df3[c].apply(sanit2)

new_rows = df1.append(df2).append(df3)

# drop
df18.drop(index=df_masks.index, inplace=True)
# append
df18 = df18.append(new_rows, ignore_index=True)

for c in mpg_columns:
	df08[c] = df08[c].astype(float)
	df18[c] = df18[c].astype(float)

df08.greenhouse_gas_score = df08.greenhouse_gas_score.astype(int)

debug = 1










#
