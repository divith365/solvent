import os
from PIL import Image

if not os.path.exists('cards'):
    os.makedirs('cards')

def crop_grid(img_name, prefix, cols, rows, left, top, right, bottom, total_cards, custom_row_counts=None):
    img = Image.open(f'{img_name}.jpeg')
    W = right - left
    H = bottom - top
    cw = (W - (cols - 1) * 20) / cols
    ch = (H - (rows - 1) * 20) / rows
    
    count = 0
    for r in range(rows):
        cards_in_this_row = cols
        if custom_row_counts and r < len(custom_row_counts):
            cards_in_this_row = custom_row_counts[r]
            
        # calculate centering offset for this row if it has fewer cards
        row_w = cards_in_this_row * cw + (cards_in_this_row - 1) * 20
        start_x = left + (W - row_w) / 2
        
        for c in range(cards_in_this_row):
            if count >= total_cards: break
            x0 = start_x + c * (cw + 20)
            y0 = top + r * (ch + 20)
            x1 = x0 + cw
            y1 = y0 + ch
            card = img.crop((x0, y0, x1, y1))
            card.save(f'cards/{prefix}_{count}.png')
            count += 1

# deliver.jpeg: 10 cards, 3 rows (4, 4, 2)
crop_grid('deliver', 'deliver', 4, 3, 50, 480, 975, 1330, 10, [4, 4, 2])

# deliver1.jpeg: 10 cards, 3 rows (4, 4, 2)
crop_grid('deliver1', 'deliver1', 4, 3, 50, 480, 975, 1330, 10, [4, 4, 2])

# protect.jpeg: 12 cards, 3 rows (4, 4, 4)
crop_grid('protect', 'protect', 4, 3, 50, 480, 975, 1330, 12)

# protect1.jpeg: 9 cards, 3 rows (4, 4, 1)
crop_grid('protect1', 'protect1', 4, 3, 50, 480, 975, 1330, 9, [4, 4, 1])

# why.jpeg: 10 cards, 5 rows (2, 2, 2, 2, 2)
crop_grid('why', 'why', 2, 5, 50, 400, 975, 1250, 10)

# why1.jpeg: 10 cards, 5 rows (2, 2, 2, 2, 2)
crop_grid('why1', 'why1', 2, 5, 50, 400, 975, 1250, 10)

# Move the 8 Build cards to the cards directory
for r in range(2):
    for c in range(4):
        if os.path.exists(f'card_{r}_{c}.png'):
            os.rename(f'card_{r}_{c}.png', f'cards/build_{r*4+c}.png')
