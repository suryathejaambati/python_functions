'''
import os

req_path=input("Enter path to change the working dir : ")
print("The current working dir is: ",os.getcwd())
try:
    os.chdir(req_path)
    print(" Now your new working dir is: ",os.getcwd())
except FileNotFoundError:
    print("Give path is not valid path. so can't change the working directory")
except NotADirectoryError:
    print("Given path is file path. so can't change the working directory")
except PermissionError:
    print("Sorry you don't have access for the given path. so can't change the working directory")
except Exception as e:
    print(e)

'''

import os
def main():
    req_path=input("Enter path to change the working dir : ")
    print("The current working dir is: ",os.getcwd())
    try:
        os.chdir(req_path)
        print(" Now your new working dir is: ",os.getcwd())
    except FileNotFoundError:
        print("Give path is not valid path. so can't change the working directory")
    except NotADirectoryError:
        print("Given path is file path. so can't change the working directory")
    except PermissionError:
        print("Sorry you don't have access for the given path. so can't change the working directory")
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()

