# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['_decimal']
hiddenimports += collect_submodules('decimal')


a = Analysis(
    ['C:\\Users\\HHS\\Desktop\\CLEAN_FOLDER\\Clean_Folder.py'],
    pathex=[],
    binaries=[('C:\\Users\\HHS\\AppData\\Local\\Programs\\Python\\Python39\\DLLs\\_decimal.pyd', '.')],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Clean_Folder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
