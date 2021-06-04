

import pandas as pd

class dsv_database:
    """DSV Database

    This module provides a database which uses a dsv (delimiter separated file) better known as csv (comme separated file).
    You can explore and edit the database with Excel and Openoffice, and have simple database access to to it by python.
    The database features are delivered using a dataframe of the database. 
    Of course every user could also use the dataframe features to avoid using this module.
    Main purpose for this module should be to have easy database features without having knowledge of dataframes,
    and for expert features, also have the possibility to access the dataframe functions of the database easily.

    Author: Andreas Straka

    Attributes:
    df: The dataframe of the database.

    Methods:
    Open dsv file as database:
    dsv_database(path to dsv file)

    get (index): get dataset by index as list
    get_value (index, key): get dataset item by index (row) and key (column header)
    set_value (index, key, value): set dataset value
    new_dataset_by_dict (index, dict): set new dataset by passing a dict of key value pairs
    count (): get number of datasets
    keys (): get all database keys
    to_dsv (dsv_filename): write database to dsv file
    to_excel (xls_filename): write database to xlsx file
    """

    df = None
    _database_name = None
    _database_dsv = None
    _index_name = None
    _results = None
    _count = None

    def __init__(self, database_dsv):
        self._database_dsv = database_dsv

    def _open(self):
        try:
            self.df = pd.read_csv(self._database_dsv, sep=";", index_col=0)
        except:
            print("ERROR")
            exit
        self._index_name = self.df.index.name
        self.df[self._index_name]=self.df.index

    def _close(self):
        pass

    def query(self, query):
        self._open()
        self._index_df = self.df.loc[query]
        #print(self._index_name, query, ": ", self._index_df.description)
        self._close()
        return self._index_df.to_dict()

    def _action(self, action, table, where):
        pass

    def insert(self, table, fields):
        pass

    def update(self, table, fields, where):
        pass

    def get(self, query):
        return self.query(query)

    def get_value(self, query, name):
        return self.query(query)[name]

    def set_value(self, index_name, key, value):
        self.df.loc[index_name, key] = value
        self.save()

    def new_dataset_by_dict(self, index_name, dataset_dict):
        """ Create new dataset by dict. """
        for key in dict.keys():
            self.df.loc[index_name, key] = dataset_dict[key]
        print("SELF", self.df)
        self.save()

    def count(self):
        return self._count
    
    def keys(self):
        dict_keys = list(self.df.columns.values)
        #dict_keys.insert(0, self._index_name)
        return dict_keys

    def save(self):
        """ Save database """
        self.to_dsv(self._database_dsv)

    def to_dsv(self, dsv_file):
        new_csv_database = self.df.drop(self._index_name, axis=1)
        new_csv_database.to_csv(dsv_file, sep=";")

    def to_excel(self, xls_file):
        writer = pd.ExcelWriter(xls_file)
        new_csv_database = self.df.drop(self._index_name, axis=1)
        new_csv_database.to_excel(writer, sheet_name="Sheet1")
        writer.save()

        
    # future methods?
    def getBy(self, table, columns, where):
        pass

    def delete(self, table, where):
        pass

    def results(self):
        pass