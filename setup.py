from setuptools import setup, find_packages

VERSION = '0.1.6'
DESCRIPTION = "Dynamic multiselect filters for Streamlit"

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

with open("CHANGELOG.md", "r", encoding="utf-8") as fh:
    changelog = fh.read()

setup(
    name="streamlit_dynamic_filters_custom",
    version=VERSION,
    author="Jose Chaves",
    author_email="<jchavesm2017@gmail.com>",
    description=DESCRIPTION,
    long_description=f"{readme}\n\n{changelog}",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['streamlit'],
    keywords=['streamlit', 'custom', 'component'],
    license="MIT",
    url="https://github.com/jchavesmartinez/streamlit-dynamic-filters-custom",
)
