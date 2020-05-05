import os
def get_all_tomcats():
    list_of_config_files=[]
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file=="server.xml":
                list_of_config_files.append(os.path.join(r,each_file))
    return list_of_config_files             
def main():
    print("Finding list of timcats..")
    list_of_tomcats=get_all_tomcats()
    print(list_of_tomcats)
    return None
if __name__=="__main__":
    main()




