"""Setup configuration"""


from setuptools import setup


setup(
    name="katas",
    description="My solutions to several problems on code wars",
    version=0.1,
    author="Avery Pratt",
    author_email="apratt91@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["trigram"],
    extras_require={
        "test": ["pytest"]
    },
)
