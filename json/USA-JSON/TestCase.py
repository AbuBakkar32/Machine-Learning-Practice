import unittest
from CompareTwoKey import CompareTwoDict


# This class is a subclass of the unittest.TestCase class
class TestCompareTwoDict(unittest.TestCase):
    def setUp(self):
        """
        The function takes two dictionaries and compares them.
        """
        self.data1 = {
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
        self.data2 = {
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
            "targetsubid": '000',
            "transacttime": None
        }
        self.obj = CompareTwoDict(self.data1, self.data2)

    def test_converDatatypeToString(self):
        """
        It converts all the data types in a dictionary to strings
        """
        new_data1 = {
            "string": "BATS",
            "noneType": None,
            "int": 148,
            "float": 11.0,
            "list": [1, 2, 3],
            "tuple": (1, 2, 3),
            "dict": {"a": 1, "b": 2, "c": 3},
            "set": {1, 2, 3},
            "bool": True,
        }
        convertedData1 = self.obj.convertDataTypeToString(new_data1)
        self.assertNotEqual(convertedData1, new_data1)

    def test_converDatatypeToString_keyWhitespace(self):
        """
        It tests the convertDataTypeToString function.
        """
        new_data2 = {
            "string ": "None",
        }
        convertedData2 = self.obj.convertDataTypeToString(new_data2)
        self.assertNotEqual(convertedData2, new_data2)

    def test_compareTwoKey_sameValue(self):
        """
        It compares two dictionaries and returns a list of keys that have different values or equal.
        """
        output_dict1 = self.obj.convertDataTypeToString(self.data1)
        output_dict2 = self.obj.convertDataTypeToString(self.data1)
        self.assertEqual(self.obj.compareTwoKey(output_dict1, output_dict2), [])

    def test_compareTwoKey_differentValue(self):
        """
        It compares two keys and returns the list of keys that are different or same.
        """
        output_dict1 = self.obj.convertDataTypeToString(self.data1)
        output_dict2 = self.obj.convertDataTypeToString(self.data2)
        keyList = ['clordid', 'operatorid', 'sequencenumber', 'targetsubid']
        self.assertEqual(self.obj.compareTwoKey(output_dict1, output_dict2), keyList)

    def test_TowDifferentList(self):
        """
        It compares two lists and returns the difference between them or equal between them.
        """
        list1 = []
        dict1 = self.obj.convertDataTypeToString(self.data1)
        dict2 = self.obj.convertDataTypeToString(self.data2)
        for key, value in dict1.items():
            if dict1[key] not in dict2[key]:
                list1.append(key)
        list2 = self.obj.compareTwoKey(dict1, dict2)
        self.assertEqual(list1, list2)
        self.assertTrue(list1 == list2)
        self.assertAlmostEqual(list1, list2)
        self.assertListEqual(list1, list2)


# A way to run the unittest.main() function.
if __name__ == '__main__':
    unittest.main()
