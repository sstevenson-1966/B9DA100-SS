# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:29:29 2019

@author: sebst
"""

import unittest

from CA04_1743573_SebStevenson import Bills

class TestBillManagement(unittest.TestCase):

    
    def test_read_bills(self):
        self.testbills = Bills()
        self.testdf = self.testbills.read_bills()
        self.assertNotEqual(len(self.testbills.read_bills()), 0)
        
    def test_provider(self):
        self.testbills = Bills()
        self.testdf = self.testbills.read_bills()
        self.assertTrue(self.testbills.valid_provider(self.testdf, "Energia"))
        self.assertFalse(self.testbills.valid_provider(self.testdf, "Not-on-file"))
        
    def test_date_validation(self):
        self.testbills = Bills()
        self.testdf = self.testbills.read_bills()        
        self.assertTrue(self.testbills.validate_date('2019-01-01')[0])
        self.assertFalse(self.testbills.validate_date('2019-41-01')[0])


if __name__ == '__main__':
    unittest.main()