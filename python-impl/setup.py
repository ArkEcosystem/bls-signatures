import sys

import setuptools


requires = [
    'base58',
    'binary-helpers',
    'blspy @ git+https://github.com/ArkEcosystem/bls-signatures@e7942654c48e94e955c81e7a131bc3d5e9d6b707#egg=blspy',
    'coincurve',
    'pycryptodomex',
    'btclib',
    'cryptography',
]

tests_require = [
    'flake8>=3.5.0',
    'flake8-import-order>=0.17.1',
    'flake8-print>=3.1.0',
    'flake8-quotes>=1.0.0',
    'pytest>=3.6.1',
    'pytest-cov>=2.5.1',
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setup_requires = ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else []

setuptools.setup(
    name="blspy",
    author="Mariano Sorgente",
    author_email="mariano@chia.net",
    description="BLS signatures in c++ (python bindings)",
    python_requires=">=3.7",
    url='https://github.com/Chia-Network/bls-signatures',
)
