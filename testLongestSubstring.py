# -*- coding: utf-8 -*-
"""
@author: Monali
"""

import unittest
from longestSubstring import *

class TestSubstring(unittest.TestCase):

    def test_emptyString(self):
        input_string=""
        self.assertEqual(longestSubstringForEachChar(input_string,1),"Blank string can't be processed","Wrong Output")
    
    def test_noElement(self):
        input_string="211333111100223"
        self.assertEqual(longestSubstringForEachChar(input_string,''),"No elements to check","Wrong Output")
        
    def test_substring(self):
        input_string="211333111100223"
        self.assertEqual(longestSubstringForEachChar(input_string,1),4,"Wrong Output")

    def test_wrongElement(self):
        input_string="211333111100223"
        self.assertEqual(longestSubstringForEachChar(input_string,7),"Element Not present","Wrong Output")

if __name__ == '__main__':
    unittest.main()