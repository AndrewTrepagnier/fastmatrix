from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name="cy_matrix_mult",
    ext_modules=cythonize("cy_matrix_mult.pyx", language_level=3),
    include_dirs=[numpy.get_include()],
    install_requires=[
        "numpy>=1.20.0"
    ],
) 