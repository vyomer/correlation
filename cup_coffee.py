import csv
import plotly.express as px
import numpy as np

def get_data_source(datapath):
    cup_coffee = []
    hours_of_sleep = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            cup_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))
    return{"x": cup_coffee,"y": hours_of_sleep}
def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between cup of coffe vs hours of sleep is: ", correlation[0,1])
def setup():
    datapath = "cups of coffee vs hours of sleep.csv"
    data_source = get_data_source(datapath)
    find_correlation(data_source)
setup()