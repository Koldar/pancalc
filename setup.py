import os
from typing import List, Tuple, Iterable

import setuptools

from pancalc import version

# DATA

PROJECT_NAME = "pancalc"
PROJECT_MAIN_PACKAGE = PROJECT_NAME
AUTHOR_NAME = "Massimo Bono"
AUTHOR_EMAIL = "massimobono1@gmail.com"
PROJECT_DESCRIPTION = "Small command line calculator"
PROJECT_REPOSITORY = "https://github.com/Koldar/pancalc"


with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements(requirements: str) -> Iterable[str]:
    with open(requirements, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
    for line in lines:
        yield line.split("==")[0]


# def get_data_files() -> List[Tuple[str, List[str]]]:
#     if os.name == "nt":
#         return [
#             # put exe into C:\Python38\Scripts
#             ("Scripts", [os.path.join("scripts", WINDOWS_EXE)])
#         ]
#     elif os.name == "posix":
#         return [
#             # /usr/local/bin
#             ("bin", [os.path.join("scripts", LINUX_EXE)])
#         ]
#     else:
#         raise ValueError(f"invalid os name {os.name}")


setuptools.setup(
    name=PROJECT_NAME,
    version=version.VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=PROJECT_DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=PROJECT_REPOSITORY,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=list(get_requirements("requirements.txt")),
    include_package_data=True,
    entry_points={"console_scripts": [f"{PROJECT_NAME}={PROJECT_MAIN_PACKAGE}.main:main"]},
    python_requires='>=3.8',
)
