
# sentinel_module.py

sentinels = 0
sentinel_shards = 0

def reset_sentinels():
    global sentinels, sentinel_shards
    sentinels = 0
    sentinel_shards = 0

def get_sentinel_count():
    return sentinels

def get_shard_count():
    return sentinel_shards

def add_sentinel_shards(amount):
    global sentinel_shards, sentinels
    sentinel_shards += amount
    if sentinel_shards >= 5:
        new_sentinels = sentinel_shards // 5
        if new_sentinels > 0:
            sentinels += new_sentinels
            sentinel_shards %= 5
            print(f"[ALERT] {new_sentinels} Sentinel(s) born from the shards.")

def report():
    print(f"[SENTINEL REPORT] Sentinels: {sentinels} | Shards: {sentinel_shards}")
