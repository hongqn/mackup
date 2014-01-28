import distutils.core

import mackup.main


distutils.core.setup(
    name='Mackup',
    version=mackup.main.VERSION,
    author='Laurent Raufaste',
    author_email='analogue@glop.org',
    url='https://github.com/lra/mackup',
    description='Keep your application settings in sync (OS X/Linux)',
    license='GPLv3',
    packages=['mackup'],
    scripts=['bin/mackup'],
    package_data={'mackup': ['applications/*.cfg']},
)
