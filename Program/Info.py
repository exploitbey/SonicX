# ==============================================================================
#  SonicX Multi-Tools | Geliştirici: expo (https://github.com/exploitbey/SonicX)
#  Not: Bu yazılım eğitim ve yetkili güvenlik testleri amacıyla geliştirilmiştir.
# ==============================================================================
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# TR:
#     - Aşağıdaki koda dokunmayın veya değiştirmeyin. Bir hata oluşursa lütfen geliştirici ile iletişime geçin.
#     - Bu aracı satmayın ve kendi projeniz gibi göstermeyin.

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Info")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")

    Slow(f"""
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Name Tool     :  {white}{name_tool}
 {INFO_ADD} Type Tool     :  {white}{type_tool}
 {INFO_ADD} Version       :  {white}{version_tool}
 {INFO_ADD} Copyright     :  {white}{copyright}
 {INFO_ADD} Coding        :  {white}{coding_tool}
 {INFO_ADD} Language      :  {white}{language_tool}
 {INFO_ADD} Creator       :  {white}{creator}
 {INFO_ADD} Platform      :  {white}{platform}
 {INFO_ADD} GunsLol  [W]  :  {white}https://{gunslol}
 {INFO_ADD} GitHub   [W]  :  {white}{github_tool}
 {INFO_ADD} Telegram [W]  :  {white}https://{telegram}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    license_read = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open 'LICENSE' ? (y/n) -> {reset}")
    if license_read in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webbrowser.open_new_tab(license)
    else:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)