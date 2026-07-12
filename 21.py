myStr = "a,a,a,b,b,c,c,c"
visited = []
final_list = []

for ch in myStr:
    if ch not in visited and ch != ',':
        final_list.append(f"{ch}:{myStr.count(ch)}")
        visited.append(ch)


print(final_list)
print(",".join(final_list))
