from nose.tools import assert_equal
from element_library import read_first_line as rfl
from element_library import read_isotope as ri  
def test_first_line_symbol():
    f = open('element_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[0]
    exp = 'h'
    assert_equal(obs,exp)

def test_first_line_molarmass():
    f = open('element_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[1].get('molar mass')
    exp = '0.100790E+01'
    assert_equal(obs,exp)

def test_first_line_atomicnumber():
    f = open('element_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[1].get('atomic number')
    exp = '1'
    assert_equal(obs,exp)
def test_first_line_standarddensity():
    f = open('element_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[1].get('standard density')
    exp = '0.899000E-04'
    assert_equal(obs,exp)

def test_first_line_numberofisotopes():
    f = open('element_library')
    line = f.readline().strip().split()
    structure = rfl(line)
    obs = structure[1].get('number of isotopes')
    exp = '2'
    assert_equal(obs,exp)

def test_read_isotope_massnumber():
    f = open('element_library')
    f.readline()
    line = f.readline().strip().split()
    structure = ri(line)
    obs = structure.get('isotope mass number')
    exp = '1'
    assert_equal(obs,exp)

def test_read_isotope_abundance():
    f = open('element_library')
    f.readline()
    line = f.readline().strip().split()
    structure = ri(line)
    obs = structure.get('atomic abundance')
    exp = '0.999850E+02'
    assert_equal(obs,exp)
