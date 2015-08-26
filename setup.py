from distutils.core import setup

VERSION = '0.0.8'
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
        'codesters': ['sprites/codestersLogo.gif']
    },
    #package_data={'admin_tools': data_files},
    #include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts':['codesters = script.codesters']
    },
    classifiers=CLASSIFIERS,
)
