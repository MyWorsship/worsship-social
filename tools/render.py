"""Render canvas artboards (.dc.html) to PNG with local fonts and images."""
import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

SRC, OUT, S = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
names = sys.argv[4:]
BLOBS = {
    "12d91d0c30b41377df3f3aee3cd08bce": S / "logo/worsship-mark-white.png",
    "fd2b3edf892edc1dd9a5e996d20a755e": S / "logo/worsship-mark-colour.png",
    "9666112666d141c888ad286ee568a034": S / "crops/up-nav.png",
    "d3747de5a6e11a18ec7701fb86bb431c": S / "crops/up-type.png",
    "9b55f27742a035bcfea586f1c7169eb0": S / "crops/up-caption.png",
    "43f44b24327ed912124cbae77cc58c64": S / "crops/up-music.png",
    "bb0a9eb112d19724e2da198fab98d784": S / "crops/up-full.png",
    "a4ec6a2c9fde515bef0ab6d8c8d20160": S / "crops/challenge.png",
    "a9817b3513259ba85d3c7d7564fc25a1": S / "crops/o-feed-full.png",
    "66e80dbe2df7cd7b06bc4b8b3b39f35b": S / "crops/o-feed-low.png",
    "720b104df529543957029f02154850f5": S / "crops/o-wallet-full.png",
    "a525ee65802071ee06978761f7e6993e": S / "crops/o-wallet-card.png",
    "7b4826b058eba43526ae66ea2a6698d2": S / "crops/o-earn-body.png",
    "e9d141cdc21b32eafdf8d9c6a2e07509": S / "crops/o-explore-full.png",
    "749b30ec2994d5efc7d229f9649e099f": S / "crops/o-explore-tabs.png",
    "29436bf75a9f15cad299fbb68083cb5c": S / "crops/o-believers-body.png",
    "0e2d80734d53512c860fdbe36c397cdd": S / "crops/o-live-body.png",
    "867d66c4f508c6a843436b899ce39d75": S / "crops/o-wallet-full2.png",
    "f701b60ae80115c4e09c1324471a6377": S / "crops/o-wallet-card2.png",
    "fb4f39f165d0650b2586a91985a1d21f": S / "crops/o-feed-low2.png",
    "052972e1321a4eecad0c8d11f3bc084a": S / "crops/o-earn-body2.png",
}
F = S / "fonts"
FONTS = f"""
@font-face {{ font-family: 'Nunito'; src: url('file://{F}/Nunito[wght].ttf'); font-weight: 200 1000; font-style: normal; }}
@font-face {{ font-family: 'Nunito'; src: url('file://{F}/Nunito-Italic[wght].ttf'); font-weight: 200 1000; font-style: italic; }}
@font-face {{ font-family: 'Playfair Display'; src: url('file://{F}/PlayfairDisplay[wght].ttf'); font-weight: 400 900; font-style: normal; }}
@font-face {{ font-family: 'Playfair Display'; src: url('file://{F}/PlayfairDisplay-Italic[wght].ttf'); font-weight: 400 900; font-style: italic; }}
body {{ margin: 0; }}
"""

OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch()
    for name in names:
        src = (SRC / name).read_text()
        body = re.search(r"<x-dc>(.*)</x-dc>", src, re.S).group(1)
        body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
        body = re.sub(r"/_blob/([0-9a-f]{32})", lambda m: "file://" + str(BLOBS[m.group(1)]), body)
        body = re.sub(r"/_local/([\w.-]+)", lambda m: "file://" + str(S / "crops" / m.group(1)), body)
        w, h = map(int, re.search(r'"\$preview":\{"width":(\d+),"height":(\d+)\}', src).groups())
        html = f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}</style></head><body>{body}</body></html>"
        tmp = OUT / (name + ".tmp.html")
        tmp.write_text(html)
        page = browser.new_page(viewport={"width": w, "height": h})
        page.goto("file://" + str(tmp))
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        page.screenshot(path=str(OUT / name.replace(".dc.html", ".png")), clip={"x": 0, "y": 0, "width": w, "height": h})
        page.close()
        tmp.unlink()
    browser.close()
print("rendered", len(names))
