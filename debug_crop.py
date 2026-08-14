import cv2

def draw_grid(img_name, cols, rows, left, top, right, bottom, custom_row_counts=None):
    img = cv2.imread(f'{img_name}.jpeg')
    if img is None: return
    W = right - left
    H = bottom - top
    cw = int((W - (cols - 1) * 20) / cols)
    ch = int((H - (rows - 1) * 20) / rows)
    
    for r in range(rows):
        cards = cols if not custom_row_counts else custom_row_counts[r]
        row_w = cards * cw + (cards - 1) * 20
        start_x = int(left + (W - row_w) / 2)
        
        for c in range(cards):
            x0 = start_x + c * (cw + 20)
            y0 = top + r * (ch + 20)
            x1 = x0 + cw
            y1 = y0 + ch
            cv2.rectangle(img, (int(x0), int(y0)), (int(x1), int(y1)), (0, 0, 255), 2)
            
    cv2.imwrite(f'debug_{img_name}.jpeg', img)

draw_grid('deliver', 4, 3, 50, 480, 975, 1330, [4, 4, 2])
