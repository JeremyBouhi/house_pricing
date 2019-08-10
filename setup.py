from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="House Pricing",
    description="Prediction of house pricing famous kaggle dataset",
    author="Jeremy Bouhi",
    version="0.0.1",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={'house_princing': ['data/*.csv']},
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'dvc'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ]
)
