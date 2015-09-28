from distutils.core import setup

VERSION = '0.0.42'

CLASSIFIERS = [
    'Programming Language :: Python',
    'Intended Audience :: Education',
    'Topic :: Education :: Computer Aided Instruction (CAI)',
    'Development Status :: 2 - Pre-Alpha',

]
install_requires = [
    'Pillow',
]
setup(
    name="codesters",
    description="Offline replication of the graphics on codesters.com",
    version=VERSION,
    author="Codesters",
    author_email="thomas@codesters.com",
    url="https://github.com/codestersnyc/codesters-graphics",
    packages=['codesters'],
    include_package_data = True,
    package_data = {
        'codesters': ['sprites/*.gif',
                      'examples/*.py']
    },
    install_requires=install_requires,
    entry_points={
        'console_scripts':['codesters = codesters.execute:runner']
    },
    classifiers=CLASSIFIERS,
)
