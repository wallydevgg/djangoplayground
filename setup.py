from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirementsFile = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="drf-deploy",
    description="deploy sencillo para pruebas de drf",
    long_description=long_description,
    keywords="drf,rest,api,deploy",
    version="0.1",
    # package_data={
    #    "": ["*.py", "templates/*.html"],
    # },
    #
    # package_data={
    #    "*.py": ["*.py"],
    # },
    # extras_require={
    #    "gunicorn": [
    #        "gunicorn",
    #    ],
    # },
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["django>=4.2", 'backports.zoneinfo;python_version<"3.13"'],
    python_requires=">=3.10",
    zip_safe=False,
    # entry_points={  # Optional
    #    "console_scripts": [
    #        "flask-db-init=main:app",
    #    ],
    # },
    project_urls={
        "Source": "https://github.com/wallydevgg/djangoplayground/tree/ecommerce",
    },
    # scripts=["manage.py"],
)
