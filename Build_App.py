import PyInstaller.__main__

PyInstaller.__main__.run([
    'Liner_Calculation.py',
    '--onefile',
    '--windowed',
    '--add-data', 'src;src',
    '-i', ".\src\\Liner_Calculation.ico",
    '--splash', ".\src\\Liner_Calculation.png",
])
