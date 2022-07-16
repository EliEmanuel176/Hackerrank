# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 06:47:56 2022

@author: eliem
"""

class Time:
    
    def __init__(self,input_time_str):
        self.input_time_str = input_time_str
        
    def driver(self):
        
        def hours_str_to_int(hours_int_conversion):
            return int(hours_int_conversion)

        def hours_int_to_str(hours_str_conversion):
            return str(hours_str_conversion)
        
        
        def fun_for_AM():
            def hour_12_am_to_00():
                def first_zero_first_step():
                    hours_int_from_data = hours_str_to_int(hours)
                    if hours_int_from_data == 12:
                        hours_int = 12 - hours_int_from_data
                        first_zero = hours_int_to_str(hours_int)
                        hour_12_am_00_first.append(first_zero)
                    return hour_12_am_00_first
                hour_12_am_00_first = []
                first_zero_first_step()

                def second_zero_second_step():
                    hour_12_am_00_intermediate = hour_12_am_00_first * 2
                    return hour_12_am_00_intermediate
                hour_12_am_00_intermediate = []
                second_zero_second_step()

                def final_step():
                    final_step_str = ''.join(['0','0'])

                    hour_12_am_00_final.append(final_step_str)
                    return hour_12_am_00_final


                hours_int_from_data = hours_str_to_int(hours)
                str_00 = final_step()
                return str_00
            if hours_int_from_data == 12:
                call_fun_1 = hour_12_am_to_00()
                hours_display = hour_12_am_00_final[0]
                time_str = hours_display + colons_1 + mins + colons_2 + seconds
                print(time_str)
            else:
                hours_display = hours
                time_str = hours_display + colons_1 + mins + colons_2 + seconds
                print(time_str)

        def fun_for_PM():
            def hour_pm_12_to_23():
                hours_int_from_data = hours_str_to_int(hours)
                if hours_int_from_data == 12:
                    hours_display = hours
                else:

                        hours_1_to_11_pm = hours_int_from_data + 12
                        hours_1_to_11_pm_str = hours_int_to_str(hours_1_to_11_pm)
                        hours_display = hours_1_to_11_pm_str

                return hours_display
            hours_display = hour_pm_12_to_23()
            time_str = hours_display + colons_1 + mins + colons_2 + seconds
            print(time_str)




        hours = self.input_time_str[0:2]
        mins = self.input_time_str[3:5]
        seconds = self.input_time_str[6:8]
        am_or_pm = self.input_time_str[8:10]
        colons_1 = self.input_time_str[2]
        colons_2 = self.input_time_str[5]


        am_or_pm_from_data = self.input_time_str[8:9]
        colons_1_from_data = self.input_time_str[2]
        colons_2_from_data = self.input_time_str[5]

        piece_data_hours = []
        piece_data_mins = []
        piece_data_seconds = []
        piece_data_colon_1 = [':']
        piece_data_colon_2 = [':']
        piece_total = []

        hour_12_am_00_first = []
        hour_12_am_00_intermediate = []
        hour_12_am_00_final = []
        
        if am_or_pm == 'AM':
            fun_for_AM()

        else:
            fun_for_PM()


        hours_int_from_data = hours_str_to_int(hours)

        
t = Time('05:47:30PM')
t.driver()
