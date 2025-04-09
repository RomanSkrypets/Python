from printing_models import print_models as pm, show_completed_models as scm


import ex8_16
from ex8_16 import printing
from ex8_16 import printing as fn
import ex8_16 as mn
from ex8_16 import *


unprinted_designs = ['phone case', 'robot pedant', 'dodecahedron']
completed_models = []

printing(unprinted_designs, completed_models)
scm(completed_models)