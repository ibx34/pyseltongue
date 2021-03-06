from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.readlines()

with open('README.MD') as f:
    readme = f.read()

setup(
    name="Pyseltoungue",
    version="0.0.1",
    author="ibx34",
    url="https://github.com/ibx34/pyseltongue",
    license="MIT",
    include_package_data=True,
    install_requires=requirements,
    long_description=readme,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
