class Image:
    def __init__(self, layout=None, dx=None, dy=None, width=None, height=None):
        self.layout = layout
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height


def get_result():
    with open("input.txt") as file:
        tokens = []
        image = None
        for line_num, line in enumerate(file):
            if line_num == 0:
                w, h, c = map(int, line.split())
            else:
                if line == "\n":
                    tokens.append("\n")
                else:
                    t, image = tokenize(line, image)
                    tokens.extend(t)

    result = []
    surroundings = {} 
    cursor_x, cursor_y = 0, 0 
    fragment_start = 0
    current_h = h
    previous_floating = None

    for token in tokens:
        if token == "\n":
            cursor_x = 0
            candidate1 = cursor_y + current_h 
            
            lowest = 0
            for (x, y), image in surroundings.items():
                y_check = y + image.height
                if y_check > lowest:
                    lowest = y_check
            candidate2 = lowest

            cursor_y = max(candidate1, candidate2)
            previous_floating = None
            continue

        if cursor_x == 0:
            borders = _get_line_borders(cursor_y, surroundings, w, 0)
            fragment = borders.pop(0)
            fragment_start = fragment[0]
            cursor_x = fragment_start
            current_h = h

        while not _feats(token, fragment, c, cursor_x, fragment_start):
            try:
                fragment = borders.pop(0)
                fragment_start = fragment[0]
                cursor_x = fragment_start
            except IndexError:
                cursor_y += current_h
                current_h = h 
                borders = _get_line_borders(cursor_y, surroundings, w, 0)
                fragment = borders.pop(0)
                fragment_start = fragment[0]
                cursor_x = fragment_start

        if isinstance(token, Image):
            if token.layout == "floating":
                if previous_floating:
                    start_x, start_y = previous_floating
                else:
                    start_x, start_y = cursor_x, cursor_y
                img_x = max(0, start_x + token.dx)
                diff = min(0, w - (img_x + token.width))
                img_x += diff
                result.append((img_x, start_y + token.dy))
                previous_floating = (img_x + token.width, start_y + token.dy)
            elif token.layout == "embedded":
                is_cursor_fragment = (cursor_x != fragment_start) * c
                result.append((cursor_x + is_cursor_fragment, cursor_y))
                cursor_x += token.width + is_cursor_fragment
                current_h = max(current_h, token.height)
                previous_floating = None
            elif token.layout == "surrounded":
                result.append((cursor_x, cursor_y))
                surroundings[(cursor_x, cursor_y)] = token
                cursor_x += token.width
                fragment_start = cursor_x
                previous_floating = None
        else:
            cursor_x += (len(token) + (cursor_x != fragment_start)) * c
            previous_floating = None

    for pair in result:
        print(f"{pair[0]} {pair[1]}")


def _get_line_borders(y, surroundings, w, fragment_start):
    image_borders = []
    for (image_x, image_y), image in surroundings.items():
        if image_y <= y < image_y + image.height:
            image_borders.extend([image_x, image_x + image.width])
    
    image_borders = [border for border in sorted(image_borders) if border >= fragment_start]
    fragment_borders = []
    inside = False
    for index, border in enumerate(image_borders):
        if index == 0 and border == fragment_start:
            inside = True