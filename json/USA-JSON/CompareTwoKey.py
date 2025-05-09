from termcolor import colored

"""
Here are some assumptions to consider:
* All of the data will be presented as strings.  Do not attempt to interpret the data any further (integers, floats, Booleans, etc.).
* The output of your script should only present keys whose values do not match.  Show the key, the expected value, and the actual value in a format suitable for debugging.
* Consider the case where the messages have different or missing keys.
"""


# It takes two dictionaries and converts them into a single dictionary to Compare tow Dict.
class CompareTwoDict:
    # Initialize the class
    def __init__(self, dict1, dict2):
        """
        The function takes two dictionaries as arguments and assigns them to the instance variables dict1 and dict2.

        :param dict1: The first dictionary to be compared
        :param dict2: The dictionary to be merged into dict1
        """
        self.dict1 = dict1
        self.dict2 = dict2

    def convertDataTypeToString(self, data):
        """
        It takes a dictionary as an argument and returns a dictionary with all the values converted to strings

        :param data: The data to be converted
        :return: a dictionary with the key and value being the same.
        """
        try:
            data = {k.translate({32: None}): str(v) for k, v in data.items()}
        except ValueError:
            raise ValueError("Value is not a number or integer or boolean")
        return data

    def outputDict(self, data):
        """
        This function takes a dictionary as an argument and prints the key and value pairs in a table format

        :param data: The dictionary to be printed
        """
        print("+-------------------------+-----------------------------+")
        print("|Key                      |            Value            |")
        print("+-------------------------+-----------------------------+")
        for key, value in data.items():
            print(f"|{key:25}|{data[key]:^29}|")
        print("+-------------------------+-----------------------------+")

    def compareTwoKey(self, dict1, dict2):
        """
        This function takes two dictionaries as input and compares the keys and values of the two dictionaries.

        If the key and value of the first dictionary is present in the second dictionary, then it will return a list of key

        :param dict1: The expected dictionary
        :param dict2: The dictionary that is returned from the function
        """
        # call the outputDict method
        finalDict = []
        for key, value in dict1.items():
            if dict1[key] not in dict2[key]:
                finalDict.append(key)
        return finalDict

    def result(self, dict1, dict2):
        """
        It compares two dictionaries and prints the output in a table format

        :param dict1: The expected output
        :param dict2: The actual/returned message
        """
        print(colored("'Expected' Message:", attrs=['blink', 'bold']))
        self.outputDict(dict1)
        print(colored("\n\n\n'Actual/Returned' Message:", attrs=['blink', 'bold']))
        self.outputDict(dict2)
        print(colored("\n\n\n'Output Message whose values do not match:", attrs=['blink', 'bold']))
        # Printing the output in a table format.
        print("+-------------------------+---------------------------------------------------------------------------+")
        print("|Key                      |            Expected Value            |            Actual Value            |")
        print("+-------------------------+---------------------------------------------------------------------------+")
        compareKey = self.compareTwoKey(dict1, dict2)
        for key in compareKey:
            print(f"|{key:25}|{dict1[key]:^38}|{dict2[key]:^36}|")
        print("+-------------------------+---------------------------------------------------------------------------+")

    def compareDictonary(self):
        """
        It compares two dictionaries and returns the difference between them.
        :return: the output of the result function.
        """
        output_dict1 = self.convertDataTypeToString(self.dict1)
        output_dict2 = self.convertDataTypeToString(self.dict2)
        return self.result(output_dict1, output_dict2)


# This is the main function. It is executed when the program is run.
if __name__ == "__main__":
    # Creating two dictionaries with dammy data
    data1 = {
        "account": "BATS",
        "clordid": None,
        "custorderhandlinginst": 'Y',
        "executionid": 'S100000FDR',
        "executiontype": 4,
        "lastshares": 0,
        "operatorid": 148,
        "orderid": '172H1JDVCPVW',
        "orderquantity": 10,
        "price": 11.0,
        "securitytype": 'FUT',
        "sequencenumber": 0,
        "side": 2,
        "symbol": '000001',
        "targetcomputerid": 'FOOA',
        "targetsubid": "''",
        "transacttime": None
    }
    data2 = {
        "account": "BATS",
        "clordid": "restingSellOrder_GVB",
        "custorderhandlinginst": 'Y',
        "executionid": 'S100000FDR',
        "executiontype": 4,
        "lastshares": 0,
        "operatorid": 'CFE',
        "orderid": '172H1JDVCPVW',
        "orderquantity": 10,
        "price": 11.0,
        "securitytype": 'FUT',
        "sequencenumber": 1822,
        "side": 2,
        "symbol": '000001',
        "targetcomputerid": 'FOOA',
        "targetsubid": '0001',
        "transacttime": None
    }
    obj = CompareTwoDict(data1, data2)
    obj.compareDictonary()
