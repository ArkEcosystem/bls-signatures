import setuptools
from pathlib import Path

setuptools.setup(
    name="blspy_impl",
    author="Mariano Sorgente",
    author_email="mariano@chia.net",
    description="BLS signatures in c++ (pure python implementation)",
    python_requires=">=3.7",
    url='https://github.com/Chia-Network/bls-signatures',
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    py_modules=[],
)
