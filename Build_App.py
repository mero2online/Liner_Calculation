import PyInstaller.__main__

PyInstaller.__main__.run([
    'Cement_Calculation.py',
    '--onefile',
    '--windowed',
    # '--add-data', 'src;src',
    # '-i', ".\src\\Cement_Calculation.ico",
    # '--splash', ".\src\\Cement_Calculation.png",
])
