from setuptools import setup
from setuptools import find_packages
import os

package_name = 'launcher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='romeperl',
    maintainer_email='romeperl@umd.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "xacro_urdf_viewer = launcher.xacro_urdf:main",
            "kicker = launcher.kicker:main"
        ],
    },
)
