import subprocess
import threading
import os

def execution(reportName):
    i = 1
    while True:
        if os.path.isfile(f'{reportName}_{i}.html'):
            i += 1
        else:
            break
    subprocess.run(
        f'cmd /c "call pytest -s -v Test_case.py --html={reportName}_{i}.html --capture=tee-sys --disable-pytest-warnings --self-contained-html"')

if __name__ == '__main__':
    # threading.Thread(target=execution, args='chrome').start()
    threading.Thread(target=execution, args=('firefox',)).start()




