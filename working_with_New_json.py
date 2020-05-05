import json
my_dict={'Name':'Surya','skills':['python','AWS','DevOps']}
req_file="/home/ec2-user/new.json"
fo=open(req_file,"w")
json.dump(my_dict,fo,indent=4)
fo.close()


