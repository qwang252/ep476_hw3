# this function is to test nonvalid input for material library
import material_library as ml

# valid file
filename1= 'material_library'
mat_dic1 = ml.main_loop(filename1)
print(mat_dic1)
# non valid file
filename2 = 'material_library_version2'
mat_dic2 = ml.main_loop(filename2)

