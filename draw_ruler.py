import cv2

def draw_ruler(img_name):
    img = cv2.imread(f'{img_name}.jpeg')
    if img is None: return
    
    H, W = img.shape[:2]
    
    # Draw horizontal lines
    for y in range(0, H, 50):
        color = (255, 0, 0) if y % 100 == 0 else (0, 0, 255)
        thickness = 2 if y % 100 == 0 else 1
        cv2.line(img, (0, y), (W, y), color, thickness)
        if y % 100 == 0:
            cv2.putText(img, str(y), (10, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            
    # Draw vertical lines
    for x in range(0, W, 50):
        color = (255, 0, 0) if x % 100 == 0 else (0, 0, 255)
        thickness = 2 if x % 100 == 0 else 1
        cv2.line(img, (x, 0), (x, H), color, thickness)
        if x % 100 == 0:
            cv2.putText(img, str(x), (x+5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            
    cv2.imwrite(f'ruler_{img_name}.jpeg', img)

draw_ruler('deliver')
