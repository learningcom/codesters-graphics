from distutils.core import setup

VERSION = '0.0.18'

CLASSIFIERS = [
    'Programming Language :: Python',

]
install_requires = [
    'Pillow',
]
setup(
    name="codesters",
    description="Offline replication of the graphics on codesters.com",
    version=VERSION,
    author="Codesters",
    author_email="matthew@codesters.com",
    url="https://github.com/codestersnyc/codesters-graphics",
    #download_url="https://bitbucket.org/guillaumepiot/cotidia-admin-tools/downloads/cotidia-admin-tools-0.4.1.tar.gz",
    #package_dir={'codesters': 'codesters'},
    packages=['codesters'],
    include_package_data = True,
    package_data = {
        'codesters': ['sprites/*.gif',
                      'examples/*.py']
    },
    install_requires=install_requires,
    entry_points={
        'console_scripts':['codesters = codesters.execute:execute',
                           'codesters-example = codesters.execute:execute_example']
    },
    classifiers=CLASSIFIERS,
)
