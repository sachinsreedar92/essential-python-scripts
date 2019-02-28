import csv

#Open file with "w"(write), the file will create automatically.
file = open("/home/sachinsridhar/Desktop/staah.txt", "w")
#Open CSV file to read CSV, note: reading and write file should be under "with"
with open('/home/sachinsridhar/Desktop/NewStaah.csv') as csvFile:
    #Read CSV
    readCsv = csv.reader(csvFile)
    for row in readCsv:
        #Get Values and manupilate in the file.write
        Id = row[0]
        Id1 = row[1]
        #Write CSV you need format it to string if the value is an int
        file.write("Insert into product.chmm_hotel_merchant_map (ID,HOTEL_ID, MERCHANT_ID, STATUS, CREATED_BY, UPDATED_BY) values (product.CHMM_HOTEL_MERCHANT_MAP_SEQ.nextval,"+str(Id1)+", 6219839, 'A', 1,1);""\n")
#You Must Close the FIle after writing it.
file.close()