from PIL import Image

def composite_mockup():
    bg = Image.open('images/mockup_pc_white.png')
    fg = Image.open('images/faq_ui.png')
    
    # 1. Composite UI onto the laptop screen
    # These are estimated coordinates for the screen in the 1024x1024 image
    screen_x = 135
    screen_y = 155
    screen_w = 754
    screen_h = 486
    
    # Resize the UI image to fit the screen width, and crop the height if necessary
    fg_ratio = fg.width / fg.height
    screen_ratio = screen_w / screen_h
    
    if fg_ratio > screen_ratio:
        # fg is wider, scale by height
        new_h = screen_h
        new_w = int(new_h * fg_ratio)
        fg = fg.resize((new_w, new_h), Image.LANCZOS)
        # Crop the sides
        left = (new_w - screen_w) // 2
        fg = fg.crop((left, 0, left + screen_w, screen_h))
    else:
        # fg is taller, scale by width
        new_w = screen_w
        new_h = int(new_w / fg_ratio)
        fg = fg.resize((new_w, new_h), Image.LANCZOS)
        # Crop the bottom (since UI usually flows downwards)
        fg = fg.crop((0, 0, screen_w, screen_h))
        
    bg.paste(fg, (screen_x, screen_y))
    
    # 2. Crop the massive white borders so the laptop fills the thumbnail
    # The laptop is roughly between y=100 and y=800, and x=50 and x=974
    # Let's crop it tightly
    crop_x = 30
    crop_y = 110
    crop_w = 964
    crop_h = 650
    bg = bg.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
    
    bg.save('images/c3_mockup.png')
    print("Composite created successfully!")

if __name__ == "__main__":
    composite_mockup()
