from setuptools import setup

setup(
    name="data-structures",
    description="A Python implementation of data structures.",
    version=0.1,
    author="Derek Hewitt, Victor Benavente",
    author_email="derekmhewitt@gmail.com, vbenavente@hotmail.com",
    license="MIT",
    py_modules=["linked_list"],
    package_dir={"": "src"},
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
            "server = server:main", "client = client:main"
        ]
    }
)
