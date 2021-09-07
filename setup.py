import pathlib
from setuptools import setup
import discord_styler.__info__ as info

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name=info.__project__,
    version=info.__version__,
    description=info.__summary__,
    long_description=README,
    long_description_content_type="text/markdown",
    url=info.__webpage__,
    author=info.__author__,
    author_email=info.__email__,
    license=info.__license__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Chat",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    packages=["discord_styler"],
    package_data={
        "discord_styler": ["py.typed"]
    },
    install_requires=[],
)
