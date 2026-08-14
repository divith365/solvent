import cv2
import numpy as np
import os
import glob

def crop_cards(img_path, prefix):
    img = cv2.imread(img_path)
    if img is None:
        return
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # The background is light blue/cyan, the cards are white.
    # White is usually 255. Let's threshold everything close to white.
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Some cards might have images at the top which aren't white.
    # But the cards have a distinct white body.
    # Let's use a slightly different approach: Canny edge detection or adaptive threshold
    # The cards have rounded corners and drop shadows.
    # Actually, a simple threshold might break the card into two if the top image is dark.
    # A better way is to find the bounding boxes of connected components of the "content"
    # Or just use the original grid logic but with EXACT manual coordinates.
    pass

