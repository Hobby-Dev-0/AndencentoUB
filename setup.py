import re

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "Andencento"
author = "TeamAndencento"
author_email = "paman7647@gmail.com"
description = "A Secure  and Powerful Python-Telethon Based Library For Andencento Userbot."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/Andencento/Andencento"


setuptools.setup(
    name=name,
    version="0.10",
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    packages=setuptools.find_packages(),
    install_requires=[
        "telethon",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
