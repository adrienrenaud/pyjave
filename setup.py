from distutils.core import setup
setup(
  name = 'pyjave',
  packages = ['pyjave'], # this must be the same as the name above
  version = '0.1',
  description = 'PLotly and Pandas tools',
  author = 'Adrien Renaud',
  author_email = 'adrien.renaud@gmail.com',
  url = 'https://github.com/adrienrenaud/pyjave', # use the URL to the github repo
  download_url = 'https://github.com/adrienrenaud/pyjave/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['pandas', 'plotly'], # arbitrary keywords
  classifiers = [],
  install_requires = ['pandas', 'plotly>=2.0.0', 'scipy>=0.19.1'],
)