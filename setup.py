from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("mur_funcs.pyx"),
)

# to build do:
# python setup.py build_ext --inplace