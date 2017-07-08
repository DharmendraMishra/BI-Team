import os
import math

os.chdir('C:/Users/Dharmendra.Mishra/Box Sync/Dharamendra Reports/Forecast Every Monday/Automation')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    f_title, f_year, f_month, f_date = file_name.split('-')

    new_name='{}-{}-{}-{}{}'.format(f_title, f_year, (int(f_month)), (int(f_date)+7), file_ext)
    os.renames(f,new_name)



