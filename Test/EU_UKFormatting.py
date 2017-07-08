import xlrd
import pandas as pd
df = pd.read_excel('C:/Users/Dharmendra.Mishra/Box Sync/Dharamendra Reports/UK_EU Weekly/EU_UK Weekly(today).xlsx',sheetname='Links')
df_write = df.to_excel('C:/Users/Dharmendra.Mishra/Box Sync/Dharamendra Reports/UK_EU Weekly/EU_UK Weekly(today)New.xlsx',index = None)
#writer = pd.ExcelWriter('C:/Users/Dharmendra.Mishra/Box Sync/Dharamendra Reports/UK_EU Weekly/EU_UK Weekly(today)New.xlsx', engine='xlsxwriter')
#df_write.to_excel(df_write,index=False, Sheet_Name = 'Links')

workbook = df_write.book
worksheet = df_write.sheets['Links']

money_fmt = workbook.add_format({'num_format':'$#,##0' ,  'font_name':'Batang' })
Percent_fmt = workbook.add_format({'num_format':'%0.00' ,  'font_name':'Batang' })

worksheet.set_column('H:I',25,money_fmt)

df_write.save()

#format = df.add_format()
#format.set_bg_color('Blue')

#df_write = df.to_excel('C:/Users/Dharmendra.Mishra/Box Sync/Dharamendra Reports/UK_EU Weekly/EU_UK Weekly(today)New.xlsx',index = None)

