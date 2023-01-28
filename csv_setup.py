import csv 
    
    
fields = ['PESSAT ID', 'Attitude Score', 'Motivational Score', 'Confidence Score', 'Resilience Score', 'Total Score'] 
filename = "university_records.csv" 

with open(filename, "w",newline="" ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)  



