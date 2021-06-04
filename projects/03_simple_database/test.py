import os
import sys
import matplotlib.pyplot as plt

import pandas as pd

cwd = os.getcwd()
print(cwd)

#read database as csv
database = pd.read_csv("C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database.csv", sep=";", index_col="variant")

print(database)

# write database again
database.loc["Konzept 304", "description"] =  "base_variant"
database.to_csv("C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database_new.csv", sep=";")

# write database in excel file
writer = pd.ExcelWriter('C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database.xlsx')
database.to_excel(writer, sheet_name="VARIANTS")
writer.save()

# read excel database
database_excel = pd.read_excel('C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database.xlsx', index_col='variant')
print(database_excel)

#get variant data
variant="Konzept 305"
variant_df = database.loc[variant]
print("Variant ", variant, ": ", variant_df.description)
print("Torsional Stiffness: ", variant_df.c_T)
print("Mass: ", variant_df.m_rk_modal)

#plot all over variants
if (1 == 0):
    database.plot()
    plt.show()

#plot stiffness over variants
if (1 == 0):
    db_c = database[["c_T", "c_LB"]]
    db_c.plot(kind="bar")
    plt.tight_layout()
    plt.show()

