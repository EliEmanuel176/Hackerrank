# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 07:04:27 2022

@author: eliem
"""

import numpy as np

class DiagonalDifference:
    
    
    def __init__(self,arr):
        self.arr = arr
        
    def driver(self):
        
        def difference_of_diagonals():
            def sum_of_primary_diagonal():
                def number_of_loops_through_matrix_primary_diagonal():
                    index_for_loop = -1
                    for i in range(0,n,1):
                        index_for_loop += 1
                        if index_for_loop >= 0:
                            loop_rows.append(index_for_loop)
                            loop_columns.append(index_for_loop)

                    return loop_rows
                first_step = number_of_loops_through_matrix_primary_diagonal()

                def coordinates_to_primary_diagonal_elements():
                    def primary_diagonal_coordinates():
                        def primary_diagonal_i():

                            for i in first_step:
                                coordinates_i = [i]
                                i += 1
                                if i >= 0:

                                    list_of_coordinates_i_primary.append(coordinates_i)
                            return list_of_coordinates_i_primary


                        def primary_diagonal_j():
                            for j in first_step:
                                coordinates_j = [j]
                                j = n
                                j += 1
                                if j >= 0:

                                    list_of_coordinates_j_primary.append(coordinates_j)
                            return list_of_coordinates_j_primary
                        i_coordinates_primary = primary_diagonal_i()
                        j_coordinates_primary = primary_diagonal_j()


                        list_of_coordinates_final_primary = [i + j for i, j in zip(i_coordinates_primary, j_coordinates_primary)]
                        return list_of_coordinates_final_primary

                    coordinates_of_primary_diagonal = primary_diagonal_coordinates()


                    for x in range(len(coordinates_of_primary_diagonal)):
                        each_loop = coordinates_of_primary_diagonal[x]
                        i, j = each_loop
                        primary_diagonal_elements = arr_as_np_array[i, j]

                        fun_list_success_coordinates_primary.append(primary_diagonal_elements)

                    return fun_list_success_coordinates_primary

                primary_diagonal_elements = coordinates_to_primary_diagonal_elements()
                sum_of_primary_diagonal_elements = sum(primary_diagonal_elements)

                return sum_of_primary_diagonal_elements

            def sum_of_secondary_diagonal():

                def number_of_loops_through_matrix_secondary_diagonal():
                    index_for_loop = -1
                    for i in range(0,n,1):
                        index_for_loop += 1
                        if index_for_loop >= 0:
                            loop_rows_secondary_diagonal.append(index_for_loop)
                            loop_columns_secondary_diagonal.append(index_for_loop)

                    return loop_rows_secondary_diagonal
                first_step = number_of_loops_through_matrix_secondary_diagonal()




                def secondary_diagonal_coordinates():
                    first_step = number_of_loops_through_matrix_secondary_diagonal()

                    def secondary_diagonal_i():

                        for i in first_step:
                            coordinates_i = [i]
                            i += 1
                            if i >= 0:

                                list_of_coordinates_i.append(coordinates_i)
                        return list_of_coordinates_i


                    def secondary_diagonal_j():
                        for j in range(n-1,-1,-1):
                            coordinates_j = [j]
                            j = n
                            j -= 1
                            if j >= 0:

                                list_of_coordinates_j.append(coordinates_j)
                        return list_of_coordinates_j
                    i_coordinates = secondary_diagonal_i()
                    j_coordinates = secondary_diagonal_j()


                    list_of_coordinates_final = [i + j for i, j in zip(i_coordinates, j_coordinates)]
                    return list_of_coordinates_final


                def coordinates_of_secondary_diagonal_elements():
                    for z in range(len(secondary_diagonal_coordinates_all)):
                        coordinates = []
                        coordinates = secondary_diagonal_coordinates_all[z]
                        z += 1
                        fun_list_test.append(coordinates)
                    return fun_list_test




                def coordinates_to_secondary_diagonal_elements():
                    for x in range(len(coordinates_of_secondary_diagonal)):
                        each_loop = coordinates_of_secondary_diagonal[x]
                        i, j = each_loop
                        seconday_diagonal_elements = arr_as_np_array[i, j]

                        fun_list_success_coordinates.append(seconday_diagonal_elements)

                    return fun_list_success_coordinates
                secondary_diagonal_coordinates_all = secondary_diagonal_coordinates()
                coordinates_of_secondary_diagonal = coordinates_of_secondary_diagonal_elements()
                secondary_diagonal_elements = coordinates_to_secondary_diagonal_elements()
                sum_of_secondary_diagonal_elements = sum(secondary_diagonal_elements)
                return sum_of_secondary_diagonal_elements

            list_of_coordinates_i_primary = []
            list_of_coordinates_j_primary = []

            primary_diagonal_list = []
            secondary_diagonal_list = []

            list_of_coordinates_i = []
            list_of_coordinates_j = []
            list_of_coordinates_final = []



            loop_rows_secondary_diagonal = []
            loop_columns_secondary_diagonal = []
            fun_list_test = []

            loop_rows = []
            loop_columns = []

            fun_list_success_coordinates_primary = []

            fun_list_success_coordinates = []
            
            arr_as_np_array = np.array(self.arr)
            n = len(self.arr)
            sum_of_diagonal_primary = sum_of_primary_diagonal()
            sum_of_diagonal_secondary = sum_of_secondary_diagonal()
            difference = sum_of_diagonal_primary - sum_of_diagonal_secondary
            difference_abs_value = abs(difference)

            return difference_abs_value
        call_fun_1 = difference_of_diagonals()
        return call_fun_1
        
a = DiagonalDifference(
    [[1,1,2,5],
    [0,5,6,5],
    [8,2,3,5],
    [1,1,2,3]]
)
a.driver()
b = a.driver()
print(b)