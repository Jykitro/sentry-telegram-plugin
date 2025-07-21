#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

from sentry_telegram_plugin import __version__


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='sentry_telegram_plugin',
    version=__version__,
    packages=['sentry_telegram_plugin'],
    url='https://github.com/Jykitro/sentry-telegram',
    author='Jykitro',
    author_email='denisbodrov705@gmail.com',
    description='Plugin for Sentry which allows sending notification via Telegram messenger.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    entry_points={
        'sentry.plugins': [
            'sentry_telegram_plugin = sentry_telegram_plugin.plugin:TelegramNotificationsPlugin',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: System :: Monitoring',
    ],
    include_package_data=True,
)
