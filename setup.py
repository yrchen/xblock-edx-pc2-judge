from setuptools import setup

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
)
