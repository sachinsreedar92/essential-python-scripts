import csv
with open ('/home/sachinsridhar/Desktop/hong.csv') as csvFile:
    tripIds = []
    readCsv = csv.reader(csvFile , delimiter=',')
    for row in readCsv:
        tripId = row[0]
        tripIds.append(tripId)
    print(len(tripIds))
    print(tripIds)