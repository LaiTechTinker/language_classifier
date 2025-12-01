from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="zuba",
    version="0.0.4",
    packages=find_packages(),
    install_requires=[
        "torch",
        "tiktoken",
        "huggingface_hub",
        "transformers",
        "requests",           # for downloading the model
        
    ],
    include_package_data=True,  #
    package_data={"Zuba": ["model/*.pth"]},  # include the model folder
    author="Ibrahim Olayiwola",
    description="A lightweight Nigerian language classifier.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.12"
)
