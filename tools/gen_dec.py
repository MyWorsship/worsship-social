"""Generate the 30 Nov - 31 Dec 2026 posts (December monthly run).

Usage: python3 -I gen_dec.py <abs src dir>
Then render with render.py. Prefix: d<NN> = post number in the December plan.
"""
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
TAG = f'<span style="color: {TEAL_LT}; font-weight: 800">@worsship_official</span>'


def textcover(idx, kicker, head, sub, size=112):
    return f'''<div style="{BASE}; background: {BLUE}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; right: -260px; bottom: -200px; width: 820px; height: 820px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(860, 200, 84, TEAL_LT)}{star(970, 340, 40, "#FFFFFF", 0.9)}{star(80, 1080, 44, TEAL_LT)}
{top(True, idx)}
<div style="display: flex; flex-direction: column; gap: 30px; position: relative">
<div style="font-size: 30px; font-weight: 800; letter-spacing: 3px; color: {TEAL_LT}">{kicker}</div>
<h1 style="margin: 0; font-size: {size}px; line-height: 1.0; font-weight: 900; letter-spacing: -2px">{head}</h1>
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


def p(text, size=40):
    return f'<p style="margin: 0; font-size: {size}px; line-height: 1.35; font-weight: 600">{text}</p>'


def single(kicker, head, body_html, dark=True, size=110):
    bg, fg = (BLUE, "#FFFFFF") if dark else (OFF, INK)
    hc = "#FFFFFF" if dark else BLUE
    kc = TEAL_LT if dark else VIOLET
    return f'''<div style="{BASE}; background: {bg}; color: {fg}">
<div aria-hidden="true" style="position: absolute; right: -240px; top: -200px; width: 720px; height: 720px; border-radius: 50%; background: {VIOLET}; opacity: {0.55 if dark else 0.18}"></div>
{star(860, 70, 76, kc)}{star(970, 190, 40, "#FFFFFF" if dark else TEAL)}
{top(dark, "")}
<div style="display: flex; flex-direction: column; gap: 30px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 60px; color: {kc}">{kicker}</p>
<h1 style="margin: 0; font-size: {size}px; line-height: 1.0; font-weight: 900; letter-spacing: -2px; color: {hc}">{head}</h1>
{body_html}
</div>
<div style="display: flex; justify-content: center; position: relative">{footer(color="#FFFFFF" if dark else INK, size=24, icon=32, gap=34)}</div>
</div>'''


def scripture(idx, kicker, quote, ref, sub):
    """Dark scripture cover for Sunday carousels."""
    return f'''<div style="{BASE}; background: {BLUE}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; left: -260px; top: -240px; width: 820px; height: 820px; border-radius: 50%; background: {VIOLET}; opacity: 0.5"></div>
{star(880, 190, 80, TEAL_LT)}{star(990, 330, 38, "#FFFFFF", 0.9)}{star(90, 1090, 40, TEAL_LT)}
{top(True, idx)}
<div style="display: flex; flex-direction: column; gap: 34px; position: relative">
<div style="font-size: 30px; font-weight: 800; letter-spacing: 3px; color: {TEAL_LT}">{kicker}</div>
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 66px; line-height: 1.22">&ldquo;{quote}&rdquo;</p>
<div style="font-size: 32px; font-weight: 800; color: {TEAL_LT}">{ref}</div>
<p style="margin: 0; font-size: 36px; line-height: 1.35; font-weight: 600; color: rgba(255,255,255,0.9)">{sub}</p>
</div>
{swipe(True)}
</div>'''


def option(letter, text):
    return (f'<div style="display: flex; align-items: center; gap: 24px; background: #FFFFFF; border: 3px solid #E4E1FB; border-radius: 26px; padding: 22px 28px">'
            f'<div style="flex: 0 0 64px; height: 64px; border-radius: 50%; background: {VIOLET}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 34px; font-weight: 900">{letter}</div>'
            f'<div style="font-size: 38px; font-weight: 800; color: {INK}">{text}</div></div>')


def step_row(n, t):
    return (f'<div style="display: flex; align-items: center; gap: 22px"><div style="flex: 0 0 60px; height: 60px; border-radius: 50%; background: {VIOLET}; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900">{n}</div>'
            f'<div style="font-size: 36px; font-weight: 700">{t}</div></div>')


def repsat(kicker, head, sub):
    """Saturday 'rep your church tomorrow' single image."""
    return f'''<div style="{BASE}; background: {BLUE}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; right: -240px; top: -200px; width: 720px; height: 720px; border-radius: 50%; background: {VIOLET}; opacity: 0.55"></div>
{star(860, 70, 76, TEAL_LT)}{star(970, 190, 40, "#FFFFFF")}
{top(True, "")}
<div style="display: flex; flex-direction: column; gap: 26px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 60px; color: {TEAL_LT}">{kicker}</p>
<h1 style="margin: 0; font-size: 108px; line-height: 0.98; font-weight: 900; letter-spacing: -2px">{head}</h1>
<p style="margin: 0; font-size: 38px; line-height: 1.35; font-weight: 600">{sub}</p>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.25); border-radius: 28px; padding: 32px 36px; position: relative">
{step_row(1, "Profile, then Your Achievements")}
{step_row(2, "Find your church, pick a frame style")}
{step_row(3, "Add your Sunday photo, then Share")}
<div style="font-size: 26px; font-weight: 600; color: rgba(255,255,255,0.8)">Your photo stays on your phone. Tag @worsship_official</div>
</div>
<div style="display: flex; justify-content: center; position: relative">{footer(size=24, icon=32, gap=34)}</div>
</div>'''


def quiz(kicker, head, opts, ask):
    return f'''<div style="{BASE}; background: {OFF}; color: {INK}">
{star(910, 170, 60, VIOLET)}{star(995, 280, 32, TEAL)}
{top(False, "")}
<div style="display: flex; flex-direction: column; gap: 20px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 56px; color: {VIOLET}">{kicker}</p>
<h1 style="margin: 0; font-size: 80px; line-height: 1.02; font-weight: 900; letter-spacing: -2px; color: {BLUE}">{head}</h1>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; position: relative">
{"".join(option(chr(65 + i), o) for i, o in enumerate(opts))}
</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 16px; position: relative">
<div style="font-size: 32px; font-weight: 800; text-align: center">{ask}</div>
{footer(color=INK, size=24, icon=32, gap=34)}
</div>
</div>'''


REP_LAST = ("You got to the last slide.", "Now rep your church.",
            "Make your Sunday Worship Frame from today's service and tag @worsship_official.", "Make your frame")
f = {}

# d01 Mon 30 Nov: Advent creator ideas (vision/creator)
f["d01-1"] = page("Advent ideas 1", textcover("1 / 4", "ADVENT HAS BEGUN", "Four weeks. Four videos.",
                                              "A simple Advent plan for creators who want to share their faith this season."))
f["d01-2"] = page("Advent ideas 2", listslide("2 / 4", "Many churches mark Advent with four themes", [
    card("1", "Hope", "What are you trusting God for this season?"),
    card("2", "Peace", "A tip for a calmer, less rushed December"),
    card("3", "Joy", "Share a testimony or a song that lifts you"),
    card("4", "Love", "Show a simple act of kindness or generosity"),
]))
f["d01-3"] = page("Advent ideas 3", listslide("3 / 4", "Make it your own", [
    card("₦", "Finance creators", "Planning Christmas spending with wisdom"),
    card("♥", "Health creators", "Rest and wellbeing in a busy season"),
    card("∞", "Family creators", "Advent traditions at home"),
    card("♪", "Music creators", "A carol or worship song, your way"),
]))
f["d01-4"] = page("Advent ideas 4", cta("4 / 4", "Built for the audience of One.", "Post your first Advent video.",
                                        "Open Worsship, tap Upload, add a scripture reference and share it this week.", "Join Worsship"))

# d02 Wed 2 Dec: Explore tutorial
f["d02-1"] = page("Explore tutorial 1", cover("1 / 4", "HOW TO USE EXPLORE",
                                              f'Find content for <span style="color: {TEAL_LT}">every part</span> of life',
                                              "Marriage, money, career, Bible study and more, from people who share your faith.",
                                              L("o-explore-full"), "The Worsship Explore page with search, topic chips and featured videos"))
f["d02-2"] = page("Explore tutorial 2", step("2 / 4", "1", "Search, or tap a topic",
                                             "Search for an @username or #topic, or tap Youth, Career, Marriage, Finance, Health, Bible Study, Music or Devotionals.",
                                             L("o-explore-tabs"), "Explore search bar and topic chips", width=900))
f["d02-3"] = page("Explore tutorial 3", step("3 / 4", "2", "Meet new voices in Believers",
                                             "Open the Believers tab to see Suggested Voices, then follow the creators you connect with.",
                                             L("o-believers-top"), "Suggested Voices with Follow buttons", width=900))
f["d02-4"] = page("Explore tutorial 4", cta("4 / 4", "Which topic would you tap first?", "Your people are on Worsship.",
                                            "And if the topic you need is missing, maybe it's the one you should create.", "Open Explore"))

# d03 Fri 4 Dec: conversation
f["d03"] = page("Christmas song", single("Be honest.", "Which Christmas song could you play all year?",
                                         p("Carol, worship song or a family favourite. Tell us in the comments."), size=96))

# d04 Sat 5 Dec: rep your church tomorrow
f["d04"] = page("Rep your church Advent", repsat("Second Sunday of Advent.", "Rep your church tomorrow.",
                                                 "Snap a photo at service and turn it into your Sunday Worship Frame."))

# d05 Sun 6 Dec: Peace
f["d05-1"] = page("Peace 1", scripture("1 / 3", "ADVENT: PEACE",
                                       "And he will be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace.",
                                       "Isaiah 9:6 (NIV)", "December can be loud. Make room for His peace this week."))
f["d05-2"] = page("Peace 2", listslide("2 / 3", "Three ways to make room for peace", [
    card("1", "Start with stillness", "Five quiet minutes before you check your phone"),
    card("2", "Say no to one thing", "Not every invitation needs a yes"),
    card("3", "Bring a worry to God", "Name it in prayer, then leave it there"),
]))
f["d05-3"] = page("Peace 3", cta("3 / 3", *REP_LAST))

# d06 Mon 7 Dec: Christmas content ideas
f["d06-1"] = page("Christmas ideas 1", textcover("1 / 4", "CREATOR IDEAS", "Christmas content for every creator.",
                                                 "You don't need to preach to share the meaning of Christmas."))
f["d06-2"] = page("Christmas ideas 2", listslide("2 / 4", "Pick one and film it this week", [
    card("₦", "Finance", "Enjoying Christmas without starting January in debt"),
    card("♥", "Health", "Resting well when the season is busy"),
    card("∞", "Family", "One tradition that keeps Christ at the centre"),
    card("↗", "Career", "A year-end review, with gratitude"),
    card("♪", "Creatives", "A carol, a poem or a short skit"),
]))
f["d06-3"] = page("Christmas ideas 3", listslide("3 / 4", "Then post it on Worsship", [
    card("1", "Tap Upload", "Choose Video, Photo or Carousel"),
    card("2", "Add a reflection caption", "Say why it matters to you"),
    card("3", "Add a scripture reference", "Anchor it in the Word"),
    card("4", "Pick background music", "Browse by worship mood"),
]))
f["d06-4"] = page("Christmas ideas 4", cta("4 / 4", "Save this for later.", "Share the reason for the season.",
                                           "Faith, money, health, career and family. Every part of life, through a Christian lens.", "Start creating"))

# d07 Wed 9 Dec: Upload tutorial (Christmas)
f["d07-1"] = page("Christmas upload 1", cover("1 / 5", "UPLOAD TUTORIAL",
                                              f'Post your first <span style="color: {TEAL_LT}">Christmas</span> video',
                                              "Four steps from your camera roll to the Worsship feed.",
                                              L("up-full"), "The Worsship upload screen titled Share your Light"))
f["d07-2"] = page("Christmas upload 2", step("2 / 5", "1", "Tap Upload, then Video",
                                             "MP4, MOV or WebM, up to 500 MB. You can also post a photo or a carousel.",
                                             L("up-type"), "Upload screen with Video, Photo and Carousel options", width=720))
f["d07-3"] = page("Christmas upload 3", step("3 / 5", "2", "Add a caption and scripture",
                                             "Write a short reflection, then add references like Luke 2:10 or Isaiah 9:6.",
                                             L("up-caption"), "Reflection caption and scripture reference fields", width=900))
f["d07-4"] = page("Christmas upload 4", step("4 / 5", "3", "Pick background music",
                                             "Browse the Music Library by worship mood. Then publish. You can keep browsing while it uploads.",
                                             L("up-music"), "Add background music field", width=900))
f["d07-5"] = page("Christmas upload 5", cta("5 / 5", "Share your Light.", "Your story could be someone's Christmas gift.",
                                            "Get Worsship and post your first video this week.", "Post a video"))

# d08 Fri 11 Dec: Christmas quiz + Daily Faith Challenge (DFC #1)
f["d08-1"] = page("Christmas quiz 1", quiz("Christmas quiz.", "In Luke 2, who first heard the news of Jesus' birth from an angel?",
                                           ["Wise men", "Shepherds", "Priests", "An innkeeper"], "Comment A, B, C or D. Answer on the next slide."))
f["d08-2"] = page("Christmas quiz 2", cta("2 / 2", "Answer: B, the shepherds (Luke 2:8-11).", "Got a question that would stretch us?",
                                          "Every third video on Worsship is a Daily Faith Challenge. Email your question to support@worsship.com and tell us how you'd like to be credited.",
                                          "Play today's challenge"))

# d09 Sat 12 Dec: rep your church
f["d09"] = page("Rep your church 12 Dec", repsat("Carol season is here.", "Snap it. Frame it. Rep it.",
                                                 "Wearing your Christmas best to church tomorrow? Turn your photo into your Sunday Worship Frame."))

# d10 Sun 13 Dec: Joy
f["d10-1"] = page("Joy 1", scripture("1 / 3", "ADVENT: JOY",
                                     "Do not be afraid. I bring you good news that will cause great joy for all the people.",
                                     "Luke 2:10 (NIV)", "The first Christmas news was for ordinary people at work. It's for you too."))
f["d10-2"] = page("Joy 2", listslide("2 / 3", "Share some joy this week", [
    card("1", "Tell your testimony", "One thing God has done for you this year"),
    card("2", "Encourage someone", "Send a message to someone who needs it"),
    card("3", "Celebrate a creator", "Comment on a video that blessed you"),
]))
f["d10-3"] = page("Joy 3", cta("3 / 3", *REP_LAST))

# d11 Mon 14 Dec: phone filming tips
f["d11-1"] = page("Filming tips 1", textcover("1 / 3", "CREATOR TIPS", "No studio? No problem.",
                                              "Four phone tips for clearer Christmas videos."))
f["d11-2"] = page("Filming tips 2", listslide("2 / 3", "Save these before you film", [
    card("1", "Face the light", "Stand facing a window, not with it behind you"),
    card("2", "Keep it steady", "Prop your phone up or use a stand"),
    card("3", "Get close for sound", "Film somewhere quiet, close to the mic"),
    card("4", "One message per video", "Short and clear beats long and busy"),
]))
f["d11-3"] = page("Filming tips 3", cta("3 / 3", "Which tip will you try first?", "Your phone is enough.",
                                        "Film it, open Worsship, tap Upload and share what God has put on your heart.", "Post a video"))

# d12 Wed 16 Dec: Daily Faith Challenge tutorial (DFC #2)
f["d12-1"] = page("DFC holidays 1", cover("1 / 4", "DAILY FAITH CHALLENGE",
                                          f'Keep your streak through the <span style="color: {TEAL_LT}">holidays</span>',
                                          "One Bible question a day, right in your feed.",
                                          L("ch-full"), "A Daily Faith Challenge question with four answer options"))
f["d12-2"] = page("DFC holidays 2", step("2 / 4", "1", "Find it in your feed",
                                         "It appears every third video. You can also open it from your notifications.",
                                         L("ch-q"), "Challenge question with options A to D", width=640))
f["d12-3"] = page("DFC holidays 3", step("3 / 4", "2", "Answer, then come back tomorrow",
                                         "Read why the answer is right and keep your streak going, even on holiday.",
                                         L("ch-streak"), "A correct answer with a 1 Day Streak badge", width=420))
f["d12-4"] = page("DFC holidays 4", cta("4 / 4", "Got a question that would stretch us?", "Write a future challenge.",
                                        "Email your question to support@worsship.com and tell us how you'd like to be credited.", "Play today's challenge"))

# d13 Fri 18 Dec: church traditions
f["d13"] = page("Church Christmas tradition", f'''<div style="{BASE}; background: {OFF}; color: {INK}">
{star(910, 170, 60, VIOLET)}{star(995, 280, 32, TEAL)}
{top(False, "")}
<div style="display: flex; flex-direction: column; gap: 20px; position: relative">
<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 500; font-size: 56px; color: {VIOLET}">Tell us.</p>
<h1 style="margin: 0; font-size: 88px; line-height: 1.0; font-weight: 900; letter-spacing: -2px; color: {BLUE}">What's your church's Christmas tradition?</h1>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; position: relative">
{option("A", "Carol service")}{option("B", "Christmas Day service")}{option("C", "Crossover night")}{option("D", "Something else (tell us!)")}
</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 16px; position: relative">
<div style="font-size: 32px; font-weight: 800">Comment A, B, C or D</div>
{footer(color=INK, size=24, icon=32, gap=34)}
</div>
</div>''')

# d14 Sat 19 Dec
f["d14"] = page("Rep your church 19 Dec", repsat("Last Sunday before Christmas.", "Rep your church tomorrow.",
                                                 "Carols, candles or Christmas colours: capture it in your Sunday Worship Frame."))

# d15 Sun 20 Dec: Love
f["d15-1"] = page("Love 1", scripture("1 / 3", "ADVENT: LOVE",
                                      "For God so loved the world that he gave his one and only Son.",
                                      "John 3:16 (NIV)", "The greatest gift was given in love. How will you share it this week?"))
f["d15-2"] = page("Love 2", listslide("2 / 3", "Three ways to share love this Christmas", [
    card("1", "Visit or call", "Someone who may be alone this season"),
    card("2", "Give quietly", "Meet a need without telling anyone"),
    card("3", "Speak life", "Tell someone what they mean to you"),
]))
f["d15-3"] = page("Love 3", cta("3 / 3", *REP_LAST))

# d16 Mon 21 Dec: testimony
f["d16-1"] = page("Testimony 1", textcover("1 / 3", "CHRISTMAS WEEK", "Your story is a testimony.",
                                           "Christmas is the perfect time to share what God has done."))
f["d16-2"] = page("Testimony 2", listslide("2 / 3", "A simple way to tell it", [
    card("1", "Where you were", "Set the scene in one or two lines"),
    card("2", "What God did", "Keep it honest and specific"),
    card("3", "Where you are now", "What changed for you"),
    card("4", "A scripture to hold on to", "Add it as your reference"),
]))
f["d16-3"] = page("Testimony 3", cta("3 / 3", "Someone needs to hear it.", "Share your testimony on Worsship.",
                                     "Film it on your phone, tap Upload and add the scripture that carried you.", "Share your story"))

# d17 Fri 25 Dec: Christmas Day
f["d17"] = page("Merry Christmas", single("Merry Christmas from Worsship.", "Unto us a child is born.",
                                          f'''<p style="margin: 0; font-size: 30px; font-weight: 800; color: {TEAL_LT}">Isaiah 9:6 (KJV)</p>
{p("How are you celebrating today? Share one word in the comments.")}''', size=108))

# d18 Sat 26 Dec
f["d18"] = page("Rep your church 26 Dec", repsat("Last Sunday of the year.", "Rep your church tomorrow.",
                                                 "End the year where you worship. Make your Sunday Worship Frame and tag us."))

# d19 Sun 27 Dec: year-end reflection
f["d19-1"] = page("Year end 1", scripture("1 / 3", "YEAR-END REFLECTION",
                                          "Because of the LORD's great love we are not consumed, for his compassions never fail.",
                                          "Lamentations 3:22 (NIV)", "Before the year ends, look back at His faithfulness."))
f["d19-2"] = page("Year end 2", listslide("2 / 3", "Three questions to reflect on", [
    card("1", "Where did God show up?", "Name one moment from this year"),
    card("2", "What did you learn?", "Carry the lesson into the new year"),
    card("3", "Who do you need to thank?", "Tell them before January"),
]))
f["d19-3"] = page("Year end 3", cta("3 / 3", *REP_LAST))

# d20 Mon 28 Dec: 2027 creator plan
f["d20-1"] = page("Creator plan 1", textcover("1 / 4", "NEW YEAR, NEW VOICE", "Your 2027 creator plan.",
                                              "Four steps to start creating from a Christian lens in January."))
f["d20-2"] = page("Creator plan 2", listslide("2 / 4", "Plan it in one evening", [
    card("1", "Pick your lane", "Faith, money, health, career, family or the arts"),
    card("2", "Pick a rhythm", "One or two videos a week you can keep"),
    card("3", "List four ideas", "Enough for your first month"),
    card("4", "Post the first one", "Done is better than perfect"),
]))
f["d20-3"] = page("Creator plan 3", listslide("3 / 4", "Set up on Worsship", [
    card("1", "Get Worsship", "Google Play or app.worsship.com"),
    card("2", "Set up your profile", "Tell people what you create about"),
    card("3", "Share your invite link", "Your referral code is your username"),
]))
f["d20-4"] = page("Creator plan 4", cta("4 / 4", "Built for the audience of One.", "Start the year creating.",
                                        "Save this, share it with a friend who should create, and post your first video in January.", "Join Worsship"))

# d21 Thu 31 Dec: New Year's Eve
f["d21"] = page("New Year's Eve", single("Happy New Year's Eve.", "One word for 2027?",
                                         f'''<p style="margin: 0; font-family: 'Playfair Display', serif; font-style: italic; font-size: 42px; line-height: 1.4; color: rgba(255,255,255,0.95)">"See, I am doing a new thing! Now it springs up; do you not perceive it?"</p>
<p style="margin: 0; font-size: 30px; font-weight: 800; color: {TEAL_LT}">Isaiah 43:19 (NIV)</p>
{p("Drop your word in the comments. At a crossover service tonight? Make your Sunday Worship Frame and tag " + TAG + ".", 36)}'''))

for k, html in f.items():
    with open(os.path.join(OUT, f"{k}.dc.html"), "w") as fh:
        fh.write(html)
print(" ".join(f"{k}.dc.html" for k in f))
