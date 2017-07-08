import pandas
import glob
import os
import xlsxwriter
import openpyxl



def concatenate(indir="C:\\Users\\Dharmendra.Mishra\\Box Sync\\Dharamendra Reports\\UK_EU Weekly", outfile = "C:\\Users\\Dharmendra.Mishra\\Box Sync\\Dharamendra Reports\\UK_EU Weekly\\EU_UK Weekly(today).xlsx" ):
    os.chdir(indir)
    fileList = glob.glob("*.xlsx")

    dfList = []
    print(dfList)
    header = ["CM", "AM", "Client", "IO", "Placement", "Start Date", "End Date","Booked".format('$#,##0'), "RR", "P Pacing%",
                "C Pacing%", "Imp AF", "Client Goal", "eCPA", "Last 7 day eCPA", "Market Share", "CTR", "Min Cost",
                "Metric", "Sub Region", "Creative"]
   # format1 = ('${:2f}'.format("Booked"))

    for filename in fileList:
        print(filename)
        df = pandas.read_excel(filename,header= 0, sheetname="Links", skiprows=1)
        dfList.append(df)
    concatDf = pandas.concat(dfList, axis=0)


    concatDf.to_excel(outfile, columns = header, index = None, sheet_name ="Links", engine='xlsxwriter')




if __name__ == '__main__':
    concatenate("C:\\Users\\Dharmendra.Mishra\\Box Sync\\Dharamendra Reports\\UK_EU Weekly",
                "C:\\Users\\Dharmendra.Mishra\\Box Sync\\Dharamendra Reports\\UK_EU Weekly\\EU_UK Weekly(today).xlsx")