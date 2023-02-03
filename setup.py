import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coin-collector",
    version="1.0",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'coincollector=coin_collector:main',
        ],
    },
    author="Koizumi Yuhi",
    author_email="bp18041@shibaura-it.ac.jp",
    description="A coin collector game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ykoizumi500/CoinCollector",
    packages=setuptools.find_packages(),
    python_requires='==3.10.9',
)
