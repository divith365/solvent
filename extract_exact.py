import os
from PIL import Image

def get_box(r, c, start_x=95, start_y=490, cw=195, ch=265, gap_x=15, gap_y=15):
    x0 = start_x + c * (cw + gap_x)
    y0 = start_y + r * (ch + gap_y)
    return (x0, y0, x0 + cw, y0 + ch)

def crop_list(img_name, prefix, positions):
    img = Image.open(f'{img_name}.jpeg')
    for i, pos in enumerate(positions):
        if len(pos) == 2:
            r, c = pos
            box = get_box(r, c)
        else:
            box = pos
        card = img.crop(box)
        card.save(f'cards/{prefix}_{i}.png')

# deliver and deliver1: 10 cards (first two rows full, last row edges)
pos_10 = [(r, c) for r in range(2) for c in range(4)] + [(2, 0), (2, 3)]
crop_list('deliver', 'deliver', pos_10)
crop_list('deliver1', 'deliver1', pos_10)

# protect: 12 cards
pos_12 = [(r, c) for r in range(3) for c in range(4)]
crop_list('protect', 'protect', pos_12)

# protect1: 9 cards. Let's assume row 3 has 1 card at col 1? Or col 0?
# Actually, wait, let's just extract all 4 in row 3 and I'll keep the ones that are real.
# Or wait, if protect1 has 9 cards, maybe it's 4+4+1. Let's assume the 1 is centered.
# I will just extract (2,0), (2,1), (2,2), (2,3) and I can view them to see which one is the real card.
pos_protect1 = [(r, c) for r in range(2) for c in range(4)] + [(2, 0), (2, 1), (2, 2), (2, 3)]
crop_list('protect1', 'protect1', pos_protect1)

# For 'why' and 'why1', we need new coordinates. Let's just draw the ruler and check!
