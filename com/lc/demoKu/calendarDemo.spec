# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\all_develop_soft\\pycharm-professional-2018.1.3\\codeKu\\pythonLCDemo\\com\\lc\\demoKu\\calendarDemo.py'],
             pathex=['D:\\all_develop_soft\\pycharm-professional-2018.1.3\\codeKu\\pythonLCDemo\\com\\lc\\demoKu'],
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
          name='calendarDemo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
