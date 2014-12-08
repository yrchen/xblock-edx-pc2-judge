import os
from setuptools import setup

def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name='xblock-edx-pc2-judge',
    version='0.1',
    description='Edx-Pc2-Judge XBlock Tutorial Sample',
    py_modules=['edxpc2judge'],
    install_requires=['XBlock', 'requests'],
    entry_points={
        'xblock.v1': [
            'edxpc2judge = edxpc2judge:EdxPc2JudgeBlock',
        ]
    }
    packages=[
        'edxpc2judge',
    ],
    include_package_data=True,
    package_data=package_data("edxpc2judge", "static"),
)
