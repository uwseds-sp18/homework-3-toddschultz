"""
Homework 3
Todd Schultz
"""
import unittest
import os
import homework3 as hw3

pathname = '.'


class HW3_UnitTests(unittest.TestCase):

    def test_number_rows(self):
        # test for more than 10 rows in the dataframe
        dftest = hw3.create_dataframe(pathname)
        self.assertTrue(dftest.shape[0] >= 10)
        
    def test_column_names(self):
        # test for exactly and only the column names video_id, category_id, 
        # and language
        dftest = hw3.create_dataframe(pathname)
        
        # if we test for the number of columns to match the number of exact column
        # names, and that we have at least one column of each of the required names
        # then we can conclude that we have only the exact columns required
        passtest = True
        knownnames = ('video_id', 'category_id', 'language')
        passtest = passtest & (dftest.shape[1] == len(knownnames))
        col_names = dftest.columns
        
        def is_valid_column(cnames, testcname):
            isvalid = False
            for x in range(0, len(cnames)):
                isvalid = isvalid | (cnames[x] == testcname)
            return isvalid
        
        for y in range(0, len(knownnames)):
            passtest = passtest & (is_valid_column(col_names, knownnames[y]))
        
        self.assertTrue(passtest)
        
    def test_key_columns(self):
        # test for columns make a key
        dftest = hw3.create_dataframe(pathname)
        teststr = dftest['video_id'].map(str) + dftest['language']
        self.assertTrue(teststr.nunique() == dftest.shape[0])

    def test_invalid_path(self):
        # test for ValueError for invalid path test path
        invalidpath = os.path.join('.', 'no', 'path', 'should', 'be', 'named', 'this')
        with self.assertRaises(ValueError):
            hw3.create_dataframe(invalidpath)


if __name__ == '__main__':
    unittest.main()
