# this funciton is to read a material library into a single material data structure
import check_blank_comments as check
def read_first_line(line):
    material_name = line[0]
    single_material_dic ={}
    single_material_dic['standard density'] = line[1]
    single_material_dic['number of elements'] = line[2]
    for i in range(1,int(line[2])+1):
      single_material_dic['component element '+ str(i)]={}
    return material_name,single_material_dic

def read_components(line):
    component_dic ={}
    component_dic['component element symbol']= line[0]
    component_dic['mass fraction'] = line[1]
    component_dic['atomic number'] = line[2]
    return component_dic

def main_loop(filename):
    #try:
    #   f=open(filename)
    #except FileNotFoundError:
    #   print('cannot find the file under the name of '+filename)
    if check.check_blank_comments(filename)==False: 
        return
    material_dictionary = {}
    f= open(filename)
    for line in f:
        line = line.strip().split()
        if len(line[0]) >= 3:
           material_name = read_first_line(line)[0]
           material_dictionary[material_name] =read_first_line(line)[1]
           i = 1
        else:
           material_dictionary[material_name]['component element '+str(i)].update(read_components(line))
           i=i+1

    return material_dictionary
