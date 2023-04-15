import os
from setuptools import setup, find_packages

VERSION = "1.7.3"

src_dir = os.path.dirname(__file__)

install_requires = [
    "boto3",
    "troposphere",
    "PyYAML",
    "awacs",
    "gitpython",
    "jinja2",
    "schematics",
    "formic2",
    "python-dateutil",
    "MarkupSafe",
    "more-itertools",
    "rsa",
    "python-jose",
    "future",
]

setup_requires = ['pytest-runner']

tests_require = [
    "pytest~=7.0.0",
    "pytest-cov~=4.0",
    "mock~=5.0",
    "moto[awslambda]~=4.0.0",
    "testfixtures~=7.0.0",
    "flake8-future-import",
]

scripts = [
    "scripts/compare_env",
    "scripts/docker-stacker",
    "scripts/stacker.cmd",
    "scripts/stacker",
]


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == "__main__":
    setup(
        name="stacker",
        version=VERSION,
        author="Michael Barrett",
        author_email="loki77@gmail.com",
        license="New BSD license",
        url="https://github.com/cloudtools/stacker",
        description="AWS CloudFormation Stack manager",
        long_description=read("README.rst"),
        packages=find_packages(),
        scripts=scripts,
        install_requires=install_requires,
        tests_require=tests_require,
        setup_requires=setup_requires,
        extras_require=dict(testing=tests_require),
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3.5+",
        ],
    )
