from PIL import Image
img = Image.open('deliver.jpeg')
# Let's adjust bounds: left was 50 (too much left margin). Try 60.
# right was 975 (cut off right). Try 980.
# width = 920
# cw = (920 - 60) / 4 = 215. Let's try width 225.
# Let's just crop x: 60 to 285. y: 480 to 740.
card = img.crop((60, 480, 285, 740))
card.save('test_crop.png')
