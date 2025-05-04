
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

def classify_relic(tag):
    return relic_tags.get(tag.lower(), "unclassified")
