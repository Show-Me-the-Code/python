"""
previous issue : prints only month at the moment because you have mentioned only %B to extrac the year we need to use %Y along with %B(i.e month)  
"""

from datetime import datetime 

date = "29-01-2025"

date_obj= datetime.strptime(date, "%d-%m-%Y")   
print(date_obj.strftime("%B %Y"))


#  mention that if you’re looping through dates from a CSV, then you just need to apply the format like:

# data_obj = datetime.strptime(date,"%d-%m-%Y")
# print(data_obj.strftime(%B %Y)) %B for month and %Y for year 