"""Generate the 19-29 Nov posts."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import (BLUE, VIOLET, TEAL, TEAL_LT, OFF, INK, star, page, top, swipe, cover, step, cta, card)  # noqa: E402
from socials import footer  # noqa: E402

OUT = sys.argv[1]
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
files = {}

# 1. Thu 19 Nov: Daily Faith Challenge
files["n1-1"] = page("Daily Faith Challenge 1", cover(
    "1 / 4", "DAILY FAITH CHALLENGE",
    f'One question a day. <span style="color: {TEAL_LT}">Grow</span> every day.',
    "Keep scrolling. Every third video in your feed is a Bible question waiting for you.",
    L("ch-full"), "A Daily Faith Challenge question about Proverbs 21:20 with four answer options"))
files["n1-2"] = page("Daily Faith Challenge 2", step(
    "2 / 4", "1", "Spot it in your feed",
    "The challenge appears every third video. You can also open it from your notifications.",
    L("ch-q"), "Challenge question with options A to D", width=640))
files["n1-3"] = page("Daily Faith Challenge 3", step(
    "3 / 4", "2", "Answer and start your streak",
    "Pick an answer, read why it is right, then come back tomorrow for Day 2.",
    L("ch-streak"), "A correct answer with a 1 Day Streak badge", width=470))
files["n1-4"] = page("Daily Faith Challenge 4", cta(
    "4 / 4", "Got a question that would stretch us?", "Write tomorrow's challenge.",
    "Email your question to support@worsship.com and tell us how you'd like to be credited.", "Play today's challenge"))

# 2. Fri 20 Nov: conversation
files["n2"] = page("Finish this sentence", single(
    "Finish this sentence.", "I wish more Christians made videos about…",
    p("Money? Mental wellbeing? Marriage? Career? Tell us in the comments. You might inspire someone's first video.")))

# 3. Sat 21 Nov: Sunday Worship Frame tutorial
files["n3-1"] = page("Sunday Worship Frame 1", cover(
    "1 / 5", "SUNDAY WORSHIP FRAME",
    f'Rep your <span style="color: {TEAL_LT}">church</span> tomorrow',
    "Turn your Sunday photo into a frame with your church's name on it.",
    L("sw-result"), "A finished Sunday Worship Frame reading This was how I worship, with filter options and Save and Share buttons"))
files["n3-2"] = page("Sunday Worship Frame 2", step(
    "2 / 5", "1", "Find your church",
    "Go to Profile, then Your Achievements, and search for your church. Not listed? Add it.",
    L("sw-search"), "Sunday Worship Frame church search with a list of churches", width=760))
files["n3-3"] = page("Sunday Worship Frame 3", step(
    "3 / 5", "2", "Pick a frame style",
    "Royal Purple, Golden Sunday or Pure Light. Then choose your Sunday photo.",
    L("sw-style"), "Frame style options and a Choose your Sunday photo button", width=620))
files["n3-4"] = page("Sunday Worship Frame 4", step(
    "4 / 5", "3", "Add a filter, then save or share",
    "Your photo is processed on your phone and never uploaded to our servers.",
    L("sw-result"), "Finished frame with filters, frame colours, Save and Share", width=380))
files["n3-5"] = page("Sunday Worship Frame 5", cta(
    "5 / 5", "See you at church.", "Tag @worsship_official",
    "Post your frame tomorrow and tag us. We'd love to see where you worship.", "Make your frame"))

# 4. Sun 22 Nov
files["n4"] = page("How was church today", single(
    "Happy Sunday.", "How was church today?",
    p(f"Share one line from today's message in the comments. Then make your Sunday Worship Frame and tag {TAG}.")))

# 5. Mon 23 Nov: Your expertise is ministry
files["n5-1"] = page("Expertise is ministry 1", textcover(
    "1 / 4", "CREATORS WANTED", "Your expertise is ministry.",
    "You don't need a pulpit to create from a Christian lens."))
files["n5-2"] = page("Expertise is ministry 2", listslide("2 / 4", "Who belongs on Worsship", [
    card("₦", "Finance", "Budgeting, saving and giving wisely"),
    card("♥", "Health", "Fitness, nutrition and wellbeing"),
    card("↗", "Career", "Work, business and leadership"),
    card("∞", "Family", "Marriage, parenting and relationships"),
    card("♪", "Creatives", "Music, poetry, comedy and art"),
]))
files["n5-3"] = page("Expertise is ministry 3", listslide("3 / 4", "How to start", [
    card("1", "Get Worsship", "Google Play or app.worsship.com"),
    card("2", "Set up your profile", "Tell people what you create about"),
    card("3", "Post your first video", "Add a scripture reference to anchor it"),
    card("4", "Turn on support", "Let viewers send you gifts"),
]))
files["n5-4"] = page("Expertise is ministry 4", cta(
    "4 / 4", "Built for the audience of One.", "Start creating today.",
    "Faith, money, health, career and family. Every part of life, through a Christian lens.", "Join Worsship"))

# 6. Wed 25 Nov: creator tips
files["n6-1"] = page("Creator tips 1", textcover(
    "1 / 3", "CREATOR TIPS", "5 tips for your first month.",
    "Small habits that help new creators get found on Worsship."))
files["n6-2"] = page("Creator tips 2", listslide("2 / 3", "Save this for later", [
    card("1", "Post consistently", "Aim for a rhythm you can keep"),
    card("2", "Add a scripture reference", "Anchor your message in the Word"),
    card("3", "Tag who it's for", "A church, pastor or creator (up to 5)"),
    card("4", "Add background music", "Pick a track from the Music Library"),
    card("5", "Share your invite link", "Your referral code is your username"),
]))
files["n6-3"] = page("Creator tips 3", cta(
    "3 / 3", "Which tip will you try first?", "Your next video is someone's encouragement.",
    "Open Worsship, tap Upload and share what God has put on your heart.", "Post a video"))

# 7. Thu 26 Nov: gratitude
files["n7"] = page("What are you thankful for", single(
    "This week,", "What are you thankful for?",
    f'''<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-size: 40px; line-height: 1.4; color: rgba(255,255,255,0.95)">"Give thanks in all circumstances; for this is God's will for you in Christ Jesus."</p>
<p style="margin: 0; font-size: 30px; font-weight: 800; color: {TEAL_LT}">1 Thessalonians 5:18 (NIV)</p>
{p("Drop one thing in the comments.")}'''))

# 8. Fri 27 Nov: what do you watch first
files["n8"] = page("What do you watch first", f'''<div style="{BASE}; background: {OFF}; color: {INK}">
{star(910, 170, 60, VIOLET)}{star(995, 280, 32, TEAL)}
{top(False, "")}
<div style="display: flex; flex-direction: column; gap: 20px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 56px; color: {VIOLET}">Be honest.</p>
<h1 style="margin: 0; font-size: 96px; line-height: 1.0; font-weight: 900; letter-spacing: -2px; color: {BLUE}">What do you watch first?</h1>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; position: relative">
{option("A", "Sermon clips")}{option("B", "Worship sessions")}{option("C", "Testimonies")}{option("D", "Faith and money, health or career")}
</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 16px; position: relative">
<div style="font-size: 32px; font-weight: 800">Comment A, B, C or D</div>
{footer(color=INK, size=24, icon=32, gap=34)}
</div>
</div>''')

# 9. Sat 28 Nov: rep your church tomorrow
files["n9"] = page("Wear it Snap it Frame it", f'''<div style="{BASE}; background: {BLUE}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; right: -240px; top: -200px; width: 720px; height: 720px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(860, 70, 76, TEAL_LT)}{star(970, 190, 40, "#FFFFFF")}
{top(True, "")}
<div style="display: flex; flex-direction: column; gap: 26px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 60px; color: {TEAL_LT}">Sunday's almost here.</p>
<h1 style="margin: 0; font-size: 116px; line-height: 0.98; font-weight: 900; letter-spacing: -2px">Snap it. Frame it. Rep it.</h1>
<p style="margin: 0; font-size: 38px; line-height: 1.35; font-weight: 600">Take a photo at service tomorrow, turn it into your Sunday Worship Frame and tag {TAG}.</p>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.25); border-radius: 28px; padding: 32px 36px; position: relative">
{step_row(1, "Profile, then Your Achievements")}
{step_row(2, "Find your church, pick a frame style")}
{step_row(3, "Add your Sunday photo, then Share")}
<div style="font-size: 26px; font-weight: 600; color: rgba(255,255,255,0.8)">Your photo stays on your phone. #SundayWorship</div>
</div>
<div style="display: flex; justify-content: center; position: relative">{footer(size=24, icon=32, gap=34)}</div>
</div>''')

# 10. Sun 29 Nov: audience of One
files["n10-1"] = page("Audience of One 1", textcover(
    "1 / 3", "WHAT WE MEAN", "Built for the audience of One.",
    "Three things that shape everything we build at Worsship."))
files["n10-2"] = page("Audience of One 2", listslide("2 / 3", "Why it matters", [
    card("1", "Create for God first", "Not for the algorithm or the applause"),
    card("2", "A safer, more intentional space", "Somewhere faith is welcome, not mocked"),
    card("3", "Every part of life", "Faith, money, health and career, through a Christian lens"),
]))
files["n10-3"] = page("Audience of One 3", cta(
    "3 / 3", "You got to the last slide.", "Now rep your church.",
    "Make your Sunday Worship Frame from today's service and tag @worsship_official.", "Make your frame"))

for k, html in files.items():
    with open(os.path.join(OUT, f"{k}.dc.html"), "w") as fh:
        fh.write(html)
print(" ".join(f"{k}.dc.html" for k in files))
