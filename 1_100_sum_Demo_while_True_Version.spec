# -*- mode: python -*-

block_cipher = None


a = Analysis(['E:\\pycharm-professional-2018.1.3\\Code\\pythonLCDemo\\com\\lc\\demoKu\\1_100_sum_Demo_while_True_Version.py'],
             pathex=['E:\\pycharm-professional-2018.1.3\\Code\\pythonLCDemo'],
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
          name='1_100_sum_Demo_while_True_Version',
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
               name='1_100_sum_Demo_while_True_Version')
