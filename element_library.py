# this function is to read an element library into an element dictionary
import check_blank_comments as check
def read_first_line(line):
    symbol= line[0]
    single_element_dic = {}
    single_element_dic['molar mass']= line[1]
    single_element_dic['atomic number']= line[2]
    single_element_dic['standard density']= line[3]
    single_element_dic['number of isotopes'] = line[4]
    for i in range(1,int(line[4])+1):
        single_element_dic['isotope '+str(i)]={}
    return symbol, single_element_dic
def read_isotope(line):
    isotope_dic = {}
    isotope_dic['isotope mass number']= line[0]
    isotope_dic['atomic abundance']= line[1]
    return isotope_dic
# return the element dictionary in main_loop
def main_loop(filename):
 
    if check.check_blank_comments(filename)!=True
       return 
    #try:
    #   f = open(filename)
    #except FileNotFoundError:
    #   print('cannot find the file under the name of '+ filename)
    #   return
    element_dictionary = {}
    for line in f:
        line = line.strip().split()
        if len(line) > 2:
           symbol = read_first_line(line)[0]
           element_dictionary[symbol] = read_first_line(line)[1]
           i = 1
        else:
           element_dictionary[symbol]['isotope '+str(i)].update(read_isotope(line))
           i=i+1
              
    return element_dictionary 


         
                  

