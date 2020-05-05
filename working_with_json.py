import json
req_file="/home/ec2-user/my.json"
fo=open(req_file,"r")
#print(type(fo.read()))
print(json.load(fo))
#print(json.load(fo).get("Eternal Flame"))
fo.close()
