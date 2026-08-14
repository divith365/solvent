from PIL import Image

img = Image.open('/home/arun/solvent/Build.jpeg')
W, H = 935, 620
cw = (W - 3 * 15) / 4
ch = (H - 15) / 2

for r in range(2):
    for c in range(4):
        x0 = 45 + c * (cw + 15)
        y0 = 710 + r * (ch + 15)
        x1 = x0 + cw
        y1 = y0 + ch
        card = img.crop((x0, y0, x1, y1))
        # Save as PNG to avoid all compression artifacts!
        card.save(f'/home/arun/solvent/card_{r}_{c}.png')
