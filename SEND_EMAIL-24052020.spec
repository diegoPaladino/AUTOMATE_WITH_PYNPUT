# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['SEND_EMAIL-24052020.py'],
             pathex=['C:\\Users\\Diego\\Desktop\\TESTE_BOT\\AUTOMATE_WITH_PYNPUT\\AUTOMATE_WITH_PYNPUT\\AUTOMATE_WITH_PYNPUT'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          [],
          exclude_binaries=True,
          name='SEND_EMAIL-24052020',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SEND_EMAIL-24052020')


----
