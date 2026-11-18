"""Generate the four end-of-October posts (12 artboards) for the canvas."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from socials import footer  # noqa: E402

OUT = sys.argv[1]
BLUE, VIOLET, TEAL, TEAL_LT, OFF, INK = "#2B04DB", "#856CF7", "#5EC4B3", "#9DFFEE", "#F7F8FA", "#2C2C31"
LOGO_W, LOGO_C = "/_blob/12d91d0c30b41377df3f3aee3cd08bce", "/_blob/fd2b3edf892edc1dd9a5e996d20a755e"
B = {
    "feed_full": "/_blob/a9817b3513259ba85d3c7d7564fc25a1",
    "feed_low": "/_blob/fb4f39f165d0650b2586a91985a1d21f",
    "wallet_full": "/_blob/867d66c4f508c6a843436b899ce39d75",
    "wallet_card": "/_blob/f701b60ae80115c4e09c1324471a6377",
    "earn_body": "/_blob/052972e1321a4eecad0c8d11f3bc084a",
    "explore_full": "/_blob/e9d141cdc21b32eafdf8d9c6a2e07509",
    "explore_tabs": "/_blob/749b30ec2994d5efc7d229f9649e099f",
    "believers": "/_blob/29436bf75a9f15cad299fbb68083cb5c",
    "live": "/_blob/0e2d80734d53512c860fdbe36c397cdd",
}
STAR = "M50 0C55 35 65 45 100 50C65 55 55 65 50 100C45 65 35 55 0 50C35 45 45 35 50 0Z"


def star(x, y, s, c, o=1):
    return (f'<svg aria-hidden="true" width="{s}" height="{s}" viewBox="0 0 100 100" '
            f'style="position: absolute; left: {x}px; top: {y}px; opacity: {o}"><path d="{STAR}" fill="{c}"></path></svg>')


def page(title, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400&amp;family=Playfair+Display:ital,wght@0,600;1,500&amp;display=swap">
<style>
body{{margin:0}}
a{{color:{BLUE}}}a:hover{{color:{VIOLET}}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''


def top(dark, idx):
    logo = LOGO_W if dark else LOGO_C
    col = "rgba(255,255,255,0.85)" if dark else INK
    count = f'<div style="font-size: 28px; font-weight: 600; color: {col}">{idx}</div>' if idx else ""
    return (f'<div style="display: flex; justify-content: space-between; align-items: center; position: relative">'
            f'<img src="{logo}" alt="Worsship" style="height: 72px; width: auto; display: block">{count}</div>')


def swipe(dark, left=""):
    pill = (f'<div style="font-size: 28px; font-weight: 800; color: {INK if dark else "#FFFFFF"}; '
            f'background: {"#FFFFFF" if dark else BLUE}; padding: 14px 28px; border-radius: 999px">Swipe →</div>')
    return (f'<div style="display: flex; justify-content: space-between; align-items: center; position: relative">'
            f'<div style="font-size: 28px; font-weight: 700">{left}</div>{pill}</div>')


def cover(idx, kicker, head_html, sub, img, alt, note=""):
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px 64px; background: {BLUE}; color: #FFFFFF; font-family: 'Nunito', sans-serif; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
<div aria-hidden="true" style="position: absolute; right: -260px; top: 200px; width: 820px; height: 820px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(530, 160, 64, TEAL_LT)}{star(40, 1100, 40, "#FFFFFF", 0.85)}{star(560, 1020, 48, TEAL_LT)}
{top(True, idx)}
<div style="display: flex; align-items: center; gap: 24px; position: relative">
<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 26px">
<div style="font-size: 28px; font-weight: 800; letter-spacing: 3px; color: {TEAL_LT}">{kicker}</div>
<h1 style="margin: 0; font-size: 78px; line-height: 1.04; font-weight: 900; letter-spacing: -1px">{head_html}</h1>
<p style="margin: 0; font-size: 34px; line-height: 1.3; font-weight: 600; color: rgba(255,255,255,0.92)">{sub}</p>
{f'<p style="margin: 0; font-size: 22px; font-weight: 600; color: rgba(255,255,255,0.7)">{note}</p>' if note else ''}
</div>
<div style="flex: 0 0 370px; height: 800px; border: 12px solid #111114; border-radius: 54px; overflow: hidden; background: #111114; transform: rotate(5deg); box-shadow: 0 30px 60px rgba(10,0,60,0.45)">
<img src="{img}" alt="{alt}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block">
</div>
</div>
{swipe(True)}
</div>'''


def step(idx, n, head, sub, img, alt, width=900, last=False, note=""):
    foot = (f'<div style="position: relative">{footer(color=INK, size=24, icon=32, gap=34)}</div>' if last
            else swipe(False))
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px 64px; background: {OFF}; color: {INK}; font-family: 'Nunito', sans-serif; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
{star(910, 190, 60, VIOLET)}{star(995, 300, 32, TEAL)}
{top(False, idx)}
<div style="display: flex; flex-direction: column; gap: 22px; position: relative">
<div style="display: flex; align-items: center; gap: 18px">
<div style="width: 68px; height: 68px; border-radius: 50%; background: {VIOLET}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 38px; font-weight: 900">{n}</div>
</div>
<h2 style="margin: 0; font-size: 70px; line-height: 1.05; font-weight: 900; color: {BLUE}; letter-spacing: -1px">{head}</h2>
<p style="margin: 0; font-size: 34px; line-height: 1.35; font-weight: 600">{sub}</p>
</div>
<div style="display: flex; justify-content: center; position: relative">
<div style="width: {width}px; border-radius: 28px; overflow: hidden; background: #FFFFFF; border: 3px solid #E4E1FB; box-shadow: 0 18px 40px rgba(43,4,219,0.12)">
<img src="{img}" alt="{alt}" style="width: 100%; height: auto; display: block">
</div>
{f'<div style="position: absolute; left: 0; right: 0; bottom: -40px; text-align: center; font-size: 22px; font-weight: 600; color: #6B6B76">{note}</div>' if note else ''}
</div>
{foot}
</div>'''


def cta(idx, kicker, head, sub, button):
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px 64px; background: {BLUE}; color: #FFFFFF; font-family: 'Nunito', sans-serif; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
<div aria-hidden="true" style="position: absolute; left: -240px; bottom: -220px; width: 760px; height: 760px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(880, 170, 80, TEAL_LT)}{star(990, 320, 40, "#FFFFFF", 0.9)}
{top(True, idx)}
<div style="display: flex; flex-direction: column; gap: 36px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 60px; color: {TEAL_LT}">{kicker}</p>
<h2 style="margin: 0; font-size: 90px; line-height: 1.04; font-weight: 900; letter-spacing: -1px">{head}</h2>
<p style="margin: 0; font-size: 36px; line-height: 1.35; font-weight: 600">{sub}</p>
<div style="display: flex"><div style="font-size: 40px; font-weight: 900; color: {INK}; background: {TEAL}; padding: 26px 44px; border-radius: 999px">{button}</div></div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; position: relative">
{footer(size=24, icon=32, gap=34)}
<div style="font-size: 25px; font-weight: 600; color: rgba(255,255,255,0.85)">Get Worsship on Google Play or at app.worsship.com</div>
</div>
</div>'''


def card(icon_text, head, sub):
    return (f'<div style="display: flex; align-items: center; gap: 26px; background: #FFFFFF; border: 3px solid #E4E1FB; border-radius: 28px; padding: 26px 30px">'
            f'<div style="flex: 0 0 84px; height: 84px; border-radius: 24px; background: {VIOLET}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{icon_text}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 4px"><div style="font-size: 38px; font-weight: 900; color: {BLUE}">{head}</div>'
            f'<div style="font-size: 28px; font-weight: 600">{sub}</div></div></div>')


files = {}

# Post A: Meet Worsship (Wed 28 Oct)
files["oa-1"] = page("Meet Worsship 1", cover(
    "1 / 3", "MEET WORSSHIP",
    f'A home for <span style="color: {TEAL_LT}">faith-filled</span> creators',
    "Short videos on every part of life, through a Christian lens.",
    B["feed_full"], "The Worsship home feed with a worship video, Word for Today and Amen button"))
features = "".join([
    card("1", "Watch", "Short videos on faith, money, career, health and more"),
    card("2", "Say Amen", "React, comment and share what moves you"),
    card("3", "Support", "Send creators support right from the video"),
    card("4", "Create", "Share your own videos with scripture and music"),
])
files["oa-2"] = page("Meet Worsship 2", f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px 64px; background: {OFF}; color: {INK}; font-family: 'Nunito', sans-serif; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
{star(910, 190, 60, VIOLET)}{star(995, 300, 32, TEAL)}
{top(False, "2 / 3")}
<h2 style="margin: 0; font-size: 76px; line-height: 1.05; font-weight: 900; color: {BLUE}; letter-spacing: -1px; position: relative">What you can do on Worsship</h2>
<div style="display: flex; flex-direction: column; gap: 22px; position: relative">{features}</div>
{swipe(False)}
</div>''')
files["oa-3"] = page("Meet Worsship 3", cta(
    "3 / 3", "Built for the audience of One.", "Faith belongs in the conversation.",
    "Join creators and believers exploring every part of life through a Christian lens.", "Join Worsship today"))

# Post B: Support a creator (Thu 29 Oct)
files["ob-1"] = page("Support a creator 1", cover(
    "1 / 4", "HOW IT WORKS",
    f'Support the creators who <span style="color: {TEAL_LT}">bless you</span>',
    "Three taps from a video you love to a creator you want to encourage.",
    B["wallet_full"], "The Worsship wallet screen showing an available seed balance and a Top Up button", note="Sample figures shown."))
files["ob-2"] = page("Support a creator 2", step(
    "2 / 4", "1", "Top up your wallet",
    "Your wallet holds your seed balance. Top-ups are paid securely through Paystack.",
    B["wallet_card"], "Wallet card with Available Seed Balance and a Top Up button", width=780, note="Sample figures shown."))
files["ob-3"] = page("Support a creator 3", step(
    "3 / 4", "2", "Tap the gift on a video you love",
    "The gift icon sits beside every video where the creator has turned on support.",
    B["feed_low"], "A worship video in the Worsship feed with Like, Amen, comment, gift and share buttons", width=520))
files["ob-4"] = page("Support a creator 4", step(
    "4 / 4", "3", "Creators: withdraw to your bank",
    "Add your withdrawal account in Earnings. The minimum withdrawal is ₦1,000, and small withdrawals are processed automatically.",
    B["earn_body"], "Earnings screen with available balance, total earned, withdrawal account and amount field", width=520, last=True, note="Sample figures shown."))

# Post C: Explore (Fri 30 Oct)
files["oc-1"] = page("Explore 1", cover(
    "1 / 4", "EXPLORE",
    f'Find your <span style="color: {TEAL_LT}">people</span> on Worsship',
    "Search creators and topics, or browse by what matters to you.",
    B["explore_full"], "The Worsship Explore screen with topic chips and Featured videos"))
files["oc-2"] = page("Explore 2", step(
    "2 / 4", "1", "Browse by topic",
    "Youth, Career, Marriage, Finance, Health, Bible Study, Music, Devotionals and more. Then switch between Featured, New, Believers, Growth and Live.",
    B["explore_tabs"], "Explore search bar, topic chips and tabs for Featured, New, Believers and Growth", width=900))
files["oc-3"] = page("Explore 3", step(
    "3 / 4", "2", "Meet new voices",
    "Believers suggests creators to follow, plus worship leaders sharing praise and worship.",
    B["believers"], "Believers tab with Suggested Voices and Worshipers lists", width=500))
files["oc-4"] = page("Explore 4", step(
    "4 / 4", "3", "Catch live moments",
    "Watch replays of live sessions, or schedule your own event.",
    B["live"], "Live tab with a Schedule Event button and a replay ready to watch", width=500, last=True))

# Post D: Rep your church tomorrow (Sat 31 Oct)
step_row = lambda n, t: (f'<div style="display: flex; align-items: center; gap: 22px"><div style="flex: 0 0 60px; height: 60px; border-radius: 50%; background: {VIOLET}; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900">{n}</div>'
                         f'<div style="font-size: 36px; font-weight: 700">{t}</div></div>')
files["od-1"] = page("Rep your church tomorrow", f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px 64px; background: {BLUE}; color: #FFFFFF; font-family: 'Nunito', sans-serif; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
<div aria-hidden="true" style="position: absolute; right: -240px; top: -200px; width: 720px; height: 720px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(860, 70, 76, TEAL_LT)}{star(970, 190, 40, "#FFFFFF")}
{top(True, "")}
<div style="display: flex; flex-direction: column; gap: 26px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 60px; color: {TEAL_LT}">Sunday's coming.</p>
<h1 style="margin: 0; font-size: 120px; line-height: 0.98; font-weight: 900; letter-spacing: -2px">Rep your church tomorrow.</h1>
<p style="margin: 0; font-size: 38px; line-height: 1.35; font-weight: 600">Snap a photo at service, turn it into your Sunday Worship Frame, and tag <span style="color: {TEAL_LT}; font-weight: 800">@worsship_official</span>.</p>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.25); border-radius: 28px; padding: 32px 36px; position: relative">
{step_row(1, "Profile, then Your Achievements")}
{step_row(2, "Find your church, pick a frame style")}
{step_row(3, "Add your Sunday photo, then Share")}
<div style="font-size: 26px; font-weight: 600; color: rgba(255,255,255,0.8)">Your photo stays on your phone. #SundayWorship</div>
</div>
<div style="display: flex; justify-content: center; position: relative">{footer(size=24, icon=32, gap=34)}</div>
</div>''')

for k, html in files.items():
    with open(os.path.join(OUT, f"{k}.dc.html"), "w") as fh:
        fh.write(html)
print(list(files))
