"""

The content in this script closely follows this example:

    https://tellurium.readthedocs.io/en/latest/_notebooks/core/tesedmlExample.html#reading-executing-sed-ml

But does not work. Why?

"""

import os
import tellurium as te
import tesedml as libsedml
import matplotlib.pyplot as plt


# find the sbml and sedml files
model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')
teusink2000 = os.path.join(model_dir, 'model.xml')
sedml_file = os.path.join(os.path.dirname(__file__), 'simulation.xml')

if not os.path.isfile(teusink2000):
    raise FileNotFoundError(teusink2000)

if not os.path.isfile(sedml_file):
    raise FileNotFoundError(sedml_file)

# load the model
r = te.loadSBMLModel(teusink2000)

# check for errors in the sedml
sedml_doc = libsedml.readSedML(sedml_file)
n_errors = sedml_doc.getErrorLog().getNumFailsWithSeverity(libsedml.LIBSEDML_SEV_ERROR)
print('Read SED-ML file, number of errors: {}'.format(n_errors))
if n_errors > 0:
    print(sedml_doc.getErrorLog().toString())

# read the sedml file
with open(sedml_file, 'r') as f:
    sedml = f.read()

# run the simulations
te.executeSEDML(sedml)




plt.show()








