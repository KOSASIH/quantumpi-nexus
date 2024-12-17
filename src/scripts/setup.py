# setup.py

from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    packages=find_packages(where='main'),
    package_dir={'': 'main'},
    install_requires=[
        'flask',  # Example dependency
        'sqlalchemy',  # Example dependency
        'alembic',  # Example dependency for migrations
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',  # Replace with your command and function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
