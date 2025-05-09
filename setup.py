from setuptools import setup, find_packages

setup(
    name="ai-ecommerce-assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "transformers>=4.15.0",
        "torch>=1.10.0",
        "fastapi>=0.70.0",
        "uvicorn>=0.15.0",
        "python-dotenv>=0.19.0",
        "redis>=4.0.0",
        "sqlalchemy>=1.4.0",
        "shopify-python-api>=9.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.9b0",
            "isort>=5.9.3",
            "flake8>=3.9.2",
        ],
    },
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="A modular AI-integrated library for e-commerce websites",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-ecommerce-assistant",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 