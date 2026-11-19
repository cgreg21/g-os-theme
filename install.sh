#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "$BASH_SOURCE")" && pwd)"
THEME_DEST="$HOME/.themes/G-OS"
ICON_DEST="$HOME/.local/share/icons"
if [[ $# -gt 0 && $1 == --uninstall ]]; then
  rm -rf -- "$THEME_DEST" "$ICON_DEST/G-OS" "$ICON_DEST/G-OS-dark"
  printf 'G-OS theme and icon themes removed.\n'
  exit 0
fi
python3 "$ROOT/scripts/generate-icons.py"
mkdir -p -- "$THEME_DEST" "$ICON_DEST"
cp -a "$ROOT/gnome-shell" "$ROOT/gtk-3.0" "$ROOT/gtk-4.0" "$ROOT/index.theme" "$THEME_DEST/"
cp -a "$ROOT/icons/G-OS" "$ROOT/icons/G-OS-dark" "$ICON_DEST/"
printf 'G-OS installed in %s\n' "$THEME_DEST"
printf 'Icon themes installed in %s\n' "$ICON_DEST"
printf 'Choose G-OS or G-OS-dark with GNOME Tweaks or gsettings.\n'
printf 'Example: gsettings set org.gnome.desktop.interface icon-theme G-OS\n'
printf 'Enable User Themes to apply the GNOME Shell stylesheet.\n'
