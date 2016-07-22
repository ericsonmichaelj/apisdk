from setuptools import setup
import relateiq

setup(
    name='relateiq',
    version=relateiq.__version__,
    packages=['relateiq'],
    install_requires=[
        'requests==2.6.0',
        'nameparser==0.3.4',
        'validate_email==1.3',
        'pytz==2015.2'
    ],
    description='API wrapper for salesforceIQ.',
    author='Michael Ericson',
    author_email='michael@covalentcareers.com',
    url='https://github.com/ericsonmichaelj/relateiq',
)