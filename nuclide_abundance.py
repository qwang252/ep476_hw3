# this function is to calculate the nuclide abundances for specific material composition
import material_library as ml
import element_library as el
# calculate atomic density for specific nuclide
# wo = w/o, ao=a/o  
def calculate_atomic_density(rho,wo,ao,MM):
    return rho*wo*ao/MM
# calculate each nuclide's abundance in a specific material and store
# that value under the specified nuclide(A&Z) in nuclide abundance dictionary
def nuclide_abundance_dic(materialfilename,elementfilename,materialname):
   
    total_atomic_den = total_atomic_density(materialfilename,elementfilename,materialname)
    material_structure = ml.main_loop(materialfilename)
    element_structure = el.main_loop(elementfilename)
    Nuclide_abundance_dic = {}
    material = material_structure.get(materialname)
    rho = float(material.get('standard density'))
    number_of_elements = int(material.get('number of elements'))
    for i in range(1,number_of_elements+1):
        element = material.get('component element '+str(i))
        symbol = element.get('component element symbol')
        # atomic number
        Z = element_structure.get(symbol).get('atomic number')
        
        wo=float(element.get('mass fraction'))/100
        MM=float(element_structure.get(symbol).get('molar mass'))
        number_isotopes = int(element_structure.get(symbol).get('number of isotopes'))

        for j in range(1,number_isotopes+1):
            ao=float(element_structure.get(symbol).get('isotope '+str(j)).get('atomic abundance'))/100
            N_i=calculate_atomic_density(rho,wo,ao,MM)
            A = element_structure.get(symbol).get('isotope '+str(j)).get('isotope mass number')
            key = 'A = '+A+', Z = '+Z
            isotope_abundance = N_i/total_atomic_den
            Nuclide_abundance_dic.update({key:isotope_abundance})
          
    return Nuclide_abundance_dic 
# calculate total atomic density for specific material
def total_atomic_density(materialfilename,elementfilename,materialname):
    try:
         material_structure = ml.main_loop(materialfilename)
         element_structure = el.main_loop(elementfilename)
         material = material_structure.get(materialname)
    except FileNotFoundError:
         print('not valid input files')
         return
    except AttributeError:
         print('no such material under the name of '+materialname+' in the material library')
         return 
    number_of_element = int(material.get('number of elements'))
    rho = float(material.get('standard density'))
    total_atomic_den = 0
    for i in range(1,number_of_element+1):
        element = material.get('component element '+str(i))
        symbol = element.get('component element symbol')
        wo=float(element.get('mass fraction'))/100
        MM=float(element_structure.get(symbol).get('molar mass'))
        
        total_atomic_den += rho/MM*wo
    return total_atomic_den
