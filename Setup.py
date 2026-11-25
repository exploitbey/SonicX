# ==============================================================================
#  SonicX Multi-Tools | Geliştirici: expo (https://github.com/exploitbey/SonicX)
#  Not: Bu yazılım eğitim ve yetkili güvenlik testleri amacıyla geliştirilmiştir.
# ==============================================================================
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# TR:
#     - Aşağıdaki koda dokunmayın veya değiştirmeyin. Bir hata oluşursa lütfen geliştirici ile iletişime geçin.
#     - Bu aracı satmayın ve kendi projeniz gibi göstermeyin.


try:
    import sys
    import os

    def OpenSites():
        try:
            import webbrowser
            from Program.Config.Config import telegram, gunslol
            webbrowser.open(f'https://{telegram}')
            webbrowser.open(f'https://{gunslol}')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the SonicX Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        OpenSites()
        os.system("python SonicX.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the SonicX Tool:\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        OpenSites()
        os.system("python3 SonicX.py")

except Exception as e:
    input(e)