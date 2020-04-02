
from setuptools import setup


def main():

    setup(
        name='gadgetapp',
        packages=['gadgetapp'],
        package_dir={'': 'src'},
        version=open('VERSION.txt').read().strip(),
        author='Stuart Lynne',
        author_email='stuart.lynne@gmail.com',
        url='http://github.com/Belarra/gadgetapp',
        download_url='http://github.com/Belarra/gadgetapp.git',
        license='MIT',
        keywords=['usb', 'gadget'],
        description='gadgetapp implements a simple GUI application to configure Gadget USB Devices',
        entry_points={'console_scripts': ['gadgetapp = gadgetapp:main', ], },
        install_requires=["argparse", "inotify", "termcolor", "python-magic", "sysfstree", "gadgetconfig"],
        classifiers=[
            "Programming Language :: Python",
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Operating System :: POSIX",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Topic :: System :: System Shells",
            "Topic :: System :: Systems Administration",
        ],
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown'

    )


if __name__ == '__main__':
    main()
