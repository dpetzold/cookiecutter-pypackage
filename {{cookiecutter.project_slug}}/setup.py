#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def get_requirements(env=None):
    if env:
        env = f'-{env}'
    with open(f'requirements{env if env else ""}.txt') as fp:
        return [
            line.strip()
            for line in fp.readlines()
            if not line.startswith('#')
        ]


setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.mail:main',
        ],
    },
    extras_require={
        'dev': get_requirements('dev') + get_requirements('test'),
    },
    install_requires=get_requirements(),
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(
        include=[
            '{{ cookiecutter.project_slug }}',
            '{{ cookiecutter.project_slug }}.*'
        ]
    ),
    setup_requires=get_requirements('setup'),
    test_suite='tests',
    tests_require=get_requirements('test'),
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
