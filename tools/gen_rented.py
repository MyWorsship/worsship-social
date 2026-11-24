"""Mon 14 Dec: Your ministry shouldn't live on rented land (carousel)."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nov_helpers import page, textcover, listslide, card, cta  # noqa: E402

OUT = sys.argv[1]
files = {
    "r-1": page("Rented land 1", textcover(
        "1 / 4", "FOR FAITH CREATORS", "Two pages. Just in case.",
        "Why do so many of us open a backup account the same week we start?")),
    "r-2": page("Rented land 2", listslide("2 / 4", "Why the backup page?", [
        card("1", "Context gets misread", "A sermon, a testimony or a prayer read by a system that doesn't know faith"),
        card("2", "No one to talk to", "An appeal that ends in a template reply"),
        card("3", "Years of work at risk", "Your audience and archive in one place you don't control"),
    ])),
    "r-3": page("Rented land 3", listslide("3 / 4", "What we built on Worsship", [
        card("✓", "Reviewed with faith in mind", "Held posts are checked by people who understand faith content"),
        card("✓", "No dead ends", "See the status of any held or removed post, with time to appeal"),
        card("✓", "Your faith, kept private", "Faith details are only stored with your consent"),
    ])),
    "r-4": page("Rented land 4", cta(
        "4 / 4", "Matthew 7:24", "Build on solid ground.",
        "Your ministry shouldn't live on rented land. Worsship is a home for faith creators, built by people who share your values.",
        "Join Worsship")),
}
for k, html in files.items():
    with open(os.path.join(OUT, f"{k}.dc.html"), "w") as fh:
        fh.write(html)
print(" ".join(f"{k}.dc.html" for k in files))
