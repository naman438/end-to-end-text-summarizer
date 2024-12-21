import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"

REPO_NAME= "end-to-end-text-summarizer"
AUTHOR_USER_NAME="naman438"
SRC_REPO="text_summarizer"
AUTHOR_EMAIL="namankundra422@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for text summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)