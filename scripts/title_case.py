"""Apply Title Case to every title and heading of an HTML deck (slides-design skill).

Usage:
    python title_case.py deck.html [--dry-run] [--classes sub-h,eyebrow,k]

Rule (always, for English decks): capitalise the first and last word and every major word; keep minor words
(a, an, the, and, but, or, nor, for, of, on, in, to, at, by, with, as, per, via, vs) lower-case in the middle.
Hyphenated words capitalise each part ("Self-Operated", "Singapore-Based"). Words that already contain a capital
(NextAPI, BitSpace, API, OCI, SaaS, R&D) are left exactly as written. Wording is never changed — only case.

Touches: <h1>-<h6> whose content is plain text (no child tags), plus elements with one of --classes
(default: sub-h, eyebrow, k, sub, panel-title, label-lg) whose content is plain text. Prints every change.
Chinese headings are unaffected (no Latin letters to change).
"""
import argparse
import re
from pathlib import Path

MINOR = {"a", "an", "the", "and", "but", "or", "nor", "for", "of", "on", "in", "to", "at", "by", "with", "as",
         "per", "via", "vs"}


def cap_part(p):
    return p[:1].upper() + p[1:] if p[:1].isalpha() and p[:1].islower() else p


def cap_word(w, edge):
    if not re.search("[A-Za-z]", w) or w.startswith("&"):
        return w
    core = w.strip("()[]\"'“”‘’,.:;!?")
    if core.lower() in MINOR and not edge:
        return w
    return "-".join(p if any(c.isupper() for c in p) else cap_part(p) for p in w.split("-"))


def title_case(text):
    words = text.split(" ")
    idx = [i for i, w in enumerate(words) if re.search("[A-Za-z]", w)]
    out = []
    for i, w in enumerate(words):
        if i not in idx:
            out.append(w)
            continue
        # first word, last word, and the first word after a colon count as edges
        after_colon = i > 0 and words[i - 1].endswith(":")
        out.append(cap_word(w, i == idx[0] or i == idx[-1] or after_colon))
    return " ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--classes", default="sub-h,eyebrow,k,sub,panel-title,label-lg")
    a = ap.parse_args()

    path = Path(a.deck)
    html = path.read_text(encoding="utf-8")
    changes = []

    def fix(m):
        inner = m.group(3)
        new = title_case(inner)
        if new != inner:
            changes.append((inner, new))
        return m.group(1) + new + m.group(4)

    html = re.sub(r"(<(h[1-6])\b[^>]*>)([^<]*)(</\2>)", fix, html)
    cls = "|".join(re.escape(c) for c in a.classes.split(",") if c)
    html = re.sub(r'(<(\w+)\b[^>]*class="(?:[^"]*\s)?(?:' + cls + r')(?:\s[^"]*)?"[^>]*>)([^<]*)(</\2>)', fix, html)

    for old, new in changes:
        print(f"{old!r} -> {new!r}")
    print(f"{len(changes)} change(s){' (dry run)' if a.dry_run else ''}")
    if not a.dry_run and changes:
        path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
