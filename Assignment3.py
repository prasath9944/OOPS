
import logging
import socket
import datetime
logging.basicConfig(filename="Assignment3.log", level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
class Assignment3:
    def pattern(self,length):
        try:
            logging.info("It will try to print the pattern with specified length")
            i=0
            while i<=length:
                print('* '*(i+1))
                i=i+1
        except Exception as e:
            logging.error(e)
            print(e)

    def div_by_3(self,r1,r2,range_value):
        try:
            logging.info("It will display the list of items between the range")
            l=list(range(r1,r2+1,range_value))
            return l
        except Exception as e:
            logging.Exception()
            return e

    def even_no(self,n1,n2):
        try:
            logging.info("It will generate all the items that are divisible by 2")
            i=n1
            l=[]
            while i<=n2:
                if i%2==0:
                    l.append(i)
                i+=1
            return l
        except Exception as e:
            logging.error(e)
            return e

    def find_time_system(self):
        try:
            logging.info("It will generate current time of your system")
            print(datetime.datetime.today().time())
        except Exception as e:
            logging.error(e)
            print(e)

    def find_date_system(self):
        try:
            logging.info("It will generate current date in your system")
            print(datetime.datetime.today().date())
        except Exception as e:
            logging.error(e)
            print(e)

    def find_ip_address(self):
        try:
            logging.info("It will display the ip address of your local machine")
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer Name is:" + hostname)
            print("Your Computer IP Address is:" + IPAddr)
            logging.info("Your Computer Name is:" + hostname)
            logging.info("Your Computer IP Address is:" + IPAddr)
        except Exception as e:
            logging.error(e)
            print(e)
    def find_len_withoutbuildin(self,s):
        try:
            logging.info("It will find the length of the string"+s)
            i=0
            while i<len(s):
                i=i+1
            logging.info("The length of the string "+s+" is "+str(i))
            return i
        except Exception as e:
            logging.error(e)
            return e

    def index_primitive(self,l):
        try:
            logging.info("It will generater all the index of the data structure "+str(l))
            i=0
            l1=[]
            while i<len(l):
                l1.append(i)
                i=i+1
            logging.info("the indexes are "+str(l))
            return l
        except Exception as e:
            logging.error(e)
            return e

df=Assignment3()
print(df.index_primitive([1,2,3,4,5]))