"""
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

__description__ = "simple python module to get the list of plugins installed on a jenkins instance in plugins.txt format"

setup(
    # identity
    name="list_jenkins_plugins",
    version="1.0.0",
    # sources
    py_modules=["list_jenkins_plugins"],
    # entry points, see https://packaging.python.org/specifications/entry-points/
    entry_points={
        "console_scripts": [
            "list-jenkins-plugins=list_jenkins_plugins:main",
        ],
    },
    # installation constraints
    python_requires=">=3.5, <4",
    install_requires=["requests>=2,<3"],
    # authoring
    description=__description__,
    author_email="postarcr@gmail.com",
    # PyPi metadata
    long_description=__description__,
    long_description_content_type="text/plain",
    url="https://github.com/rikZerac/gradle-hello-world",
    license="open source",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3"
    ],
    keywords="jenkins plugins.txt",
    project_urls={
        "Source": "https://github.com/rikZerac/gradle-hello-world",
    }
)