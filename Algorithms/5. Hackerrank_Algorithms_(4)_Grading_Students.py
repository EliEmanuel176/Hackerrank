# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:34:08 2022

@author: eliem
"""

class Grading:
    
    def __init__(self,grades):
        self.grades = grades
        
    def driver(self):
        
        def n_list_str():
            for i in self.grades:
                if i >= 0:
                    i = str(i)
                    n_list_str_list.append(i)

            return n_list_str_list

        def lists_by_digits_str():
            for i in n_list_str_list:
                if len(i) == 1:
                    single_d_str_list.append(i)
                elif len(i) == 2:
                    double_d_str_list.append(i)
                elif len(i) == 3:
                    triple_d_str_list.append(i)
                else:
                    more_than_3_d_str_list.append(i)

        def lists_by_digits_int():
            if len(single_d_str_list) >= 1:
                for i in single_d_str_list:
                    i = int(i)
                    single_d_int_list.append(i)

            if len(double_d_str_list) >= 1:
                for i in double_d_str_list:
                    i = int(i)
                    double_d_int_list.append(i)

            if len(triple_d_str_list) >= 1:
                for i in triple_d_str_list:
                    i = int(i)
                    triple_d_int_list.append(i)

            if len(more_than_3_d_str_list) >= 1:
                for i in more_than_3_d_str_list:
                    i = int(i)
                    more_than_3_d_int_list.append(i)

        def pass_or_fail_1_3_d():
            for i in triple_d_int_list:
                full_marks_grade_int.append(i)
            for i in single_d_int_list:
                failing_grade_int.append(i)


        def potential_to_be_rounded():
            for i in double_d_int_list:
                if i >= 38:
                    potential_to_be_rounded_int.append(i)
                else:
                    failing_grade_int.append(i)
                    
        def potential_to_be_rounded_to_str():
            for i in potential_to_be_rounded_int:
                i = str(i)
                potential_to_be_rounded_str_list.append(i)           

        def first_and_second_digits(ele):
            return [digit for digit in ele]

        def test_fun():
            for i in range(len(potential_to_be_rounded_str_list)):
                j = potential_to_be_rounded_str_list[i]

                if len(j) >= 0:
                    second_digits_list.append(j)
            return second_digits_list

        def digits_spliters():
            for i in range (len(second_digits_list)):
                j = potential_to_be_rounded_str_list[i]
                for value in j:
                    k = value[0]
                    k_list.append(k)
            return k_list

        def test_func_digits():
            for i in range(1,len(k_list),2):
                i = i
                l_list.append(k_list[i])
            return l_list

        def l_list_to_int():
            for i in range(0, len(l_list)):
                l_list[i] = int(l_list[i])
                l_list_int.append(l_list[i])
            return l_list_int

        def corresponding_diff_in_value():
            for i in l_list_int:
                raw_diff = (i - 5)
                list_of_raw_diff.append(raw_diff)
            return list_of_raw_diff

        def rounding_sort():
            for idx in range(0, len(list_of_raw_diff)) :
                if list_of_raw_diff[idx] >= 3:
                    round_up_indices.append(idx)
                elif list_of_raw_diff[idx] >= -2 and list_of_raw_diff[idx] < 0: 
                    round_up_indices.append(idx)
                else:
                    round_nil_indices.append(idx)
                    
        def final_grade_full_marks_or_fail():
            for i in full_marks_grade_int:
                final_marks_full = i
                if final_marks_full >= 0:
                    final_grade_list.append(final_marks_full)
            for i in failing_grade_int:
                final_marks_fail = i
                if final_marks_fail >= 0:
                    final_grade_list.append(final_marks_fail)

            return final_grade_list
        
        def myround(x, base):
            return base * round(x/base)
        
        def append_unrounded_values():
            for i in round_nil_indices:  
                values_final_unchanged = potential_to_be_rounded_int[i]
                if values_final_unchanged >=0:
                    final_grade_list.append(values_final_unchanged)
            return final_grade_list
        
        def append_rounded_values():
            for j in round_up_indices:
                values_final_rounded = potential_to_be_rounded_int[j]
                values_final_rounded_up = myround(values_final_rounded,base)
                if values_final_rounded_up >= 0:
                    final_grade_list.append(values_final_rounded_up)
            return final_grade_list
        
        def sort_list():
            while stored_value:
                minimum = stored_value[0]   
                for x in stored_value: 
                    if x < minimum:
                        minimum = x
                order_list.append(minimum)
                stored_value.remove(minimum) 
            return order_list

        def value_mapping_list_to_list():
            for i in range(len(order_list)):
                if i >= 0:
                    value_mapping.append(i)    
            return value_mapping
        
        def zip_lists(list_1,list_2):
            return list(zip(list_1,list_2))
        
        def extract_order_of_n_list():
            for num in n_list:
                for i in range(len(value_mapping_zipped)):
                    if value_mapping_zipped[i][0] == num:
                        order_of_number_list.append(value_mapping_zipped[i][1])
            return order_of_number_list
        
        def sort_list_final_grades():
            while final_grade_list_copy:
                minimum = final_grade_list_copy[0]   
                for x in final_grade_list_copy: 
                    if x < minimum:
                        minimum = x
                order_list_final_grades.append(minimum)
                final_grade_list_copy.remove(minimum) 
            return order_list_final_grades

        def value_mapping_final_grades_list_to_list():
            for i in range(len(order_list_final_grades)):
                if i >= 0:
                    value_mapping_final_grades.append(i)    
            return value_mapping_final_grades

        def extract_order_of_final_grades():
            for num in final_grade_list:
                for i in range(len(value_mapping_final_grades_zipped)):
                    if value_mapping_final_grades_zipped[i][0] == num:
                        order_of_number_final_grades_list.append(value_mapping_final_grades_zipped[i][1])
            return order_of_number_final_grades_list
        
        def reordering():
    
            for j in range(len(order_of_n_list_zipped)):
                for i in range(len(final_grades_zipped)):
                    if final_grades_zipped[i][1] == order_of_n_list_zipped[j][1]:
                        final_list.append(final_grades_zipped[i][0])

        single_d = []
        double_d = []
        triple_d = []
        more_than_3_d = []

        single_d_str_list = []
        double_d_str_list = []
        triple_d_str_list = []
        more_than_3_d_str_list = []

        single_d_int_list = []
        double_d_int_list = []
        triple_d_int_list = []
        more_than_3_d_int_list = []
        
        full_marks_grade_int = []
        failing_grade_int = []
        
        potential_to_be_rounded_int = []
        potential_to_be_rounded_str_list = []

        k_list = []
        l_list = []
        second_digits_list = []
        
        list_of_raw_diff = []
        l_list_int = []
        
        round_up_indices = []
        round_nil_indices = []
        indices = []
        
        final_grade_list = []
        
        order_list = []
        value_mapping = []
        
        order_of_number_list = []
        
        order_list_final_grades = []
        value_mapping_final_grades = []

        order_of_number_final_grades_list = []
        
        final_list = []
        
        i = 0
        base = 5
        n_list = self.grades
        stored_value = n_list.copy()
        n_list_str_list = []
        n_atm = n_list[i] ###[9,99,999,9999] test if it works if n were a list
        n_atm_str = str(n_atm)
        n_atm_int = n_atm


        call_fun = n_list_str()
        call_fun_2 = lists_by_digits_str()
        call_fun_3 = lists_by_digits_int()
        
        call_fun_4 = pass_or_fail_1_3_d()
        
        call_fun_5 = potential_to_be_rounded()
        
        call_fun_6 = potential_to_be_rounded_to_str()
        
        test_fun = test_fun()
        split_the_digits = digits_spliters()
        each_second_digit = test_func_digits()
        
        test_fun_4 = l_list_to_int()
        test_fun_5 = corresponding_diff_in_value()
        
        test_fun_6 = rounding_sort()
        
        final_grade_full_marks_or_fail()

        call_fun_7 = append_unrounded_values()
        
        call_fun_8 = append_rounded_values()
        
        call_fun_9 = sort_list()
        call_fun_10 = value_mapping_list_to_list()
        
        value_mapping_zipped = zip_lists(order_list, value_mapping)
        
        call_fun_11 = extract_order_of_n_list()
        
        order_of_n_list_zipped = zip_lists(n_list, call_fun_11)
        
        final_grade_list_copy = final_grade_list.copy()
        
        call_fun_12 = sort_list_final_grades()
        call_fun_13 = value_mapping_final_grades_list_to_list()
        
        value_mapping_final_grades_zipped = zip_lists(order_list_final_grades, value_mapping_final_grades)
        
        call_fun_14 = extract_order_of_final_grades()
        
        final_grades_zipped = zip_lists(final_grade_list, order_of_number_final_grades_list)
        
        call_fun_15 = reordering()
        
        return final_list
    
a = Grading([73, 67, 38, 33])
a.driver()
b = a.driver()
print(b)