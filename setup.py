from setuptools import setup, find_packages


setup(
    name="edu.pad",
    version="0.0.1",
    author="Felipe Sánchez",
    author_email="leon.sanchez@est.iudigital.edu.co",
    description="",
    py_modules=["actividad1","actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4"
                      
    
    ]

)