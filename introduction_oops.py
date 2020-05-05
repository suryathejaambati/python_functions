'''
import os
def get_details_for_each_tomcat(script):
    global tcf,th
    tcf=script
    th=os.path.dirname(os.path.dirname(script))
    #print(f"The tomcat config file is: {tcf}\n The Tomcat home is :{th}")
    return None
def display_details():
    print(f"The tomcat config file is: {tcf}\n The Tomcat home is :{th}")
    return None
def main():
    get_details_for_each_tomcat("/home/ec2-user/sury/script1.py")
    get_details_for_each_tomcat("/home/ec2-user/sury/script2.py")
    display_details()
    return None
main()
'''
import os
class python:
    def get_details_for_each_tomcat(self,script):
        self.psf=script
        self.ph=os.path.dirname(os.path.dirname(script))
        return None
    def display_details(self):
        print(f"The python config file is:{self.psf}\n The python home is :{self.ph}")
        return None
def main():
        script1=python()
        script2=python()
        script1.get_details_for_each_tomcat("/home/ec2-user/sury/script1.py")
        #get_details_for_each_tomcat("script1","/home/ec2-user/sury/script1.py")
        script2.get_details_for_each_tomcat("/home/ec2-user/sury/script2.py")
        #get_details_for_each_tomcat("script2","/home/ec2-user/sury/script2.py")
        #print(script1.psf)
        #print(script2.ph)
        #print(script2.psf)
        script1.display_details()
        script2.display_details()
        return None
if __name__=="__main__":
    main()



