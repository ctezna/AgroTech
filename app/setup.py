from setuptools import setup,find_packages

requires = (
        'Flask',
        )

setup(
    name='agroTech',
    version='1.0',
    author='Carlos Tezna',
    author_email='agroTech@gmail.com',
    description='Software for managing AgroTech SmartPots',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
