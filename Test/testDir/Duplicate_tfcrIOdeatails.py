import pandas as pd
import csv

#df = pd.read_csv('C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/tfcrLabelIoIds.csv',engine='python')

#df.drop_duplicates(['IOID'])

#df.to_csv('C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/tfcrLabelIoIds.csv',sep=",",index=False)

IN_File = 'C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/tfcrIoDetails.csv'
OUT_File = 'C:/Users/Dharmendra.Mishra/Desktop/Autoaddition/Dup/tfcrIoDetails.csv'

def main():
    with open(IN_File, mode='r',newline='') as inf,open(OUT_File,mode='w',newline='') as outf:
        incsv, outcsv = csv.reader(inf),csv.writer(outf)
        TFIOID = set()
        for row in incsv:
            TFIOIDs = tuple(row[0:2])
            if TFIOIDs not in TFIOID:
                outcsv.writerow(row)
                TFIOID.add(TFIOIDs)

if __name__=="__main__":
    main()




