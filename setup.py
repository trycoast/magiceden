from setuptools import setup


def readme():
    '''Read README file'''
    with open('README.rst') as infile:
        return infile.read()


setup(
    name='magiceden',
    version='0.1',
    description='Magiceden API wrapper',
    long_description=readme().strip(),
    author='',
    author_email='',
    url='https://bitbucket.org/kindwail/magiceden',
    packages=['magiceden'],
    install_requires=['requests', 'tenacity', 'ratelimit @ git+https://github.com/trycoast/ratelimit.git'],
    keywords=[
        'magiceden',
        'solana',
        'nft',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development'
    ],
    include_package_data=True,
    zip_safe=False
)
