# -*- mode: python -*-

block_cipher = None


a = Analysis(['parsing_message_app_king.py'],
             pathex=['E:\\pycharm-professional-2018.1.3\\Code\\pythonLCDemo\\com\\lc\\demo\\PyQt5Demo\\parsingMessageDemo'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='parsing_message_app_king',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
