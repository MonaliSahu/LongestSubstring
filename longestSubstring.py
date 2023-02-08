# -*- coding: utf-8 -*-
"""
@author: Monali
"""

def getLongestSubstring(function):
    '''
    Decorator function on top of the longestSubstringForEachChar function
    
    It helps in doing all the initial input validations
    '''
    def check(input_string,element):
        element=str(element)
        if isinstance(input_string,str):
            if len(input_string)==0:
                return "Blank string can't be processed"
            if len(element)==0:
                return "No elements to check"
            substr_len_count=function(input_string)
            return substr_len_count.get(element,"Element Not present")
    return check
    
@getLongestSubstring              
def longestSubstringForEachChar(input_string,*element):
    '''
    Function to find length of longest substring of each character of a input string.s

    Parameters
    ----------
    input_string : String
        The original string from which substring length needs to be found.
    *element : Non Keyword argument (to accept element for check())

    Returns
    -------
    char_dict : Dict
        returns a dictionary with all unique characters as the key and their longest substring length as value.

    '''
    char_dict={}
    char_dict[input_string[0]]=1
    count=1
    for index in range(1,len(input_string)):
        if input_string[index] not in char_dict.keys():
            char_dict[input_string[index]]=1
        prev_char=index-1
        if (input_string[prev_char]==input_string[index]):
            count+=1
        else:
            if char_dict[input_string[prev_char]] < count:
                char_dict[input_string[prev_char]]=count
            count=1
    if char_dict[input_string[-1]] < count:
        char_dict[input_string[-1]]=count
    return char_dict