import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pycat-test',
    version='0.0.1',
    description='A cat like tool implemented in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mitsuhachi/pycat',
    author='Mitsu Hachi',
    author_email='pypi@hachimitsu.fastmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['pycat=pycat:main']
    }
)
