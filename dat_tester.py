
import pandas as pd

# Dat file reader
# Assumptions
# 1. Every dat's first row is United States
# 2. The column format of all dats is the same.
def read_dat_file(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
        lines[0] = lines[0].replace("United States", "United_States")
        values = lines[0].split(r' ')
        values = [x for x in values if x != '']
        idxs = [lines[0].index(v) for v in values]
        # print(values)
        # print(idxs)
        # print(values[-1])

        mHHs = []
        states = []
        countys = []
        postals = []
        names = []

        # print('Median HHincomes')
        for line in lines:
            if line.strip() != '':
                mHHs.append(line[idxs[-11]:idxs[-10]].strip())
                postals.append(line[idxs[-1]:].strip())
                names.append(line[idxs[-2]:idxs[-1]].strip())
                states.append(line[0:2].strip())
                countys.append(line[3:6].strip())
        
        df = pd.DataFrame({
                'State FIPS Code': states, 
                'County FIPS Code': countys, 
                'Postal Code': postals,
                'Name': names,
                'Median Household Income': mHHs}
            )

        # print(df.head())
        return df

        



        
read_dat_file('est1997all.dat')