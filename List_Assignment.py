
import logging

logging.basicConfig(filename="List_Assignment.log", level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')



class List:

    def pattern(self ,row ,item):
        try:
            logging.info("This will print the pattern with specified rows")
            for i in range(row):
                print(item *( i +1))
        except Exception as e:
            logging.error(e)
            print(e)

    def extract_list_entites(self ,l):
        try:
            logging.info("It will extract all the list entites")
            for i in l:
                if type(i )==list:
                    print(i)
        except Exception as e:
            logging.error(e)
            print(e)

    def extract_dict_entities(self ,l):
        try:
            logging.info("It will extract all the dictionary entites")
            for i in l:
                if type(i )==dict:
                    print(i)
        except Exception as e:
            logging.error(e)
            print(e)

    def extract_tuple_entities(self ,l):
        try:
            logging.info("It will extract all the tuples entites")
            for i in l:
                if type(i)==tuple:
                    print(i)
        except Exception as e:
            logging.error(e)
            print(e)
    def extract_numerical_entites(self ,ls):
        try:
            l=[]
            logging.info("It will extract all the numerical data in the entites")
            for i in ls:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                           l.append(j)
                if type(i)==dict:
                    for k,m in i.items ():
                        if type(k)==int:
                            l.append(k)
                        if type(m)==int:
                            l.append(m)
            return l
        except Exception as e:
            logging.error(e)
            return e
    def summation_dat(self,l):
        try:
            logging.info("It will give the summation of the numerical data")
            return sum(l)
        except Exception as e:
            logging.error(e)
            return e
    def extract_odd_value(self,l):
        try:
            l1=[]
            logging.info("It will extract odd values from the numerical data in the list")
            for i in l:
                if i%2!=0:
                    l1.append(i)
            return l1
        except Exception as e:
            logging.error(e)
            return e
    def extract_mul_entites(self,entites):
        try:
            ls=[]
            logging.info("It will extract all the entites multiplication in each entites")
            for i in entites:
                m1=1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            m1=m1*j
                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int:
                            m1=m1*k
                        if type(m) == int:
                            m1=m1*m
                ls.append(m1)
            return ls
        except Exception as e:
            logging.error(e)
            return e

s=List()
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


print(s.extract_mul_entites(l))