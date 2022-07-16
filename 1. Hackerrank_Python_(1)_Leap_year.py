# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:29:56 2022

@author: eliem
"""

class Leap_Year:
    
    
    def __init__(self,input_year):
        self.input_year = input_year
        
    def driver(self):
        
        def fun_1_first_filtration():
            if self.input_year % 4 == 0:
                potential_leap_year_list.append(self.input_year)
            else:
                not_leap_year_list.append(self.input_year)
        
        def fun_2_second_filtration():
            for i in potential_leap_year_list:
                if i % 100 == 0 and i % 400 == 0:
                    leap_year_list.append(i)
                else:
                    not_leap_year_list.append(i)
                        
        def process():
            call_fun_1 = fun_1_first_filtration()
            if len(not_leap_year_list) == 1:
                return False
            else:
                call_fun_2 = fun_2_second_filtration()
                if len(not_leap_year_list) == 1:
                    return False
                else:
                    return True
                
        potential_leap_year_list = []
        not_leap_year_list = []
        leap_year_list = []

        initialization = process()
        return  initialization 
    

a = Leap_Year(2000)
a.driver()
b = a.driver()
print(b)