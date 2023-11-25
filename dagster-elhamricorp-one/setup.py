from setuptools import find_packages, setup

setup(
    name="dagster_elhamricorp_one",
    packages=find_packages(exclude=["dagster_elhamricorp_one_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
