from setuptools import setup

setup(
    name='cu',
    version='0.0.1',
    packages=['cu'],
    url='',
    license='MIT',
    author='ae',
    author_email='ribrea@icloud.com',
    description='ClickUp CLI',
    entry_points={
        'console_scripts': [
            'cu = cu:main',
        ]
    }
)
