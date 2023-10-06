from setuptools import setup, find_packages

setup(
    name='Xnotepad',
    version='0.0.1',
    packages=find_packages(), 
    install_requires=[
        
        'PyQt5',
        'fastapi',
    ],
    entry_points={
        'console_scripts': [
            # اسکریپت‌هایی که می‌خواهید به عنوان اسکریپت اجرایی نصب شوند
            'xnotepad = xnotepad.main:main',
        ],
    },
    author='M . Ali Anbarloo',  # نام نویسنده
    description='A simple notepad application',  # توضیحات پروژه
)
