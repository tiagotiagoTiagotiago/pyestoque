import cx_Freeze

executables = [cx_Freeze.Executable('PyStock - App.py', icon='View/Imagens/Logo Ico.ico', base='Win32GUI')]

cx_Freeze.setup(
    name="PyStock",
    options={'build_exe': {'packages': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'mysql.connector', 'os', 'sys', 'openpyxl.drawing.image', 'datetime', 'time', 'tkinter.filedialog', 'openpyxl'],
                           'include_files': ['View/', 'Base xls.xlsx']}},
    executables=executables
)