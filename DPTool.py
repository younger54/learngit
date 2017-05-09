from distutils.core import setup
import sys
import numpy
import scipy.sparse.csgraph._validation

import glob

includes = ["encodings", "encodings.*"]
sys.argv.append("py2exe")

# We need to exclude matplotlib backends not being used by this executable.  You may find
# that you need different excludes to create a working executable with your chosen backend.
# We also need to include include various numerix libraries that the other functions call.

opts = {
    'py2exe': {"includes": ["sip", "PyQt4.QtGui", "matplotlib.backends", "matplotlib.backends.backend_qt4agg",
                            "matplotlib.figure", "pylab", "numpy", "matplotlib.pyplot",
                            "matplotlib.backends.backend_tkagg", "scipy.optimize", "scipy.sparse.csgraph._validation",
                            "scipy.special._ufuncs_cxx", "scipy.integrate"],
               'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                'libgobject-2.0-0.dll', 'MSVCP90.dll'],
               'packages': ['FileDialog'],
               }
}

# Save matplotlib-data to mpl-data ( It is located in the matplotlib\mpl-data
# folder and the compiled programs will look for it in \mpl-data
# note: using matplotlib.get_mpldata_info
data_files = [(r'mpl-data', glob.glob(r'D:\Program Files\Python27\Lib\site-packages\matplotlib\mpl-data\*.*')),
              # Because matplotlibrc does not have an extension, glob does not find it (at least I think that's why)
              # So add it manually here:
              (r'mpl-data', [r'D:\Program Files\Python27\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
              (r'mpl-data\images',
               glob.glob(r'D:\Program Files\Python27\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
              (r'mpl-data\stylelib',
               glob.glob(r'D:\Program Files\Python27\Lib\site-packages\matplotlib\mpl-data\stylelib\*.*')),
              (r'mpl-data\fonts',
               glob.glob(r'D:\Program Files\Python27\Lib\site-packages\matplotlib\mpl-data\fonts\*.*'))]

# for console program use 'console = [{"script" : "scriptname.py"}]
setup(windows=[{"script": "DefectPredict.py"}], options=opts, data_files=data_file)