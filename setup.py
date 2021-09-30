from setuptools import setup



setup(name="PyNeuro",
      version="1.2.1",
      description="Library for connect with Neurosky's Mindwave EEG headset via TCP Socket",
      author="Zach Wang",
      author_email="wangziqi0325@gmail.com",
      long_description=open('INFO.rst', 'r').read(),
      license="MIT",
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
      ],
      url="https://github.com/ZACHSTRIVES/PyNeuro",
      packages=['PyNeuro'],


      )