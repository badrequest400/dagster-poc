from setuptools import find_packages, setup

setup(
    name="poc",
    packages=find_packages(exclude=["poc_tests"]),
    install_requires=[
        "dagster",
        "pandas",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
    package_data={"poc": ["defs/data/*"]},
)
