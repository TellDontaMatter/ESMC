"""Builds dist/index.html from index.template.html + events.json.
Muse (or anyone) only edits events.json. Do not hand-edit the events list in the template."""
import json, html, os, re, sys

FIELDS = ("date", "time", "name", "place", "link")
events = json.load(open("events.json", encoding="utf-8"))
for i, e in enumerate(events):
    missing = [f for f in FIELDS if not str(e.get(f, "")).strip()]
    if missing:
        sys.exit(f"events.json entry {i+1} is missing: {', '.join(missing)}")
    if not re.match(r"^https://(www\.)?facebook\.com/events/\d+/?$", e["link"]):
        sys.exit(f"events.json entry {i+1}: link must be a Facebook event URL, got {e['link']}")

def row(e):
    esc = lambda v: html.escape(str(v), quote=True)
    return f"""      <article class="event-row">
        <div class="event-date">{esc(e['date'])}<span class="event-time">{esc(e['time'])}</span></div>
        <div>
          <h3 class="event-name"><a href="{esc(e['link'])}" target="_blank" rel="noopener noreferrer">{esc(e['name'])}</a></h3>
          <p class="event-place">{esc(e['place'])}</p>
        </div>
      </article>
"""

tpl = open("index.template.html", encoding="utf-8").read()
start, end = "<!-- EVENTS:START -->", "<!-- EVENTS:END -->"
if tpl.count(start) != 1 or tpl.count(end) != 1:
    sys.exit("template markers missing")
out = re.sub(re.escape(start) + r".*?" + re.escape(end),
             start + "\n" + "\n".join(row(e) for e in events) + "      " + end, tpl, flags=re.S)
os.makedirs("dist", exist_ok=True)
open("dist/index.html", "w", encoding="utf-8").write(out)
print(f"Built dist/index.html with {len(events)} events")
