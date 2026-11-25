# ==============================================================================
#  SonicX Multi-Tools | Geliştirici: expo (https://github.com/exploitbey/SonicX)
#  Not: Bu yazılım eğitim ve yetkili güvenlik testleri amacıyla geliştirilmiştir.
# ==============================================================================
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# TR:
#     - Aşağıdaki koda dokunmayın veya değiştirmeyin. Bir hata oluşursa lütfen geliştirici ile iletişime geçin.
#     - Bu aracı satmayın ve kendi projeniz gibi göstermeyin.

from .Config import *
try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import sys
    import requests
    import random
except Exception as e:
    print(f'Modules of the python library required for SonicX are not installed, make sure you have correctly installed python and have launched the "Setup.py" file which will install all the necessary modules.')
    input(f'Error: {e}')

color = colorama.Fore
blue = color.BLUE
white = color.WHITE
green = color.GREEN
reset = color.RESET
red = color.RED
yellow = color.YELLOW
cyan = color.CYAN
magenta = color.MAGENTA

try: username_pc = os.getlogin()
except: username_pc = "username"

try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "None"

tool_path = os.path.dirname(os.path.abspath(__file__)).split("Program\\")[0].split("Program/")[0].strip()

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{blue}[{white}'
AFTER = f'{blue}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'
NOTE = f'{BEFORE}NOTE{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{blue}+{white}]{blue}'

def Censored(text):
    censored = [w for w in [website] if w and w.lower() != "none"]
    for censored_text in censored:
        if text in censored or censored_text in text:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()

def Title(title):
    if os_name == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} - {title}")
    elif os_name == "Linux":
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} - {title}\x07")
        
def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

def Reset():
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "SonicX.py")]
        subprocess.run(file)

    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "SonicX.py")]
        subprocess.run(file)

def StartProgram(program):
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)
        
    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)

def Slow(text):
    delay = 0.03
    lines = text.split('\n')
    for line in lines:
        print(line)
        time.sleep(delay)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid ID !", reset)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid URL !", reset)
    time.sleep(3)
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)
    Reset()

def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number !", reset)
    time.sleep(3)
    Reset()

def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Username !", reset)
    time.sleep(3)
    Reset()

def ErrorPlatform():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Unsupported Platform !", reset)
    time.sleep(3)
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error Module: {white}{e}", reset)
    Continue()
    Reset()

def OnlyWindows():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Windows 10/11 !", reset)
    Continue()
    Reset()

def OnlyLinux():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Linux !", reset)
    Continue()
    Reset()

def SonicBannerColor(text):
    palette = [
        (0, 240, 255),
        (0, 215, 255),
        (0, 190, 255),
        (0, 165, 255),
        (0, 140, 255),
        (0, 115, 255),
        (0, 95, 245),
        (20, 75, 235),
        (0, 95, 245),
        (0, 115, 255),
        (0, 140, 255),
        (0, 165, 255),
        (0, 190, 255),
        (0, 215, 255),
    ]
    lines = text.split('\n')
    out = []
    for i, l in enumerate(lines):
        chars = []
        for j, c in enumerate(l):
            if c not in (' ', '\t', '⠀'):
                idx = (i + j // 2) % len(palette)
                r, g, b = palette[idx]
                chars.append(f"\033[38;2;{r};{g};{b}m{c}\033[0m")
            else:
                chars.append(c)
        out.append(''.join(chars))
    return '\n'.join(out)

def MainColor(text):
    start_color = (0, 140, 255)  
    end_color = (0, 235, 255)

    num_steps = 10

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    gradient_chars = '┴┼┘┤└┐─┬├┌└│]░▒░▒█▓▄▌▀()╭╮╰╯═║╔╗╚╝╠╣╦╩╬»«'
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in gradient_chars:
                color_index = (i + j) % num_colors
                color = colors[color_index]
                result.append(text_color(*color) + char + "\033[0m")
            else:
                result.append(char)
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)

def MainColor2(text):
    start_color = (0, 102, 255)  
    end_color = (102, 178, 255)

    num_steps = 9

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]
            result.append(text_color(*color) + char + "\033[0m")
        
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)

def ChoiceUserAgent():
    file_user_agent = os.path.join(tool_path, "2-Input", "Headers", "UserAgent.txt")

    with open(file_user_agent, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        user_agent = random.choice(lines).strip()
    else:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36"
    
    return user_agent

tor_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // DARK WEB ]═══════════════════════════════════════[ ONION NODE ]═╗
  ║     .---.     │  ██████╗  █████╗ ██████╗ ██╗  ██╗  ██╗    ██╗███████╗██████╗   ║
  ║    / .-. \    │  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝  ██║    ██║██╔════╝██╔══██╗  ║
  ║   | ( @ ) |   │  ██║  ██║███████║██████╔╝█████╔╝   ██║ █╗ ██║█████╗  ██████╔╝  ║
  ║    \ `-' /    │  ██║  ██║██╔══██║██╔══██╗██╔═██╗   ██║███╗██║██╔══╝  ██╔══██╗  ║
  ║     `---'     │  ██████╔╝██║  ██║██║  ██║██║  ██╗  ╚███╔███╔╝███████╗██████╔╝  ║
  ║    [ TOR ]    │  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚══╝╚══╝ ╚══════╝╚═════╝   ║
  ╚════════════════════════[ github.com/exploitbey/SonicX ]════════════════════════╝
""")

dox_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // DOX ENGINE ]════════════════════════════════════════════[ DOSSIER ]═╗
  ║    ┌─────┐    │  ██████╗  ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗       ║
  ║    │ (●) │    │  ██╔══██╗██╔═══██╗╚██╗██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║       ║
  ║    │ ─── │    │  ██║  ██║██║   ██║ ╚███╔╝        ██║   ██║   ██║██║   ██║██║       ║
  ║    │ ─── │    │  ██║  ██║██║   ██║ ██╔██╗        ██║   ██║   ██║██║   ██║██║       ║
  ║    └─────┘    │  ██████╔╝╚██████╔╝██╔╝ ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗  ║
  ║    [ DOX ]    │  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  ║
  ╚══════════════════════════[ github.com/exploitbey/SonicX ]══════════════════════════╝
""")

osint_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // OSINT INTEL ]═════════════════════════════════════[ RECON ]═╗
  ║      .-.      │   ██████╗ ███████╗██╗███╗   ██╗████████╗    ██╗  ██╗       ║
  ║    .(   ).    │  ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ╚██╗██╔╝       ║
  ║   (  (◎)  )   │  ██║   ██║███████╗██║██╔██╗ ██║   ██║        ╚███╔╝        ║
  ║    `-( )-'    │  ██║   ██║╚════██║██║██║╚██╗██║   ██║        ██╔██╗        ║
  ║       |       │  ╚██████╔╝███████║██║██║ ╚████║   ██║       ██╔╝ ██╗       ║
  ║   [ OSINT ]   │   ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝       ║
  ╚══════════════════════[ github.com/exploitbey/SonicX ]══════════════════════╝
""")

wifi_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // IP PINGER ]═══════════════════════════════════════════[ SIGNAL ]═╗
  ║    .-----.    │  ██╗██████╗     ██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗   ║
  ║   / .---. \   │  ██║██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗  ║
  ║  | /  .  \ |  │  ██║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝  ║
  ║      (●)      │  ██║██╔═══╝     ██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗  ║
  ║      /|\      │  ██║██║         ██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║  ║
  ║    [ ICMP ]   │  ╚═╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ║
  ╚════════════════════════[ github.com/exploitbey/SonicX ]═════════════════════════╝
""")

phishing_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // WEB CLONER ]══════════════════════════════════════[ MIRROR ]═╗
  ║       |       │  ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗   ║
  ║       |       │  ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝   ║
  ║       |       │  ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗  ║
  ║     \ |       │  ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║  ║
  ║      `J       │  ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝  ║
  ║    [ HTML ]   │  ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝   ║
  ╚══════════════════════[ github.com/exploitbey/SonicX ]═══════════════════════╝
""")

decrypted_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // DECRYPTOR ]════════════════════════════════════════[ UNLOCK ]═╗
  ║      .---.    │  ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗  ║
  ║     /         │  ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝  ║
  ║     ┌─────┐   │  ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║     ║
  ║     │ [O] │   │  ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║     ║
  ║     └─────┘   │  ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║     ║
  ║   [ CRACK ]   │  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝     ║
  ╚═══════════════════════[ github.com/exploitbey/SonicX ]═══════════════════════╝
""")

encrypted_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // ENCRYPTOR ]══════════════════════════════════════════[ CIPHER ]═╗
  ║      .---.    │  ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗  ║
  ║      |   |    │  ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝  ║
  ║     ┌─────┐   │  █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║     ║
  ║     │ [X] │   │  ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║     ║
  ║     └─────┘   │  ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║     ║
  ║   [ HASH ]    │  ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝     ║
  ╚════════════════════════[ github.com/exploitbey/SonicX ]════════════════════════╝
""")

scan_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // NET SCANNER ]═════════════════════════════════════════[ RADAR ]═╗
  ║     .---.     │  ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗   ║
  ║    /  |  \    │  ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗  ║
  ║   |--(+)--|   │  ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝  ║
  ║    \  |  /    │  ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗  ║
  ║     `---'     │  ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║  ║
  ║   [ SCAN ]    │  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ║
  ╚════════════════════════[ github.com/exploitbey/SonicX ]════════════════════════╝
""")

sql_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // VULN SCAN ]═══════════════════════════════════════════════════════[ AUDIT ]═╗
  ║     _____     │  ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗  ███████╗ ██████╗ █████╗ ███╗   ██╗  ║
  ║    /     \    │  ██║   ██║██║   ██║██║     ████╗  ██║  ██╔════╝██╔════╝██╔══██╗████╗  ██║  ║
  ║    | [!] |    │  ██║   ██║██║   ██║██║     ██╔██╗ ██║  ███████╗██║     ███████║██╔██╗ ██║  ║
  ║    \  ▼  /    │  ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║  ╚════██║██║     ██╔══██║██║╚██╗██║  ║
  ║     `---'     │   ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║  ███████║╚██████╗██║  ██║██║ ╚████║  ║
  ║   [ AUDIT ]   │    ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ║
  ╚══════════════════════════════[ github.com/exploitbey/SonicX ]══════════════════════════════╝
""")

map_banner = SonicBannerColor(r"""
  ╔═[ ⚡ SONIC-X // IP GEOMAP ]══════════════════════════════════════════[ GPS ]═╗
  ║     .---.     │   ██████╗ ███████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗   ║
  ║    /  ◎  \    │  ██╔════╝ ██╔════╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗  ║
  ║    \     /    │  ██║  ███╗█████╗  ██║   ██║    ██╔████╔██║███████║██████╔╝  ║
  ║     \   /     │  ██║   ██║██╔══╝  ██║   ██║    ██║╚██╔╝██║██╔══██║██╔═══╝   ║
  ║       v       │  ╚██████╔╝███████╗╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║       ║
  ║    [ GEO ]    │   ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝       ║
  ╚══════════════════════[ github.com/exploitbey/SonicX ]═══════════════════════╝
""")
