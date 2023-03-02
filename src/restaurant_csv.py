import csv
import pandas as pd
import os.path

class RestaurantCsv(object):
    FILE_NAME = "restaurant.csv"
    COLUMNS   = ["Name", "Count"]
    
    def __init__(self, rank = 1):
        if not os.path.isfile(self.FILE_NAME):
            self.df = pd.DataFrame(columns=self.COLUMNS)
            self.df.to_csv(self.FILE_NAME, index=False)
        else:
            self.df = pd.read_csv(self.FILE_NAME)
        
        self.rank = rank

    def write(self, restaurant):
        if restaurant in self.df["Name"].values:
            self.df.loc[self.df["Name"] == restaurant, "Count"] += 1
            self.df.to_csv(self.FILE_NAME, index=False)
        else:
            self.df = pd.DataFrame({'Name': [restaurant], 'Count': [1]})
            self.df.to_csv(self.FILE_NAME, index=False, header=False, mode='a')
    
    def read(self):
        df = pd.read_csv(self.FILE_NAME)
        print(df)
    
    def exists(self):
        if not self.df.empty:
            return True
        else:
            return False

    def get_restaurant_by_rank(self):
        try:
            sorted_count_desc = self.df.sort_values('Count', ascending=False)
            
            return sorted_count_desc.iloc[self.rank - 1]['Name']
        except IndexError:
            return False