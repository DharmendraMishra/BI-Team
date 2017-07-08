import pandas as pd
import csv

#df = pd.read_csv('C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/tfcrLabelIoIds.csv',engine='python')

#df.drop_duplicates(['IOID'])

#df.to_csv('C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/tfcrLabelIoIds.csv',sep=",",index=False)

IN_File = 'C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/tfcrLabelIoIds.csv'
OUT_File = 'C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/Dup/tfcrLabelIoIds.csv'

def main():
    with open(IN_File, mode='r',newline='') as inf,open(OUT_File,mode='w',newline='') as outf:
        incsv, outcsv = csv.reader(inf),csv.writer(outf)
        IOID = set()
        for row in incsv:
            IOIDs = tuple(row[0:2])
            if IOIDs not in IOID:
                outcsv.writerow(row)
                IOID.add(IOIDs)

if __name__=="__main__":
    main()




