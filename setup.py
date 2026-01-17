from setuptools import setup
import os
from glob import glob

package_name = 'tb3_maze_sim'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Install worlds
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.world')),

        # Install models
        (os.path.join('share', package_name, 'models', 'maze_wall'),
            glob('models/maze_wall/*')),

        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='charan',
    maintainer_email='charan@example.com',
    description='TurtleBot3 custom maze simulation with wall follower solver',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wall_follower = tb3_maze_sim.wall_follower:main',
        ],
    },
)

