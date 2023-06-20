#Verzeichnisstruktur
'''
password_package/
└── password_package/
    └── password_module.py
'''


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Password_package",
    version="1.0.0",
    author="Victoria",
    author_email="vhertfelder@stud.macromedia.de",
    description="Password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
	license='MIT',
    packages=['password_package'],
	install_requires=['requests'],
)