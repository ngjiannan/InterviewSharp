import collections, hashlib, importlib, json, os, random, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "mcq"))
EXPECT = {"Easy": 30, "Medium": 60, "Hard": 70, "Expert": 40}
ORDER = {"Easy": 0, "Medium": 1, "Hard": 2, "Expert": 3}
TRACKS = {
    "angular": ("Angular", ["angular_easy_medium", "angular_hard", "angular_expert"]),
    "dotnet": (".NET / C#", ["dotnet_easy_medium", "dotnet_hard", "dotnet_expert"]),
}


def build(track):
    title, mods = TRACKS[track]
    Q = []

    def m(level, topic, text, options, correct, hint, explanation, code=None):
        assert level in EXPECT, (text, level)
        assert 4 <= len(options) <= 5, text
        assert len(set(options)) == len(options), text
        assert correct and len(set(correct)) == len(correct) and all(0 <= c < len(options) for c in correct), text
        assert len(correct) < len(options), text
        if len(correct) > 1:
            assert "Select all that apply" in text, text
            rng = random.Random(hashlib.sha1(text.encode()).hexdigest())
            perm = list(range(len(options)))
            rng.shuffle(perm)
            options, correct = [options[p] for p in perm], [perm.index(c) for c in correct]
        Q.append({"level": level, "topic": topic, "text": text, "options": options, "correct": sorted(correct),
                  "hint": hint, "explanation": explanation, "code": code})

    for mod in mods:
        importlib.import_module(mod).add(m)
    c = collections.Counter(x["level"] for x in Q)
    assert dict(c) == EXPECT, (track, c)
    assert len({x["text"] + (x["code"] or "") for x in Q}) == len(Q), \
        [t for t, n in collections.Counter(x["text"] + (x["code"] or "") for x in Q).items() if n > 1]
    Q.sort(key=lambda x: ORDER[x["level"]])
    for i, x in enumerate(Q, 1):
        x["id"] = i
        x["key"] = hashlib.sha1((x["text"] + (x["code"] or "")).encode("utf-8")).hexdigest()[:12]
    assert len({x["key"] for x in Q}) == len(Q)
    multi = sum(len(x["correct"]) > 1 for x in Q)
    pos = collections.Counter(x["correct"][0] for x in Q if len(x["correct"]) == 1)

    with open(os.path.join(ROOT, f"mcq_{track}.json"), "w", encoding="utf-8") as f:
        json.dump(Q, f, indent=1, ensure_ascii=False)
    with open(os.path.join(ROOT, f"mcq_{track}.md"), "w", encoding="utf-8") as f:
        f.write(f"# {title} MCQ practice (with answers)\n\n")
        lvl = None
        for x in Q:
            if x["level"] != lvl:
                lvl = x["level"]; f.write(f"\n## {lvl}\n\n")
            f.write(f"### {x['id']}. [{x['topic']}] {x['text']}\n\n")
            if x["code"]:
                f.write("```\n" + x["code"] + "\n```\n\n")
            for i, o in enumerate(x["options"]):
                f.write(f"- {'ABCDE'[i]}. {o}\n")
            f.write("\n**Answer:** " + ", ".join("ABCDE"[i] for i in x["correct"]) + f"\n\n**Explanation:** {x['explanation']}\n\n")
    print(track, dict(c), "multi-select:", multi, "single-answer positions:", dict(sorted(pos.items())))


for t in TRACKS:
    build(t)
