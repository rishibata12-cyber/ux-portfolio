from PIL import Image

def crop_mockups():
    # Crop PC mockup
    pc = Image.open('images/mockup_pc_white.png')
    pc = pc.crop((30, 110, 994, 760))
    pc.save('images/mockup_pc_white.png')
    
    # Crop App mockup
    app = Image.open('images/mockup_app_white.png')
    app = app.crop((150, 150, 874, 874))
    app.save('images/mockup_app_white.png')
    print("Mockups cropped successfully!")

if __name__ == "__main__":
    crop_mockups()
