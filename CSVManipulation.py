import csv
with open ('/Users/sachinsreedar92/Downloads/medikoe.csv') as csvFile:
    column = []
    readCsv = csv.reader(csvFile, delimiter=',')
    for row in readCsv:
        data = row[0]
        if data != "":
            column.append(data)
    dup_list = column


def remove_duplicates(dup_list):
    withoutDup = []
    for ele in dup_list:
        if ele not in withoutDup:
            withoutDup.append(ele)
    return withoutDup

print(len(dup_list))
print(remove_duplicates(dup_list))
