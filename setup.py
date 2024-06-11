from setuptools import find_packages, setup

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="show-job",  # Package name
    version="0.1.0",  # Initial release version
    author="Mohammed Ibrahim",
    author_email="mohammedibrahimgaballah@gmail.com",
    description="A brief description of the show-job package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marait123/show-job",  # URL to your package's repo
    # Automatically find and include your packages
    packages=find_packages(),
    classifiers=[
        # Specify the Python versions you support
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose a license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version required
    install_requires=[  # List your package dependencies here
        # e.g., 'requests', 'numpy',
        "pre-commit == 3.5.0",
    ],
    entry_points={
        "console_scripts": [
            "show-job=show_job.show_job:main",  # Define the console script
        ],
    },
    # Include additional files specified in MANIFEST.in
    include_package_data=True,
)
