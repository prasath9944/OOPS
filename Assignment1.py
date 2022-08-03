
import logging

logging.basicConfig(filename="String_Assignment.log", level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')

class Assignment1:

    def extract_str(self, data, start, end, step):
        try:
            logging.info("The Entered string %s with start index is %s, end index is %s and step size is %s", data,
                         start, end, end)
            msg = data[start: end: step]
            logging.info("The sliced index is %s", msg)
        except Exception as e:
            logging.error(e)
            msg = e
        return msg

    def reverse_str(self, data):
        try:
            logging.info("The string %s which was in try catch to execute the reverse", data)
            msg = data[::-1]
            logging.info("The reversed string is %s", msg)
        except Exception as e:
            logging.error(e)
            data = e
        return msg

    def split_str(self, data):
        try:
            logging.info("This string will get splitted after generating uppercase of the string")
            data = data.upper()
            logging.info("The Upper_case value of string is %s", data)
            data = data.split()
        except Exception as e:
            logging.exception()
            data = e
        return data

    def lower_str(self, data):
        try:
            logging.info("The string %s is converted into lower case", data)
            data = data.lower()
            logging.info('the lower case string is "%s"', data)
        except Exception as e:
            logging.error(e)
            data = e
        return data

    def captilize_str(self, data):
        try:
            logging.info("the string %s is Captilized", data)
            data = data.capitalize()
            logging.info("The string %s is the Captilized version", data)
        except Exception as e:
            logging.error(e)
            data = e
        return data

    def expand_str(self, data):
        try:
            logging.info("The string %s is expanded based on the tabs sequence characters", data)
            data = data.expandtabs()
            logging.info("The expanded string is %s", data)
        except Exception as e:
            logging.error(e)
            data = e
        return data

    def strip_str(self, data):
        try:
            logging.info("The string %s is striped", data)
            data1 = data.strip()
            data2 = data.lstrip()
            data3 = data.rstrip()
            print(data3)
            print(data2)
            logging.info("The string of left strip %s and right strip is %s and stripped string is %s", data2, data3,
                         data1)
        except Exception as e:
            logging.error(e)
            data1 = e
        return data1

    def replace_str(self, data, name, value):
        try:
            logging.info("The string %s is replaced with %s ", name, value)
            data = data.replace(name, value)
        except Exception as e:
            logging.exception()
            data = e
        return data

    def center_str(self, data, value):
        try:
            logging.info("The string %s will be centered with space of %s", data, value)
            data = data.center(value)
        except Exception as e:
            logging.error(e)
            data = e
        return data


