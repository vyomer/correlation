import csv
import plotly.express as px
import numpy as np

def get_data_source(datapath):
    ice_sales = []
    temperature = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            ice_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
            temperature.append(float(row["Temperature"]))
    return{"x": temperature,"y": ice_sales}
def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between temperature vs ice cream is: ", correlation[0,1])
def setup():
    datapath = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source = get_data_source(datapath)
    find_correlation(data_source)
setup()
            

