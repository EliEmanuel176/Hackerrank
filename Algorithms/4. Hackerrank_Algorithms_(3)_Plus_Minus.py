# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 07:20:51 2022

@author: eliem
"""
class Ratio:
    def __init__(self,arr):
        self.arr = arr
        
    def driver(self):
        def function():
            def positive_ratio():
                for i in range (len_of_array):
                    element_in_loop = self.arr[i]
                    if element_in_loop  > 0:
                        positive_list.append(element_in_loop)
                        len_of_positive_list = len(positive_list)
                        ratio_of_positive_unrounded = len_of_positive_list / len_of_array
                        ratio_of_positive = round(ratio_of_positive_unrounded,6)
                return ratio_of_positive
        
            def negative_ratio():
                for i in range (len_of_array):
                    element_in_loop = self.arr[i]
                    if element_in_loop  < 0:
                        negative_list.append(element_in_loop)
                        len_of_negative_list = len(negative_list)
                        ratio_of_negative_unrounded = len_of_negative_list / len_of_array
                        ratio_of_negative = round(ratio_of_negative_unrounded,6)
                return ratio_of_negative
            
            
                
            def zero_ratio():
                for i in range (len_of_array):
                    element_in_loop = self.arr[i]
                    if element_in_loop  == 0:
                        zero_list.append(element_in_loop)
                        len_of_zero_list = len(zero_list)
                        ratio_of_zero_unrounded = len_of_zero_list / len_of_array
                        ratio_of_zero = round(ratio_of_zero_unrounded,6)
                return ratio_of_zero
            
            positive_list = []
            negative_list = []
            zero_list = []
        
            
            len_of_array = len(self.arr)
        
            positive_r = positive_ratio()
            positive_r_rounded = round(positive_r,6)
            positive_r_final = format(positive_r_rounded, '.6f')
            
            negative_r = negative_ratio()
            negative_r_rounded = round(negative_r,6)
            negative_r_final = format(negative_r_rounded, '.6f')
            
            zero_r = zero_ratio()
            zero_r_rounded = round(zero_r,6)
            zero_r_final = format(zero_r_rounded, '.6f')
            
            message = print(f"""{positive_r_final}\n{negative_r_final}\n{zero_r_final}""")
            return message
        
        call_fun_1 = function()
        return call_fun_1
    
a = Ratio([-4, 3, -9, 0, 4, 1])
a.driver()

