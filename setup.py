"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.  # noqa: E501

    The version of the OpenAPI document: 2.4.9
    Contact: hello@eliona.io
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "Python Eliona API client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Eliona REST API",
    author="Eliona by IoTEC AG",
    author_email="hello@eliona.io",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Eliona REST API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    long_description="""\
    The Eliona REST API enables unified access to the resources and data of an Eliona environment.  # noqa: E501
    """
)
