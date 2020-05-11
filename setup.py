from setuptools import setup

setup(
    name='2B2T_Queue',
    version='1.0',
    packages=['2B2T_Queue'],
    url='https://github.com/LeoNobre-hash/2B2T_Queue.git',
    author='NobreHD',
    author_email='leo.nobre.hd@gmail.com',
    description='2B2T Server Queue Monitoring Program',
    requires=['requests', 'win10toast'],
    scripts=['2B2T_Queue/main.py']
)
