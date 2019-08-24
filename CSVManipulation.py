import csv
with open ('/Users/sachinsreedar92/Downloads/medikoe.csv') as csvFile:
    tripIds = []
    readCsv = csv.reader(csvFile, delimiter=',')
    for row in readCsv:
        tripId = row[0]
        if tripId != "":
            tripIds.append(tripId)
    dup_list = tripIds


def remove_duplicates(dup_list):
    withoutDup = []
    for ele in dup_list:
        if ele not in withoutDup:
            withoutDup.append(ele)
    return withoutDup

print(len(dup_list))
print(dup_list)
