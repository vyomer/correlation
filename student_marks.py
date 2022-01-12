import csv
import plotly.express as px
import numpy as np

def get_data_source(datapath):
    student_marks = []
    day_present = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            day_present.append(float(row["Days Present"]))
    return{"x": student_marks,"y": day_present}
def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between student marks vs days present is: ", correlation[0,1])
def setup():
    datapath = "Student Marks vs Days Present.csv"
    data_source = get_data_source(datapath)
    find_correlation(data_source)
setup()