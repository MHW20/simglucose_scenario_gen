from setuptools import setup

setup(
    name="simglucose_scenario_gen",
    version="0.3.0",
    description="A Type-1 Diabetes Simulator as a Reinforcement Learning Environment in OpenAI gym or rllab (python implementation of UVa/Padova Simulator)",
    url="https://github.com/MHW20/simglucose_scenario_gen",
    author="Jinyu Xie, Matthew Hanna",
    author_email="xjygr08@gmail.com, matthewhanna70@gmail.com",
    license="MIT",
    packages=["simglucose"],
    install_requires=[
        "gym==0.9.4",
        "gymnasium~=0.29.1",
        "pathos>=0.3.1",
        "scipy>=1.11.0",
        "matplotlib>=3.7.2",
        "numpy>=1.25.0",
        "pandas>=2.0.3",
    ],
    include_package_data=True,
    zip_safe=False,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
