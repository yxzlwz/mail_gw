from setuptools import setup

setup(
    name='mail_gw',
    version='0.4',
    description='Tempmail Python SDK of https://api.mail.gw/',
    url="https://github.com/Danny-Yxzl/mail_gw",
    author="Yixiangzhilv",
    author_email="mail@yixiangzhilv.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords="API sdk tempmail",
    install_requires=["requests"],
    packages=["mail_gw"],
    project_urls={
        "Bug Reports": "https://github.com/Danny-Yxzl/mail_gw/issues",
        "Say Thanks!": "https://www.yixiangzhilv.com/",
        "Source": "https://github.com/Danny-Yxzl/mail_gw",
    },
)
