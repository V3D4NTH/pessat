import csv 
import bars
    

filename = "university_records.csv" 

def csv_writer(filename):
    with open(filename, "a",newline = "") as csvfile:
        csvwriter = csv.writer(csvfile)
        rows = [bars.srn ,bars.Attitude_marks, bars.Motivation_marks ,bars.Confidence_marks , bars.Resilience_marks , bars.Total_marks]
        # writing the data rows bars.Motivation_marks
        csvwriter.writerow(rows)  