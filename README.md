# ESMC — esmc.pages.dev

**To update events, edit `events.json` only.** Each push to `main` rebuilds the page and deploys it to the Cloudflare Pages project `esmc`.

Each event needs: `date`, `time`, `name`, `place`, `link` (a facebook.com/events/... URL). Soonest first, drop past events. If the listing doesn't give a place or time, write "See the Facebook event for details." Never add club-hosted events. Never invent a date, time or place. The build fails, and nothing deploys, if a field is blank or a link isn't a Facebook event URL.

Don't edit `index.template.html` for event changes.
