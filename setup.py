from collections import OrderedDict

from os import path
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-goodgrids',
    description=(
        'Create Excel files from CSVs using the GoodGrids API, based on an example Excel file template.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=__import__('django_goodgrids').__version__,
    author='Evertabs LLC',
    author_email='support@goodgrids.com',
    url='https://github.com/goodgrids/django-goodgrids',
    project_urls=OrderedDict([
        # ("Documentation", "https://django-goodgrids.readthedocs.io/en/%s/" % release_tag),
        ("GoodGrids", "https://goodgrids.com"),
        ("Source", "https://github.com/goodgrids/django-goodgrids"),
        ("PyPi", "https://pypi.org/project/django-goodgrids"),
        ("Tracker", "https://github.com/goodgrids/django-goodgrids/issues"),
    ]),
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.11',
        'requests>=2',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    keywords='csv excel spreadsheet conversion',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Office/Business',
        'Topic :: Utilities',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
