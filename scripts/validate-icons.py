#!/usr/bin/env python3
from pathlib import Path
import configparser,sys,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]/"icons"; errors=[]
for theme in ("G-OS","G-OS-dark"):
 base=root/theme; manifest=base/"index.theme"
 if not manifest.is_file():errors.append(theme+": missing index.theme");continue
 cfg=configparser.ConfigParser(interpolation=None);cfg.read(manifest,encoding="utf-8")
 for d in cfg.get("Icon Theme","Directories",fallback="").split(","):
  if d and not (base/d.strip()).is_dir():errors.append(theme+": missing "+d)
 svgs=list(base.rglob("*.svg"))
 if not svgs:errors.append(theme+": no SVG files")
 for svg in svgs:
  try:ET.parse(svg)
  except ET.ParseError as e:errors.append(str(svg)+": "+str(e))
 if not (base/"512x512/apps/org.gnome.GNOME.svg").is_file():errors.append(theme+": missing 512px GNOME logo")
 if not list((base/"scalable/actions").glob("*-symbolic.svg")):errors.append(theme+": missing symbolic files")
if errors:print("\\n".join(errors));sys.exit(1)
print("G-OS light/dark icon themes: manifests and SVG assets valid.")
