from setuptools import setup

setup(
    name="translator-knowledge-beacon",
    url="https://github.com/NCATS-Tangerine/translator-knowledge-beacon",
    version = "1.3.0",
    packages = ['beacon_controller', 'config'],
    include_package_data=True,
    install_requires=[
        'BiolinkMG',
        'tornado',
        'requests',
        'flask',
        'pyyaml',
        'connexion == 1.1.15',
        'python_dateutil == 2.6.0',
        'setuptools >= 21.0.0'
    ]
)
