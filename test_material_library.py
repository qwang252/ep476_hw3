from nose.tools import assert_equal
from material_library import read_first_line as rfl
from material_library import read_components as rc  
def test_first_line_materialname():
    f = open('material_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[0]
    exp = 'water'
    assert_equal(obs,exp)

def test_first_line_density():
    f = open('material_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[1].get('standard density')
    exp = '1.00'
    assert_equal(obs,exp)

def test_first_line_numelements():
    f = open('material_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[1].get('number of elements')
    exp = '2'
    assert_equal(obs,exp)
def test_read_components_componentsymbol():
    f = open('material_library')
    f.readline()
    line = f.readline().strip().split()
    structure = rc(line)
    obs = structure.get('component element symbol')
    exp = 'h'
    assert_equal(obs,exp)

def test_read_components_massfraction():
    f = open('material_library')
    f.readline()
    line = f.readline().strip().split()
    structure = rc(line)
    obs = structure.get('mass fraction')
    exp = '11.111'
    assert_equal(obs,exp)

def test_read_components_atomicnumber():
    f = open('material_library')
    f.readline()
    line = f.readline().strip().split()
    structure = rc(line)
    obs = structure.get('atomic number')
    exp = '1'
    assert_equal(obs,exp)


