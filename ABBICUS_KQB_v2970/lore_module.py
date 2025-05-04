
import os
from collections import Counter

lore_terms = {}
lore_path = os.path.join(".", "lore")
stopwords = set(['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'])

def scanlore():
    global lore_terms
    if not os.path.exists(lore_path):
        print("[!] Lore folder not found.")
        return
    terms = {}
    files = []
    for filename in os.listdir(lore_path):
        if filename.endswith(".txt") or filename.endswith(".kqb"):
            files.append(filename)
            with open(os.path.join(lore_path, filename), "r", encoding="utf-8") as f:
                for line in f:
                    for word in line.strip().lower().split():
                        word = ''.join(c for c in word if c.isalnum())
                        if len(word) < 3 or word in stopwords:
                            continue
                        key = (word, filename)
                        terms[key] = terms.get(key, 0) + 1
    lore_terms = terms
    print(f"Files: {', '.join(files)}")
    print(f"Indexed {len(set(word for word, _ in lore_terms.keys()))} unique terms across lore.")

def health():
    if not lore_terms:
        print("[Health] No lore indexed yet.")
        return
    from collections import defaultdict
    flat_terms = Counter()
    files_for_rare = defaultdict(list)

    for (word, filename), count in lore_terms.items():
        flat_terms[word] += count
        if count == 1:
            files_for_rare[word].append(filename)

    common = flat_terms.most_common(10)
    rare = list(files_for_rare.keys())[:5]

    print("[GENERATING STORY HEALTH REPORT...]")
    print(f"[Book] Total Unique (Filtered) Tags: {len(flat_terms)}")
    print(f"[Rare Tags] Rare Narrative Tags: {len(rare)}")

    print("\n[Top Terms] Most Common Story Terms:")
    for word, count in common:
        print(f" - {word}: {count}")

    print("\n[Special Terms] Rare Terms:")
    for word in rare:
        print(f" - {word} (appears in: {', '.join(set(files_for_rare[word]))})")

def freq(term):
    count = sum(c for (w, _), c in lore_terms.items() if w == term)
    print(f"[FREQ] '{term}' appears {count} times.")
    return count

def relic(tag, enforcers, forbidden_words, sacred_words):
    count = sum(c for (w, _), c in lore_terms.items() if w == tag)
    ostriches = 0
    oso_units = 0

    if tag in forbidden_words:
        enforcers += 5
        print(f"[FORBIDDEN RELIC] '{tag}' triggered +5 Enforcers!")
    elif tag in sacred_words:
        oso_units += 3
        ostriches += 1
        print(f"[SACRED RELIC] '{tag}' blessed your cause: +3 Oso Units, +1 Ostrich!")

    if count > 0:
        print(f"[RELIC UNLOCKED] '{tag}' appears {count} times.")
    else:
        print(f"[RELIC LOCKED] '{tag}' not found in lore.")
    return enforcers, oso_units, ostriches