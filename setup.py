from setuptools import setup

setup(
    name="data-structures",
    description="""A Python implementation of data structures.
    Some previous work by Victor Benavente, vbenavente@hotmail.com""",
    version=0.1,
    author="Derek Hewitt, Jeff Torres",
    author_email="derekmhewitt@gmail.com, jeffrey.n.torres@gmail.com",
    license="MIT",
    py_modules=["linked_list"],
    package_dir={"": "src"},
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
        ]
    }
)
