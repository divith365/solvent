import cv2
import numpy as np
import os

if not os.path.exists('cards'):
    os.makedirs('cards')

def auto_crop(filename, prefix, expected_count=None):
    img = cv2.imread(filename)
    if img is None: return
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Threshold to find white cards. Background is usually light blue.
    # Cards have drop shadows, so we should be careful.
    _, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        area = w * h
        # Card should be reasonably large, say > 20000 pixels
        # Typical card is 215x270 ~ 58000.
        if area > 15000 and area < 400000:
            # Aspect ratio check: usually taller than wide or roughly square
            if h > w * 0.5:
                boxes.append((x, y, w, h))
                
    if not boxes:
        print(f"No boxes found for {filename}")
        return
        
    # Remove boxes that are too small relative to the largest box
    max_area = max(w*h for x,y,w,h in boxes)
    valid_boxes = [b for b in boxes if b[2]*b[3] > max_area * 0.4]
    
    # Sort boxes by row, then by column
    # Group by Y coordinate (allow 50px tolerance)
    valid_boxes.sort(key=lambda b: b[1])
    
    rows = []
    current_row = [valid_boxes[0]]
    for b in valid_boxes[1:]:
        if abs(b[1] - current_row[0][1]) < 50:
            current_row.append(b)
        else:
            rows.append(current_row)
            current_row = [b]
    rows.append(current_row)
    
    # Sort each row by X and flatten
    final_boxes = []
    for r in rows:
        r.sort(key=lambda b: b[0])
        final_boxes.extend(r)
        
    print(f"{filename}: Found {len(final_boxes)} cards")
    
    # Crop and save
    count = 0
    for i, (x, y, w, h) in enumerate(final_boxes):
        if expected_count and count >= expected_count: break
        
        # Add a tiny 2px padding to avoid clipping if necessary
        px = max(0, x - 2)
        py = max(0, y - 2)
        pw = min(img.shape[1] - px, w + 4)
        ph = min(img.shape[0] - py, h + 4)
        
        card = img[py:py+ph, px:px+pw]
        cv2.imwrite(f'cards/{prefix}_{count}.png', card)
        count += 1

auto_crop('deliver.jpeg', 'deliver', 10)
auto_crop('deliver1.jpeg', 'deliver1', 10)
auto_crop('protect.jpeg', 'protect', 12)
auto_crop('protect1.jpeg', 'protect1', 9)
auto_crop('why.jpeg', 'why', 10)
auto_crop('why1.jpeg', 'why1', 10)

