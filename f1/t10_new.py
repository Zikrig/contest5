import dataclasses as dt

def solve():
    with open("input.txt") as file:
        tks = []
        cur_im = None
        for line_num, line in enumerate(file):
            if line_num == 0:
                width, height, char_size = map(int, line.split())
            else:
                if line == "\n":
                    tks.append("\n")
                else:
                    t = []
                    for tk in line.split():
                        if tk.startswith("(image"):
                            cur_im = Img()

                        elif cur_im:
                            key, value = tk.split("=")
                            if value.endswith(")"):
                                if key == "layout":
                                    cur_im.__setattr__(key, value[:-1])
                                else:
                                    cur_im.__setattr__(key, int(value[:-1]))
                                t.append(cur_im)
                                cur_im = None
                            elif key == "layout":
                                setattr(cur_im, key, value)
                            else:
                                setattr(cur_im, key, int(value))

                        else:
                            t.append(tk)

                    tks.extend(t)

    cur_height, cur_x, cur_y, frag_st, res, sur_imgs, floating_hm = height, 0, 0, 0, [], {}, None

    for tk in tks:
        if tk == "\n":
            cur_x = 0
            sec = 0
            for (x, y), image in sur_imgs.items():
                if y + image.height > sec:
                    sec = y + image.height
            
            cur_y = max(cur_y + cur_height, sec)
            floating_hm = None
            continue

        if cur_x == 0:
            brdrs = limits(cur_y, sur_imgs, width, 0)
            fragment = brdrs.pop(0)
            frag_st, __ = fragment
            cur_x = frag_st
            cur_height = height

        while not can_be_placed(fragment, char_size, cur_x, frag_st, tk):
            try:
                fragment = brdrs.pop(0)
                frag_st, __ = fragment
                cur_x = frag_st
            except: 
                cur_y += cur_height
                cur_height = height 
                brdrs = limits(cur_y, sur_imgs, width, 0)
                fragment = brdrs.pop(0)
                frag_st, __ = fragment
                cur_x = frag_st

        if isinstance(tk, Img):
            if tk.layout == "embedded":
                res.append((cur_x + (cur_x != frag_st) * char_size, cur_y))
                cur_height = max(cur_height, tk.height)
                floating_hm = None
                cur_x += tk.width + (cur_x != frag_st) * char_size
            elif tk.layout == "floating":
                if not floating_hm:
                    start_x, start_y = cur_x, cur_y
                else:
                    start_x, start_y = floating_hm
                img_x = max(0, start_x + tk.dx)
                diff = min(0, width - img_x - tk.width)
                img_x += diff
                res.append((img_x, start_y + tk.dy))
                floating_hm = (img_x + tk.width, start_y + tk.dy)
            elif tk.layout == "surrounded":
                res.append((cur_x, cur_y))
                sur_imgs[(cur_x, cur_y)] = tk
                cur_x += tk.width
                frag_st = cur_x
                floating_hm = None
        else:
            additional = int(frag_st != cur_x)
            cur_x += char_size*(len(tk) + additional)
            floating_hm = None

    return res


def limits(y, images, w, frag_s):
    image_brdrs = []
    for (image_x, image_y), image in images.items():
        if image_y <= y < image_y + image.height:
            image_brdrs.append(image_x)
            image_brdrs.append(image_x + image.width)
    
    fragment_brdrs = []
    inside = False
    image_brdrs = list(filter(lambda x: x >= frag_s, sorted(image_brdrs)))
    for i, border in enumerate(image_brdrs):
        if i == 0 and border == frag_s:
            inside = True

        elif not inside:
            fragment_brdrs.append((frag_s, border))
            inside = True
        else:
            frag_s = border
            inside = False
    else:
        if frag_s != w:
            fragment_brdrs.append((frag_s, w))

    return fragment_brdrs


def can_be_placed(fragment, c, x, fragment_start, token):
    __, end = fragment
    x = fragment_start if x < fragment_start else x

    if isinstance(token, str):
        if x != fragment_start:
            token = " " + token

        mayb = x + len(token) * c
        return  mayb <= end
    
    if token.layout == "floating":
        return True

    size = token.width
    if token.layout == "embedded":
        mayb = x != fragment_start
        size += mayb * c

    return end >= x+size

@dt.dataclass
class Img:
    layout: str | None = None
    width: int | None = None
    height: int | None = None
    dx: int | None = None
    dy: int | None = None


res = solve()
for r in res:
    print(f"{r[0]} {r[1]}")