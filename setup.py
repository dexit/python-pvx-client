from setuptools import setup, find_packages


setup(
    name='pvx-python',
    version='0.0.1',
    description='Python client for the People Vox',
    url='https://github.com/groveco/python-pvx-client',
    keywords=['People Vox', 'pvx'],
    install_requires=['requests>=2.3.0'],
    packages=find_packages(),
    include_package_data=True,
)