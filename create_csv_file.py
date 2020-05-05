'''
fo=open(req_file,'r')
csv_reader=csv.reader(fo,delimeter="|")
for each in csv_reader:
    print(each)
fo.close()
'''

'''
csv_writer.writerow(['S_No','Name','Age'])
csv_writer.writerow([1,"suryatheja",28])
csv_writer.writerow([2,'Chandrsmitha',25])
'''

'''
import csv
req_file="demo.csv"
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo)
my_data=(['S_No','Name','Age'],[1,"suryatheja",28],[2,'Chandrsmitha',24])
csv_writer.writerows(my_data)
fo.close()
'''
'''

import csv
req_file="demo.csv"
fo=open(req_file,'r')
content=csv.reader(fo,delimiter="|")
for each in content:
    print(each)
#data=fo.read()
#csv_reader=csv.reader(fo)
#print(csv_reader)
#print(data)
fo.close()

'''


