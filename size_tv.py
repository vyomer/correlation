import csv
import plotly.express as px
import numpy as np

def get_data_source(datapath):
    size_of_tv = []
    Average_time_spent = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            Average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x": Average_time_spent,"y": size_of_tv}
def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between size of tv vs average time spent on tv is: ", correlation[0,1])
def setup():
    datapath = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    data_source = get_data_source(datapath)
    find_correlation(data_source)
setup()
            

