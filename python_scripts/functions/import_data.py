import pandas as pd

def import_data():
    #set file path
    file_path = 'C:\Users\zionj\OneDrive\Documents\CS5290\project\raw_data\data\training_set_rel3.tsv'

    dataset_df = pd.read_csv(file_path)