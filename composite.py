from PIL import Image
import numpy as np

# Load the user's uploaded image
img = Image.open('/Users/rioshibata/.gemini/antigravity/brain/87d9cab2-f11c-42da-a9f2-008a8de39a64/media__1778907257048.png').convert('RGBA')

# Convert to numpy array
data = np.array(img)

# The background is black (0, 0, 0).
# Let's find all pixels that are very close to black and change them to pure white.
# We must be careful not to turn the laptop bezel (which is also black/dark grey) white.
# Usually, background replacement is hard without a mask.
# But wait, we can just crop the image so only the laptop and screen remain, then place it on a white background.

# Let's crop out the bottom garbage. The image is 752px tall. The bottom 152px is probably garbage.
img_cropped = img.crop((0, 0, 1024, 600))

# Save the cropped image
img_cropped.save('/Users/rioshibata/Workspace/images/c3_mockup_clean.png')

# Let's see if we can just make it look good in CSS.
