"""Social footer: platform icon + handle, as inline HTML for artboards."""
import re
from pathlib import Path

ICONS = Path(__file__).parent / "icons"
ACCOUNTS = [
    ("tiktok", "worsship_official"),
    ("instagram", "worsship_official"),
    ("linkedin", "Worsship"),
    ("facebook", "Worsship"),
]


def path_d(name):
    svg = (ICONS / f"{name}.svg").read_text()
    return re.search(r'<path d="([^"]+)"', svg).group(1)


def footer(color="#FFFFFF", size=24, icon=34, gap=36, wrap=False):
    items = []
    for name, handle in ACCOUNTS:
        items.append(
            f'<div style="display: flex; align-items: center; gap: 10px">'
            f'<svg aria-hidden="true" width="{icon}" height="{icon}" viewBox="0 0 24 24"><path d="{path_d(name)}" fill="{color}"></path></svg>'
            f'<span style="font-size: {size}px; font-weight: 800; color: {color}">{handle}</span></div>'
        )
    if wrap:
        return (f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: {gap}px 40px; justify-items: start">'
                + "".join(items) + "</div>")
    return (f'<div style="display: flex; justify-content: center; align-items: center; gap: {gap}px; flex-wrap: nowrap">'
            + "".join(items) + "</div>")


if __name__ == "__main__":
    print(footer())
