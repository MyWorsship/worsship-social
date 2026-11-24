"""Generate the 19-29 Nov posts."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import (BLUE, VIOLET, TEAL, TEAL_LT, OFF, INK, star, page, top, swipe, cover, step, cta, card)  # noqa: E402
from socials import footer  # noqa: E402

L = lambda n: f"/_local/{n}.png"  # noqa: E731
BASE = ("width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px 64px; "
        "font-family: 'Nunito', sans-serif; display: flex; flex-direction: column; justify-content: space-between; "
        "position: relative; overflow: hidden")


def textcover(idx, kicker, head, sub):
    return f'''<div style="{BASE}; background: {BLUE}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; right: -260px; bottom: -200px; width: 820px; height: 820px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(860, 200, 84, TEAL_LT)}{star(970, 340, 40, "#FFFFFF", 0.9)}{star(80, 1080, 44, TEAL_LT)}
{top(True, idx)}
<div style="display: flex; flex-direction: column; gap: 30px; position: relative">
<div style="font-size: 30px; font-weight: 800; letter-spacing: 3px; color: {TEAL_LT}">{kicker}</div>
<h1 style="margin: 0; font-size: 112px; line-height: 1.0; font-weight: 900; letter-spacing: -2px">{head}</h1>
<p style="margin: 0; font-size: 40px; line-height: 1.32; font-weight: 600; color: rgba(255,255,255,0.92)">{sub}</p>
</div>
{swipe(True)}
</div>'''


def listslide(idx, head, cards, last=False):
    foot = (f'<div style="position: relative; display: flex; justify-content: center">{footer(color=INK, size=24, icon=32, gap=34)}</div>'
            if last else swipe(False))
    return f'''<div style="{BASE}; background: {OFF}; color: {INK}">
{star(910, 190, 60, VIOLET)}{star(995, 300, 32, TEAL)}
{top(False, idx)}
<h2 style="margin: 0; font-size: 72px; line-height: 1.05; font-weight: 900; color: {BLUE}; letter-spacing: -1px; position: relative; max-width: 820px">{head}</h2>
<div style="display: flex; flex-direction: column; gap: 20px; position: relative">{"".join(cards)}</div>
{foot}
</div>'''


def single(kicker, head, body_html, dark=True):
    bg, fg = (BLUE, "#FFFFFF") if dark else (OFF, INK)
    hc = "#FFFFFF" if dark else BLUE
    kc = TEAL_LT if dark else VIOLET
    return f'''<div style="{BASE}; background: {bg}; color: {fg}">
<div aria-hidden="true" style="position: absolute; right: -240px; top: -200px; width: 720px; height: 720px; border-radius: 50%; background: {VIOLET}; opacity: {0.55 if dark else 0.18}"></div>
{star(860, 70, 76, kc)}{star(970, 190, 40, "#FFFFFF" if dark else TEAL)}
{top(dark, "")}
<div style="display: flex; flex-direction: column; gap: 30px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 60px; color: {kc}">{kicker}</p>
<h1 style="margin: 0; font-size: 110px; line-height: 1.0; font-weight: 900; letter-spacing: -2px; color: {hc}">{head}</h1>
{body_html}
</div>
<div style="display: flex; justify-content: center; position: relative">{footer(color="#FFFFFF" if dark else INK, size=24, icon=32, gap=34)}</div>
</div>'''


def p(text, dark=True):
    return f'<p style="margin: 0; font-size: 40px; line-height: 1.35; font-weight: 600">{text}</p>'


def option(letter, text, dark=False):
    return (f'<div style="display: flex; align-items: center; gap: 24px; background: #FFFFFF; border: 3px solid #E4E1FB; border-radius: 26px; padding: 22px 28px">'
            f'<div style="flex: 0 0 64px; height: 64px; border-radius: 50%; background: {VIOLET}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 34px; font-weight: 900">{letter}</div>'
            f'<div style="font-size: 38px; font-weight: 800; color: {INK}">{text}</div></div>')


step_row = lambda n, t: (f'<div style="display: flex; align-items: center; gap: 22px"><div style="flex: 0 0 60px; height: 60px; border-radius: 50%; background: {VIOLET}; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900">{n}</div>'  # noqa: E731
                         f'<div style="font-size: 36px; font-weight: 700">{t}</div></div>')
TAG = f'<span style="color: {TEAL_LT}; font-weight: 800">@worsship_official</span>'
