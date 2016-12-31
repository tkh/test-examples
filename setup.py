import setuptools


param_dict = dict(
    name='test-examples',
    version='0.0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
)

setuptools.setup(**param_dict)
