from distutils.core import setup

setup(
    name='PyconfBot',
    version='0.2',
    author='Rohith Gilla',
    author_email='gillarohith1@gmail.com',
    scripts=['config.py','main.py'],
    url='https://twitter.com/BotGills/',
    description='Official PyConIndia  Retweet bot.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django",
        "tweepy",
    ],
)