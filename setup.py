from setuptools import setup

setup(
    name="acolyte",
    packages=["acolyte"],
    include_package_data=True,
    install_requires=[
        "discord-py",
        "python-dotenv",
        "ffmpeg-python"
    ]
)
