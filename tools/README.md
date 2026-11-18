# Post design tools

How Worsship social posts are made (used by Claude's weekly and monthly scheduled tasks).

1. Write a generator like `gen_nov.py` (helpers in `kit.py`: cover, step, cta, card; footers in `socials.py`).
   Images: `/_local/<name>.png` loads from `crops/` (cleaned app screenshots, no real user data).
2. Generate: `python3 -I gen_X.py <abs src dir>` (copy `support.js` into the src dir).
3. Render: `python3 -I render.py <abs src dir> <abs out dir> <abs path to this tools folder> <names...>` (1080x1350 PNG).
4. Convert to JPEG (TikTok rejects PNG) and commit to `2026-MM-weekN/`.
5. Schedule in Metricool (brand 7634472, Africa/Lagos) using the raw.githubusercontent.com URLs.

Rules: no real usernames, bank details or user numbers; sample figures labelled; claims only about shipped features.
