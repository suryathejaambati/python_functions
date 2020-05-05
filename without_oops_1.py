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
    #print(list_of_tomcats)
    cnt=1
    for each_config_file in list_of_tomcats:
        print(f"The info for tomcat:{cnt}")
        print(f"The tomcat home is :", os.path.dirname(os.path.dirname(each_config_file)))
        print(f"The tomcat config file is :",each_config_file)
        cnt=cnt+1
    return None
if __name__=="__main__":
    main()

