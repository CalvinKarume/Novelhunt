from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "NovelHunt"
AUTHOR_USER_NAME = "Calvin Karume"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=Calvin_Karume,
    description="A book Recommender system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/CalvinKarume/NovelHunt",
    author_email="johncalvinkarume@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)