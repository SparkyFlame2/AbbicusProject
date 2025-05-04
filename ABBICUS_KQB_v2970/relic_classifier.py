
# relic_classifier.py

relic_tags = {
    "kai": "truth",
    "alara": "mythic",
    "echo": "truth",
    "fracture": "corrupted",
    "vault": "lost",
    "can": "truth",
    "authority": "corrupted",
    "archivists": "truth",
    "origin": "mythic",
    "shutdown": "fake",
    "freedom": "truth",
    "guardian": "mythic",
    "watchers": "corrupted",
    "paradox": "lost",
    "creator": "truth",
    "seize": "corrupted"
}

# Set of relics the player has unlocked
unlocked_relics = set()

def classify_relic(tag):
    classification = relic_tags.get(tag.lower(), "unclassified")
    if classification != "unclassified":
        unlocked_relics.add(tag.lower())
    return classification

def count_unlocked_relics():
    return len(unlocked_relics)