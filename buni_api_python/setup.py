from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="buni_api_client", # Name of the package on PyPI
    version="1.0.0",
    author="Your Name / Organization", # Replace with actual author
    author_email="your.email@example.com", # Replace with actual email
    description="A Python client for the KCB Buni API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/buni_api_python", # Replace with your repo URL
    packages=find_packages(exclude=["examples", "tests"]), # Exclude examples and tests from package
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # Assuming MIT, change if different
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", # Or another appropriate status
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires='>=3.7', # Based on f-strings and type hints used
    project_urls={ # Optional
        "Bug Tracker": "https://github.com/yourusername/buni_api_python/issues",
        "Source Code": "https://github.com/yourusername/buni_api_python",
    },
    include_package_data=False, # If you have non-code files inside your package dir
)
