from Map import Map

map = Map()
map.set("aaaa", 6)
print(map.get("aaaa"))
map.set("aaaa", "asdfasdg")
print(map.get("aaaa"))
map.delete("aaaa")
print(map.get("aaaa"))