from setuptools import setup
from Cython.Build import cythonize
import numpy 

setup(
    name="fastmatrix",
    ext_modules=cythonize("fastmatrix/cy_matrix_utils.pyx", language_level=3),
    include_dirs=[numpy.get_include()],
    install_requires=[
        "numpy>=1.20.0"
    ],
)