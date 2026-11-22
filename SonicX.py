# Copyright (c) SonicX
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|

from Program.Config.Config import *
from Program.Config.Util import *

try:
   import webbrowser
   import re
   import sys
   import os
except Exception as e:
   ErrorModule(e)

# ----------------- Tools Definition -----------------
option_site = "Site"
option_info = "Info"

# Helper for string padding ignoring ANSI escape codes
def strip_ansi(text):
   return re.sub(r'\x1b\[[0-9;]*m', '', text)

def pad_cell(text, width, align='left'):
   vis_len = len(strip_ansi(text))
   padding = max(0, width - vis_len)
   if align == 'center':
      left_pad = padding // 2
      right_pad = padding - left_pad
      return ' ' * left_pad + text + ' ' * right_pad
   elif align == 'right':
      return ' ' * padding + text
   else:
      return text + ' ' * padding

# ----------------- Menu Builder -----------------
c1_w = 34
c2_w = 35
c3_w = 33

# Column 1: OSINT Intelligence (Reordered)
c1_items = [
   ('01', 'Username Tracker', 'Username-Tracker'),
   ('02', 'Instagram OSINT', 'Instagram-Account'),
   ('03', 'Phone Number Lookup', 'Phone-Number-Lookup'),
   ('04', 'Email Tracker', 'Email-Tracker'),
   ('05', 'Email Lookup', 'Email-Lookup'),
   ('06', 'IP Geolocation', 'Ip-Lookup'),
   ('07', 'Google Dorking', 'Google-Dorking'),
   ('08', 'Exif Image Metadata', 'Get-Image-Exif'),
   ('09', 'D0x Tracker', 'D0x-Tracker'),
   ('10', 'D0x Create', 'D0x-Create'),
]

# Column 2: Utilities & Tools (Reordered)
c2_items = [
   ('11', 'Database Search', 'Search-In-DataBase'),
   ('12', 'Dark Web Links', 'Dark-Web-Links'),
   ('13', 'Hash Decryptor', 'Password-Hash-Decrypted-Attack'),
   ('14', 'Hash Encryptor', 'Password-Hash-Encrypted'),
   ('15', 'Zip Password Crack', 'Password-Zip-Cracked-Attack'),
   ('16', 'IP Generator', 'Ip-Generator'),
   ('17', 'Phishing Attack', 'Phishing-Attack'),
   ('', '', ''),
   ('', '', ''),
   ('', '', ''),
]

# Column 3: Network Scanner (Reordered)
c3_items = [
   ('18', 'IP Port Scanner', 'Ip-Port-Scanner'),
   ('19', 'IP Pinger', 'Ip-Pinger'),
   ('20', 'IP Range Scanner', 'Ip-Scanner'),
   ('21', 'Website Vuln Scanner', 'Website-Vulnerability-Scanner'),
   ('22', 'Website Info Scanner', 'Website-Info-Scanner'),
   ('23', 'Website URL Scanner', 'Website-Url-Scanner'),
   ('', '', ''),
   ('', '', ''),
   ('', '', ''),
   ('', '', ''),
]

def fmt_item(num, name, width):
   if not num:
      return ' ' * width
   content = f' {cyan}[{white}{num}{cyan}]{white} {name}'
   return pad_cell(content, width, 'left')

top = ' ╭' + '─'*c1_w + '┬' + '─'*c2_w + '┬' + '─'*c3_w + '╮'
mid = ' ├' + '─'*c1_w + '┼' + '─'*c2_w + '┼' + '─'*c3_w + '┤'
bot = ' ╰' + '─'*c1_w + '┴' + '─'*c2_w + '┴' + '─'*c3_w + '╯'

h1 = pad_cell(f'{cyan}» {white}OSINT INTELLIGENCE{cyan} «{reset}', c1_w, 'center')
h2 = pad_cell(f'{cyan}» {white}UTILITIES & TOOLS{cyan} «{reset}', c2_w, 'center')
h3 = pad_cell(f'{cyan}» {white}NETWORK SCANNER{cyan} «{reset}', c3_w, 'center')
header = f' │{h1}│{h2}│{h3}│'

rows = []
for i in range(10):
   i1 = fmt_item(c1_items[i][0], c1_items[i][1], c1_w)
   i2 = fmt_item(c2_items[i][0], c2_items[i][1], c2_w)
   i3 = fmt_item(c3_items[i][0], c3_items[i][1], c3_w)
   rows.append(f' │{i1}│{i2}│{i3}│')

total_w = c1_w + c2_w + c3_w + 2
top_bar_top = ' ╭' + '─'*total_w + '╮'
top_items = f'   {cyan}[{white}I{cyan}] {white}System Info       {cyan}[{white}S{cyan}] {white}Official Site       {cyan}[{white}0{cyan}] {white}Refresh       {cyan}[{white}X{cyan}] {white}Exit{reset}'
padded_top = pad_cell(top_items, total_w, 'left')
top_bar_mid = f' │{padded_top}│'
top_bar_bot = ' ╰' + '─'*total_w + '╯'

menu_layout = MainColor('\n'.join([
   top_bar_top,
   top_bar_mid,
   top_bar_bot,
   top,
   header,
   mid,
   *rows,
   bot
]))

raw_sonic_art = """.,--::::::--,.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠤⣭⣛⣿⣿⠟⢐⠝⢿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣴⡋⠉⠀⠀⠤⣿⣿⡟⣰⣿⣷⡜⢿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠀⠀⠉⠓⠢⣀⣠⣤⣿⣀⣿⣭⣾⣧⣼⣿⣿⣿⣆⢤⢿⡉⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣾⣿⣿⠟⣡⣍⠻⣾⣿⣿⣿⣿⡇⣿⡋⠀⠀⣒⣒⣒⣒⡒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠿⠟⠋⠉⠉⠉⠿⣿⣿⣿⣿⢸⣿⣿⣧⠹⣿⣿⣿⣿⠿⢌⠀⠠⠤⠴⠶⠶⠦⠤⠤⠤⠤⠤⠤⠤⠤⠄⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠮⠥⠤⠤⢀⠀⣀⡀⠄⠘⣿⡿⣛⣸⣿⣿⡏⢀⢻⡟⡿⣡⣾⡌⠀⢀⣀⣀⣀⣀⣀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡀⠑⠉⣀⡴⠞⠛⢰⣿⣿⢿⣿⣧⣿⣷⡅⣰⣿⠋⢀⣴⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣘⡻⣿⡆⣴⠋⠀⠀⠀⠀⠙⢿⣷⣝⣻⣿⣿⣥⣭⠇⠀⣾⣿⣿⣯⣭⠁⣴⣾⣿⣿⣷⣴⣾⣿⣿⣿⣶⣿⣯⣴⣿⣿⣿⡆
⠀⠀⣠⣶⣿⣿⣿⣞⠁⡛⠒⠂⣀⣤⣶⠾⠷⢠⣝⡛⠛⠛⠉⠀⠀⠀⠻⠿⣿⣿⣿⣶⣿⡿⢹⣿⡿⣿⣿⢯⣿⡿⣿⣿⣿⣿⡏⠉⠁⠀
⠀⢰⣿⣿⣿⣿⣿⠿⣘⣿⡖⣿⠟⠋⠀⣀⢀⣼⢧⣿⣷⡄⠀⣠⣤⣶⣶⣾⣿⣿⡿⣿⣿⣷⣿⣿⣿⣿⡏⣿⣿⣻⣿⣿⣿⣿⣷⣶⠀⠀
⢰⣿⣿⣻⣿⣾⢫⣾⡟⣸⡇⠀⣀⣤⠴⣟⠟⠹⡅⠻⣿⡇⠰⠿⠿⠿⠿⠿⠟⠋⠀⠙⠛⠛⠛⠓⠛⠛⠙⠛⠋⠛⠛⠁⠛⠛⠛⠁⠀⠀
⠘⣿⡻⣷⡭⣡⡿⣫⡜⠉⠀⠀⠁⠀⡼⠁⠀⣸⠇⠀⢈⢣⣶⣦⡄⠀⠀⠠⠤⠴⠞⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠛⠋⠀⠉⠉⠀⠀⠀⠀⠀⠐⠀⣠⠼⠋⠀⠀⠀⠀⠙⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

def Update():
   popup_version = ""
   try:
      new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', requests.get(url_config, timeout=3).text).group(1)
      if new_version != version_tool:
         popup_version = f"{cyan}[{white}!{cyan}] {blue}Update Available: {white + version_tool + blue} -> {white + new_version}\n"
   except: pass
   return popup_version

def BuildBanner():
   popup = Update()
   colored_sonic = SonicBannerColor(raw_sonic_art)
   repo_line = f"                       {blue}» {cyan}{github_tool} {blue}«"
   
   banner = f"""{popup}
{colored_sonic}
{repo_line}

{menu_layout}"""
   return banner

# ----------------- Execution Options (Dynamic Mapping) -----------------
options = {}
for item in c1_items + c2_items + c3_items:
   if item[0] and item[2]:
      options[item[0]] = item[2]

# ----------------- Main Loop -----------------
def main():
   while True:
      try:
         Clear()
         Title("Main Console")
         Slow(BuildBanner())

         prompt = f"""\n {cyan}╭───{blue}[ {cyan}⚡ {white}SonicX {blue}]──{blue}[ {white}~/Main-Console {blue}]──{blue}[ {cyan}{username_pc}{blue}@{white}{os_name} {blue}]
 {cyan}╰──❯{white} {reset}"""
         
         choice = input(prompt).strip()

         if choice in ['I', 'i', 'INFO', 'Info', 'info']:
            StartProgram(f"{option_info}.py")
            continue

         elif choice in ['S', 's', 'SITE', 'Site', 'site']:
            StartProgram(f"{option_site}.py")
            continue

         elif choice in ['X', 'x', 'EXIT', 'Exit', 'exit', 'Q', 'q', 'QUIT', 'Quit']:
            Clear()
            print(f"\n{cyan}[{white}+{cyan}] {white}Thank you for using {cyan}SonicX{white}! Goodbye.{reset}\n")
            sys.exit(0)

         elif choice in ['0', 'CLS', 'cls', 'CLEAR', 'clear']:
            continue

         elif choice in options:
            StartProgram(f"{options[choice]}.py")

         elif ('0' + choice) in options:
            StartProgram(f"{options['0' + choice]}.py")

         else:
            ErrorChoiceStart()

      except KeyboardInterrupt:
         Clear()
         sys.exit(0)
      except Exception as e:
         Error(e)

if __name__ == '__main__':
   main()
