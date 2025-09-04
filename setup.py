from setuptools import setup, find_packages

setup(
    name="complete_ml_pipeline",   # arbitrary package name
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # add your dependencies here if needed
)
