#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"icons"
APPS=["org.gnome.Nautilus","org.gnome.Settings","org.gnome.Terminal","org.gnome.Software","org.gnome.Calendar","org.gnome.clocks","org.gnome.Calculator","org.gnome.TextEditor","org.gnome.Loupe","org.gnome.Evince","org.gnome.Totem","org.gnome.Music","org.gnome.Weather","org.gnome.Contacts","org.gnome.Maps","org.gnome.Characters","org.gnome.DiskUtility","org.gnome.SystemMonitor","org.gnome.Extensions","org.gnome.tweaks","org.gnome.Screenshot","org.gnome.Console","org.gnome.font-viewer","org.gnome.Boxes","org.gnome.Connections","org.gnome.DejaDup","org.gnome.Logs","org.gnome.PowerStats","org.gnome.Ptyxis","org.gnome.baobab","org.gnome.Epiphany","org.mozilla.firefox","org.gnome.GNOME"]
SYMBOLS={
"application-exit":"<path d='M5 5l14 14M19 5 5 19'/>","go-home":"<path d='m3 11 9-8 9 8v9h-6v-6H9v6H3z'/>","go-previous":"<path d='m14 5-7 7 7 7M7 12h14'/>","go-next":"<path d='m10 5 7 7-7 7M17 12H3'/>","edit-copy":"<rect x='8' y='8' width='12' height='13' rx='2'/><path d='M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h3'/>","edit-cut":"<circle cx='6' cy='6' r='3'/><circle cx='6' cy='18' r='3'/><path d='m8 8 12 12m0-17L8 15'/>","edit-paste":"<rect x='5' y='5' width='14' height='17' rx='2'/><path d='M9 5V3h6v2M9 11h6'/>","list-add":"<path d='M12 5v14M5 12h14'/>","list-remove":"<path d='M5 12h14'/>","view-refresh":"<path d='M20 7v5h-5M4 17v-5h5M5 9a7 7 0 0 1 13-3M4 12a7 7 0 0 0 13 6'/>","view-grid":"<rect x='3' y='3' width='8' height='8' rx='1'/><rect x='13' y='3' width='8' height='8' rx='1'/><rect x='3' y='13' width='8' height='8' rx='1'/><rect x='13' y='13' width='8' height='8' rx='1'/>","view-list":"<path d='M9 5h12M9 12h12M9 19h12'/><circle cx='4' cy='5' r='1'/><circle cx='4' cy='12' r='1'/><circle cx='4' cy='19' r='1'/>","system-search":"<circle cx='10.5' cy='10.5' r='6.5'/><path d='m16 16 5 5'/>","preferences-system":"<circle cx='12' cy='12' r='3'/><path d='M19 13a7 7 0 0 0 0-3l2-2-2-3-3 1-3-2-1-3H9L8 4 5 6 2 5 1 9l2 2v3l-2 2 2 3 3-1 3 2 1 3h4l1-3 3-2 3 1 2-3z'/>","dialog-information":"<circle cx='12' cy='12' r='9'/><path d='M12 11v6m0-10h.01'/>","dialog-warning":"<path d='M12 3 2 21h20z'/><path d='M12 9v5m0 3h.01'/>","dialog-error":"<circle cx='12' cy='12' r='9'/><path d='m9 9 6 6m0-6-6 6'/>","network-wireless":"<path d='M2 8a16 16 0 0 1 20 0M5 12a11 11 0 0 1 14 0m-11 4a6 6 0 0 1 8 0m-4 4h.01'/>","audio-volume-high":"<path d='M3 9v6h4l5 4V5L7 9zM16 9a5 5 0 0 1 0 6'/>","battery-full":"<rect x='2' y='7' width='18' height='10' rx='2'/><path d='M22 10v4M5 10h12v4H5z'/>","bluetooth":"<path d='m7 7 10 10-5 4V3l5 4L7 17'/>","media-playback-start":"<path d='m7 4 14 8-14 8z'/>","media-playback-pause":"<path d='M7 4h4v16H7zM15 4h4v16h-4z'/>","media-playback-stop":"<rect x='5' y='5' width='14' height='14' rx='1'/>","lock":"<rect x='4' y='10' width='16' height='11' rx='2'/><path d='M8 10V7a4 4 0 1 1 8 0v3'/>","unlock":"<rect x='4' y='10' width='16' height='11' rx='2'/><path d='M8 10V7a4 4 0 0 1 8 0'/>","user-trash":"<path d='M4 7h16M9 7V4h6v3m-9 0 1 14h10l1-14'/>","folder":"<path d='M3 6h7l2 2h9v11H3z'/>","document-new":"<path d='M6 3h8l4 4v14H6zM14 3v5h5M12 11v7m-3-3h6'/>","document-save":"<path d='M4 3h14l3 3v15H4zM8 3v6h8V3M8 21v-7h8v7'/>","printer":"<path d='M6 8V3h12v5M6 17H4V9h16v8h-2M6 14h12v7H6z'/>","camera-photo":"<path d='M3 8h5l2-3h4l2 3h5v12H3z'/><circle cx='12' cy='14' r='4'/>","starred":"<path d='m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9z'/>","window-close":"<path d='m6 6 12 12M18 6 6 18'/>","window-maximize":"<rect x='3' y='4' width='18' height='16' rx='2'/><path d='M3 9h18'/>","zoom-in":"<circle cx='10.5' cy='10.5' r='6.5'/><path d='M10.5 7v7m-3.5-3.5h7m2 2 5 5'/>"}
LOGO="""<svg xmlns="http://www.w3.org/2000/svg" width="416" height="512" viewBox="0 0 256 315" preserveAspectRatio="xMidYMid meet"><title>GNOME foot logo</title><path fill="#000000" d="M210.658 136.723c10.613 63.064-150.402 86.092-89.773 132.253 19.046 14.5 38.493 3.392 35.547-19.101-2.458-18.766 65.957-30.13 60.598-1.77-7.016 37.191-44.519 66.55-77.033 66.55-66.092 0-129.432-76.857-117.052-132.256 18.29-81.907 178.903-98.023 187.713-45.676m-180.2-7.804c-13.944 6.136-45.617-33.426-21.915-49.803 23.712-16.374 35.86 43.665 21.916 49.803M69.75 97.493c-16.586 3.39-41.7-47.043-12.093-59.261C87.26 26.016 86.35 94.109 69.75 97.493ZM229.01 0c65.46 0-4.095 93.234-40.914 93.234C151.27 93.234 163.55 0 229.008 0M120.315 81.68c-19.615-1.196-32.57-65.26 4.268-70.042 36.85-4.781 15.339 71.24-4.268 70.043Z"/></svg>"""
def main():
 for theme,fg in (("G-OS","#394354"),("G-OS-dark","#e8edf5")):
  base=ROOT/theme
  dirs=("512x512/apps","scalable/apps","scalable/actions","scalable/status","scalable/places","scalable/mimetypes")
  for d in dirs:(base/d).mkdir(parents=True,exist_ok=True)
  logo=LOGO.replace("#000000", "#ffffff" if theme=="G-OS-dark" else "#000000")
  for i,name in enumerate(APPS):
   if name=="org.gnome.GNOME": svg=logo
   else:
    c1=["#36b6a5","#64748b","#313b4f","#58a5ef","#4b91ef","#f5a64b","#66768e","#62a8db","#2db4c9","#e56b6f","#5a9de8","#e56a9c","#48b7e8","#5bb9a5","#54b7a1","#d77eb5","#647c98","#4cb6a2","#a18be9","#e2a45e","#55a9d9","#35455d","#b48de4","#5b9ad7","#5da7df","#4db99a","#d49b52","#e9b54d","#607fba","#65b98e","#4e9be5","#f28b42"][i]
    c2=["#1672b8","#263449","#101827","#6a54d8","#7658dd","#df5c46","#29374b","#3b62b2","#3265b5","#a33c67","#3a4fb2","#8e4bc4","#4776d7","#287f99","#277c9e","#8756c8","#2d435f","#28728c","#6152bb","#ba6849","#405cbd","#18283c","#6a5bbd","#4255a5","#4266ae","#287f75","#9b5d3b","#e26d35","#33446f","#32806e","#3155ae","#d84454"][i]
    glyph="<path d='M120 140h272v232H120zM160 200h192m-192 64h120'/>" if i%4==0 else "<circle cx='256' cy='256' r='116'/><path d='M256 140v116l78 52'/>" if i%4==1 else "<path d='m120 150 100 106-100 106M250 362h142'/>" if i%4==2 else "<path d='M142 120h228v272H142zM256 180v150m-75-75h150'/>"
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs><rect x="20" y="16" width="472" height="472" rx="112" fill="url(#g)"/><g fill="none" stroke="#fff" stroke-width="23" stroke-linecap="round" stroke-linejoin="round">{glyph}</g></svg>'
   (base/"scalable/apps"/(name+".svg")).write_text(svg,encoding="utf-8")
  (base/"scalable/apps/org.gnome.GNOME.svg").write_text(logo,encoding="utf-8")
  (base/"512x512/apps/org.gnome.GNOME.svg").write_text(LOGO,encoding="utf-8")
  for name,path in SYMBOLS.items():
   svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><g fill="none" stroke="{fg}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{path}</g></svg>'
   for cat in ("actions","status"):(base/f"scalable/{cat}/{name}-symbolic.svg").write_text(svg,encoding="utf-8")
  folder='<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48"><path d="M4 9h16l5 5h19v26H4z" fill="#4c99e8" stroke="#fff" stroke-width="1.5"/></svg>'
  for cat in ("places","mimetypes"):(base/f"scalable/{cat}/folder.svg").write_text(folder,encoding="utf-8")
  (base/"index.theme").write_text(f"""[Icon Theme]
Name={theme}
Comment=G-OS macOS-inspired icon theme for GNOME 51
Inherits=Adwaita,hicolor
Directories={','.join(dirs)}

[512x512/apps]
Size=512
Type=Fixed
Context=Applications

[scalable/apps]
Size=48
Type=Scalable
MinSize=16
MaxSize=512
Context=Applications

[scalable/actions]
Size=24
Type=Scalable
MinSize=16
MaxSize=64
Context=Actions

[scalable/status]
Size=24
Type=Scalable
MinSize=16
MaxSize=64
Context=Status

[scalable/places]
Size=48
Type=Scalable
MinSize=16
MaxSize=256
Context=Places

[scalable/mimetypes]
Size=48
Type=Scalable
MinSize=16
MaxSize=256
Context=MimeTypes
""",encoding="utf-8")
 print(f"Generated {len(APPS)} app IDs and {len(SYMBOLS)} symbolic IDs in light/dark variants.")
if __name__=="__main__":main()
