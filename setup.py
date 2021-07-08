# python setup.py bdist_wheel
# twine upload

from setuptools import setup, find_packages

setup(
    name="xing-tick-crawler",
    version='0.0.7',
    url="https://github.com/quantrading/xing-tick-crawler",
    license="MIT",
    author="Jang Woo Jae",
    author_email="woojae.jang26@gmail.com",
    description="ebest xing api wrapper",
    install_requires=[
        'pandas',
        'pywin32'
    ],
    packages=find_packages(),
    python_requires='>=3',
    long_description=open('README.md', encoding='UTF8').read(),
    long_description_content_type="text/markdown",
    package_data={},
    zip_safe=False,
)
