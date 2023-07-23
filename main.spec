# type: ignore
# pylint: disable=all

from os.path import join
from site import getsitepackages

block_cipher = None

analysis = Analysis(
    ['main.py'],
    binaries = [
        (join(getsitepackages()[-1], 'ctransformers'), 'ctransformers')
    ],
    datas = [
        ('bin', 'bin'),
        ('server\\features\\generator\\templates\\main.txt', 'server\\features\\generator\\templates')
        ('out\\wingman.vsix', 'out'),
    ],
    pathex = [],
    hiddenimports = [],
    hookspath = [],
    hooksconfig = {},
    runtime_hooks = [],
    excludes = [],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    analysis.pure,
    analysis.zipped_data,
    cipher=block_cipher
)

EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.zipfiles,
    analysis.datas,
    name='Wingman',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
