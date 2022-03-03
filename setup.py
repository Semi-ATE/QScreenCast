# -*- coding: utf-8 -*-

# Copyright © Semi-ATE
# Distributed under the terms of the MIT License


import os

from setuptools import find_packages, setup
from QScreenCast import __version__

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as f:
    Project_description = f.read()


install_requires = []
with open(os.path.join(here, "requirements", "conda_run.txt")) as f:
    for line in f:
        line = line.strip()
        if line != "":
            install_requires.append(line)

setup(
    name="QScreenCast",
    version=__version__,
    description='A no-nonsense screen-caster behind a QToolButton.',
    long_description=Project_description,
    long_description_content_type='text/markdown',
    maintainer='Semi-ATE',
    maintainer_email='info@Semi-ATE.com',
    url='https://github.com/Semi-ATE/QScreenCast',
    packages=find_packages(),
    include_package_data=True,
    package_data={'QScreenCast': ['countdown.gif']},
    # See: https://pypi.org/classifiers/
    classifiers=[  
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Documentation',
        'Topic :: Education',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Capture',
    ],
    license="MIT",
    keywords=[  
        'screencast',
        'qt',
    ],
    platforms=["Windows", "Linux", "MacOS"],
    install_requires=install_requires,
    python_requires='>=3.7',
)
