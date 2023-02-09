string = "red2 blue5 black4 green1 gold3"
if 2 <=len(string) <=200:
    colors = list(string)
    colors.reverse()
    colors = "".join(colors)
    colors = colors.split()
    colors.sort(reverse=True)
    colors = " ".join(colors)
    colors = list(colors)
    colors.reverse()
    colors = "".join(colors)
    print(colors)