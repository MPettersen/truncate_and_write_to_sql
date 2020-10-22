import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'truncate-and-write-to-sql-markus',
    version = '0.0.0',
    author = 'Markus Pettersen',
    description = 'Truncate existing table and write to the table with new entries',
    long_description = long_description,
    url = 'https://github.com/MPettersen/truncate_and_write_to_sql',
    packages = setuptools.find_packages(),
    classfilters = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT Licence',
        'Operating System :: OS Independant',
    ],
    python_requires = '>=3.8',
)