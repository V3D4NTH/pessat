import csv 
import bars
    

fields = ['PESSAT ID', 'Attitude Score', 'Motivational Score', 'Confidence Score', 'Resilience Score', 'Total Score'] 
filename = "university_records.csv" 


def csv_reader(filename , fields):
        
    with open(filename,"a+") as csvfile:
        csvreader = csvfile.readlines()
        l = []
        print(csvreader)
        # for rec in csvreader:
        #     #l.append(rec)
        #     print(rec)
        # print(l)
        # print(l[0])
        # print(type(l[0]))
        # print(fields
        if l == []:
            return False
        elif l[0] != fields:
            return False
        else:
            return True

def csv_writer(fields):
    # writing to csv file 
    x = csv_reader(filename, fields)
    if x==True:
        with open(filename, "a" ) as csvfile:
            csvwriter = csv.writer(csvfile)
            rows = [bars.srn ,bars.Attitude_marks, bars.Motivation_marks ,bars.Confidence_marks , bars.Resilience_marks , bars.Total_marks]
            # writing the data rows bars.Motivation_marks
            csvwriter.writerow(rows)  
    else:
        with open(filename, "a" ) as csvfile:
            csvwriter = csv.writer(csvfile)
                    
            # writing the fields 
            csvwriter.writerow(fields) 
            rows = [bars.srn ,bars.Attitude_marks, bars.Motivation_marks ,bars.Confidence_marks , bars.Resilience_marks , bars.Total_marks]
            # writing the data rows bars.Motivation_marks
            csvwriter.writerow(rows)   