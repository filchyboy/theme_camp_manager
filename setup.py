from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="clf-lambdata-1",
    version="0.1.1",
    author="Chris Filkins",
    author_email="christopher.filkins@gmail.com",
    description="Learning about my package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/filchyboy/lambdata-pack",
    keywords="learning tools",
    packages=find_packages() # ["my_lambdata"]
)