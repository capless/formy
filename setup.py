from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)

version = '1.1.0'

LONG_DESCRIPTION = """
=======================
Formy
=======================

Python Forms Library with Jinja2 Templates based on Valley


"""

setup(
    name='formy',
    version=version,
    description="""Python Forms Library with Jinja2 Templates""",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='form,validations,schema,declarative',
    author='Brian Jinwright',
    author_email='opensource@capless.io',
    maintainer='Brian Jinwright',
    packages=find_packages(),
    url='https://github.com/capless/formy',
    license='GNU GPL V3',
    install_requires=[str(ir.req) for ir in install_reqs],
    include_package_data=True,
    zip_safe=False,
)
