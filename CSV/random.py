import csv
import datetime
import random
import calendar

header=["id", "departure_time","arrival_time", "plane_id", "airline_id"]

def get_days_in_month(year, month):
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month

idd = 0
date= datetime.date(0,0,0)
dt= datetime.time(0,0,0)
at= datetime.time(0,0,0)
planeID=0
airline_id=0

with open("randomFlight.csv", 'w', newline="") as file:
     csvwriter = csv.writer(file) # 2. create a csvwriter object
     csvwriter.writerow(header) # 4. write the header

for i in range (10000):
    h = random.randint(0, 22)
    m = random.randint(0,60)
    s = random.randint(0,60)
    dt=(h,m,s)
    h = random.randint(h, 24)
    m = random.randint(0,60)
    s = random.randint(0,60)
    at=(h,m,s)
    
    y= random.randint(1999, 2015)
    m= random.randint(0,13)
    d= random.randint(1, get_days_in_month(y, m)    
    

    
    
    with open("randomFlight.csv", 'w', newline="") as file:
        csvwriter = csv.writer(file) # 2. create a csvwriter object
        row=[idd,dt,da,planeID,airline_id]
        csvwriter.writerows(row)
