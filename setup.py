import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
includefiles = ['gifsicle.exe', 'noimage.bin', 'config.ini', 'icon.ico', 'changelog.md']

exclude_libs = ['pyreadline', 'doctest','optparse', 'matplotlib', "BaseHTTPServer", "SocketServer", "dateutil", "httplib", "itertools", "mpl_toolkits", "numpy.f2py", "pydoc_data", "urllib2", "zipimport", "scipy.sparse.linalg.eigen.arpack", "scipy.sparse._sparsetools", 'scipy']

build_exe_options = {"packages": ["numpy.core", "numpy.lib"], "optimize": 0, 'include_files':includefiles, "excludes":exclude_libs, "include_msvcr":True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "CMN_binViewer",
        version = "1.0",
        options = {"build_exe": build_exe_options},
        executables = [
            Executable("CMN_binViewer.py", 
                base=base, 
                icon="icon.ico")]
        )
