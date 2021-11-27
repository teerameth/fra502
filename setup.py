import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'fra502'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch, urdf, world files
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('urdf/*')),
        (os.path.join('share', package_name), glob('world/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='teera',
    maintainer_email='teerameth.sk@gmail.com',
    description='FRA502 Project',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
