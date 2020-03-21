from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup, find_packages


_VERSION = '0.0.1'

REQUIRED_PACKAGES = [
    'numpy >= 1.18.2',
    'matplotlib >= 3.2.1',
    'psutil >= 5.4.5',
    'opencv-python >= 4.2.0',
    'scipy >= 1.4.1',
    'scikit-image >= 0.16.2',
    'tqdm >= 4.43.0',
]

setup(
    name='pytorch_openpose',
    version=_VERSION,
    description=
    'Deep Pose Estimation implemented using pytorch',
    install_requires=REQUIRED_PACKAGES,
    url='https://github.com/alexus37/pytorch-openpose',
    author='Alexander Lelidis',
    author_email='alelidis@student.ethz.ch',
    license='Apache License 2.0',
    # check this
    package_dir={
        'torch_pose_data': 'model'
    },
    packages=['torch_pose_data'] + [pkg_name for pkg_name in setuptools.find_packages()  # main package
            if 'torch_openpose' in pkg_name],
    package_data={
        'torch_pose_data': ['model/body_pose_model.pth', 'model/hand_pose_model.pth']
    },
    zip_safe=False
)
