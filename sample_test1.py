# this function is to test nonvalid file inputs
import element_library as el

filename1 ='element_library'
ele_dic1 = el.main_loop(filename1)
print(ele_dic1)
# this file contains blank lines and comments lines
filename2='element_library_version2'
ele_dic2 = el.main_loop(filename2)


