"""DSV Database

This module provides a database which uses a dsv (delimiter separated file) better known as csv (comme separated file).
You can explore and edit the database with Excel and Openoffice, and have simple database access to to it by python.
The database features are delivered using a dataframe of the database. 
Of course every user could also use the dataframe features to avoid using this module.
Main purpose for this module should be to have easy database features without having knowledge of dataframes,
and for expert features, also have the possibility to access the dataframe functions of the database easily.

Author: Andreas Straka
"""

from dsv_database import dsv_database

DB = dsv_database("C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database.csv")

# get all dataset values as dict
result = DB.get("Konzept 306")
print("Torsional stiffness: ", result['c_T'])

# get specific dataset value
c_T = DB.get_value("Konzept 306", "c_T")
print("Torsional stiffness: ", c_T)

# set specific datatset value
DB.set_value('Konzept 306', 'c_T', 500.0)

c_T = DB.get_value("Konzept 306", "c_T")
print("Torsional stiffness changed: ", c_T)

# get list of all available values
print("Available values: ", ', '.join(DB.get("Konzept 306").keys()))
print("Available values: ", DB.keys())

# iterate dataset
var = DB.get("Konzept 304")
for i in DB.keys():
    print(i, var[i])

# write databse to dsv
DB.to_dsv("C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database_new.csv")

# write datavbase to excel
DB.to_excel("C:/Users/Andreas/Documents/GitHub/cae-master/projects/03_simple_database/database_new.xlsx")

# direct access to dataframe
print("c_T describe:\n", DB.df.describe())

# new dataset by setting unknown index
DB.set_value("Konzept 401", "c_T", 555.0)

# new dataset key by setting value to key
DB.set_value("Konzept 401", "label", "new base")

# new dataset by setting multiple keys by dict
data = { 'variant_base': 'Konzept 400', 'c_T': 43000.0, 'label': 'test' }
#DB.new_dataset_by_dict('Konzept 400', data)