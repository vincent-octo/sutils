from setuptools import setup, find_packages


setup(
    name="sutils",
    version="0.0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['decorator'],

    extras_require={'tests': ['pytest']},

    # metadata for upload to PyPI
    author="Vincent",
    author_email="vincent-octo@users.noreply.github.com",
    description="Simple Python utilities.",
    license="MIT",
    keywords="utility utilities",
    url="https://github.com/vincent-octo/sutils",  # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
