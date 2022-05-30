# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['..\\..\\tests\\install_test.py'],
             pathex=['C:\\Users\\guyst\\Documents\\NetAdmin\\source\\server\\../shared'],
             binaries=[('lib_bin\\turbojpeg-bin\\turbojpeg.dll', '.')],
             datas=[],
             hiddenimports=['win32com.client', 'win32api', 'win32con', 'win32timezone'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='install_test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir='.',
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
