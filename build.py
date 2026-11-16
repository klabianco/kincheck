# Build the site (index.html = protocol spec, cards.html = card generator)
# from the templates in src/ and the 256-word list.
# Checks the list: 256 unique words, at most 9 letters, and no shared 4-letter
# endings (rhymes like rocket/pocket are easy to mishear on a phone) except
# groups reviewed by ear below.
import collections, json, sys

REVIEWED_OK = [  # share an ending but sound clearly different on a call
    {"bucket", "cricket", "jacket", "rocket"}, {"butter", "otter"},
    {"captain", "curtain", "fountain"}, {"castle", "whistle"}, {"diamond", "almond"},
    {"doctor", "tractor"}, {"drummer", "hammer"}, {"fiddle", "paddle"},
    {"lobster", "rooster"}, {"napkin", "pumpkin"}, {"pepper", "zipper"},
    {"pickle", "buckle"}, {"popcorn", "unicorn"}, {"barrel", "squirrel"},
]

words = [l.strip() for l in open("src/wordlist.txt") if l.strip()]
problems = []
if len(words) != 256: problems.append(f"need 256 words, have {len(words)}")
if len(set(words)) != len(words): problems.append("duplicate words")
problems += [f"too long: {w}" for w in words if len(w) > 9 or not w.isalpha()]
groups = collections.defaultdict(set)
for w in words: groups[w[-4:]].add(w)
for end, g in groups.items():
    if len(g) > 1 and not any(g <= ok for ok in REVIEWED_OK):
        problems.append(f"possible rhyme (-{end}): {sorted(g)}")
if problems: sys.exit("word list rejected:\n  " + "\n  ".join(problems))

for name in ("index", "cards"):
    t = open(f"src/{name}.template.html").read()
    open(f"{name}.html", "w").write(t.replace("__WORDS__", json.dumps(words)))
print("built index.html and cards.html with", len(words), "words")
