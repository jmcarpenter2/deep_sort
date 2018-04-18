from distutils.core import setup
setup(
  name = 'deep_sort_mcdat',
  packages = ['deep_sort_mcdat'], # this must be the same as the name above
  version = '0.1',
  description = 'Customized deep_sort to be aligned with the paper',
  author = 'Jason Carpenter',
  author_email = 'jmcarpenter2@dons.usfca.edu',
  url = 'https://github.com/jmcarpenter2/deep_sort_mcdat', # use the URL to the github repo
  download_url = 'https://github.com/jmcarpenter2/deep_sort_mcdat/archive/0.1.tar.gz',
  install_requires=[
        'numpy',
        'scipy',
        'sklearn',
        'opencv-python'
  ],
  classifiers = [],
)
