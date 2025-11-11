def word_count(text):
    return len(text.split())


def count_characters(content):
    amount = {}
    content = content.lower()
    for ch in content:
        if ch in amount:
            amount[ch] += 1
        else:
            amount[ch] = 1
    return amount 

def sorting_help(item):
    return item["num"]


def sorted_characters(amounts):
    results = []
    for ch, count in amounts.items():
        if not ch.isalpha():
            continue
        results.append({"char": ch, "num": count})
    results.sort(reverse=True, key=sorting_help)
       
    return results

    




