#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
DEST="${HOME}/.themes/G-OS"
if [[ "${1:-}" == "--uninstall" ]]; then
  rm -rf -- "$DEST"
  printf 'G-OS removed from %s\n' "$DEST"
  exit 0
fi
mkdir -p -- "$DEST"
cp -a "$ROOT/gnome-shell" "$ROOT/gtk-3.0" "$ROOT/gtk-4.0" "$ROOT/index.theme" "$DEST/"
printf 'G-OS installed in %s\n' "$DEST"
printf 'Enable User Themes to apply the GNOME Shell stylesheet.\n'
