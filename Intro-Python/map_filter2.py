items = ["chair", "book", "bag"]

def return_item(item):
    if item[0] == "c":
        return item

items_map = map(return_item,items)

for x in items_map:
    print(x)


items_filter = filter(return_item, items)

for x in items_filter:
    print(x)