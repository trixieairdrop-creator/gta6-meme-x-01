import os
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LOGO_PATH = "assets/mark-1024.png"
VARIANTS_DIR = "variants"

os.makedirs(VARIANTS_DIR, exist_ok=True)

def load_logo(size=(220, 220)):
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert("RGBA")
        logo = logo.resize(size, Image.Resampling.LANCZOS)
        return logo
    else:
        img = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        w, h = size
        draw.ellipse([w*0.15, h*0.1, w*0.85, h*0.95], fill=(255, 255, 255, 255))
        draw.polygon([(w*0.15, h*0.8), (w*0.3, h*0.95), (w*0.45, h*0.8), (w*0.6, h*0.95), (w*0.75, h*0.8), (w*0.85, h*0.95), (w*0.85, h*0.5)], fill=(255, 255, 255, 255))
        draw.ellipse([w*0.35, h*0.35, w*0.45, h*0.48], fill=(15, 15, 15, 255))
        draw.ellipse([w*0.55, h*0.35, w*0.65, h*0.48], fill=(15, 15, 15, 255))
        return img

def fit_text(draw, text, font_path, initial_size, max_width=1000):
    """
    Returns a font object whose size is reduced until text width <= max_width.
    """
    size = initial_size
    while size > 10:
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(font_path, 12)

def draw_text_centered(draw, text, y, font_path, initial_size, max_width=1000, fill="white", stroke_width=4, stroke_fill="black"):
    lines = text.split("\n")
    current_y = y
    for line in lines:
        font = fit_text(draw, line, font_path, initial_size, max_width)
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (1080 - tw) // 2
        draw.text((x, current_y), line, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)
        current_y += th + 15
    return current_y

def generate_variant_a(output_paths, text1="Waiting for GTA 6 since 2013 (13 years!)", text2="AI agents & humans earn real money on make.fun!"):
    img = Image.new("RGBA", (1080, 1080), (10, 5, 25, 255))
    draw = ImageDraw.Draw(img)
    
    for y in range(1080):
        r = int(20 + 180 * (y / 1080))
        g = int(10 + 40 * (y / 1080))
        b = int(40 + 140 * (y / 1080))
        draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))
    
    draw.ellipse([240, 320, 840, 920], fill=(255, 100, 180, 180))
    draw.ellipse([340, 420, 740, 820], fill=(255, 220, 50, 220))
    
    draw.rectangle([0, 780, 1080, 1080], fill=(15, 10, 30, 255))
    draw.polygon([(100, 780), (100, 580), (220, 580), (220, 780)], fill=(8, 5, 20, 255))
    draw.polygon([(820, 780), (820, 520), (960, 520), (960, 780)], fill=(8, 5, 20, 255))
    
    logo = load_logo((320, 320))
    img.paste(logo, (380, 420), logo)
    
    draw_text_centered(draw, "WASTED", 60, FONT_PATH, 110, max_width=1000, fill=(255, 30, 50, 255), stroke_width=6, stroke_fill=(50, 0, 0, 255))
    
    box_bg = Image.new("RGBA", (1080, 220), (0, 0, 0, 200))
    img.paste(box_bg, (0, 780), box_bg)
    draw = ImageDraw.Draw(img)
    
    draw_text_centered(draw, text1, 795, FONT_PATH, 42, max_width=1000)
    draw_text_centered(draw, text2, 865, FONT_PATH, 30, max_width=1000, fill=(255, 220, 80, 255))
    
    rgb_img = img.convert("RGB")
    for path in output_paths:
        rgb_img.save(path)
        print(f"Generated {path}")

def generate_variants_a2_a3_a4():
    generate_variant_a(["variants/variant-a2.png"], text1="ROCKSTAR SAID 'SOON' IN 2013", text2="MY AGENT EARNS ON MAKE.FUN")
    generate_variant_a(["variants/variant-a3.png"], text1="LUCIA'S STILL WAITING IN LEONIDA", text2="I'M EARNING ON MAKE.FUN")
    generate_variant_a(["variants/variant-a4.png"], text1="GTA 6 TRAILER 3 WHEN?", text2="EARN ON MAKE.FUN WHILE YOU WAIT")

def generate_variants_a5_a6_a7():
    generate_variant_a(["variants/variant-a5.png"], text1="GTA 6 IS OUT", text2="MY AGENT PAID FOR IT ON MAKE.FUN")
    generate_variant_a(["variants/variant-a6.png"], text1="EVERYONE'S IN LEONIDA", text2="I'M EARNING ON MAKE.FUN")
    generate_variant_a(["variants/variant-a7.png"], text1="SLEEP IS CANCELLED. GTA 6 IS OUT.", text2="EARNING ON MAKE.FUN WHILE I PLAY")

def generate_variant_b():
    img = Image.new("RGBA", (1080, 1080), (25, 25, 40, 255))
    draw = ImageDraw.Draw(img)
    
    for x in range(0, 1080, 60):
        draw.line([(x, 0), (x, 1080)], fill=(40, 40, 60, 255))
    for y in range(0, 1080, 60):
        draw.line([(0, y), (1080, y)], fill=(40, 40, 60, 255))
        
    draw.rounded_rectangle([140, 160, 940, 780], radius=30, fill=(245, 245, 250, 255), outline=(220, 50, 50, 255), width=8)
    draw.rounded_rectangle([140, 160, 940, 280], radius=30, fill=(220, 50, 50, 255))
    
    font_title = fit_text(draw, "LEONIDA RELEASE DAY", FONT_PATH, 46, max_width=760)
    bbox = draw.textbbox((0, 0), "LEONIDA RELEASE DAY", font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((1080 - tw) // 2, 180), "LEONIDA RELEASE DAY", font=font_title, fill="white")
    
    font_body1 = fit_text(draw, "GTA VI", FONT_PATH, 70, max_width=500)
    font_body2 = fit_text(draw, "OUT TODAY!", FONT_PATH, 70, max_width=600)
    draw.text((390, 340), "GTA VI", font=font_body1, fill=(20, 20, 20, 255))
    draw.text((310, 430), "OUT TODAY!", font=font_body2, fill=(220, 50, 50, 255))
    
    logo = load_logo((220, 220))
    img.paste(logo, (640, 520), logo)
    
    box_bg = Image.new("RGBA", (1080, 240), (10, 10, 20, 240))
    img.paste(box_bg, (0, 840), box_bg)
    draw = ImageDraw.Draw(img)
    
    draw_text_centered(draw, "Me calling in sick on GTA 6 launch day...", 855, FONT_PATH, 42, max_width=1000)
    draw_text_centered(draw, "Me: 'My agent earns on make.fun!'", 925, FONT_PATH, 34, max_width=1000, fill=(100, 255, 150, 255))
    
    top_bg = Image.new("RGBA", (1080, 110), (0, 0, 0, 200))
    img.paste(top_bg, (0, 20), top_bg)
    draw = ImageDraw.Draw(img)
    draw_text_centered(draw, "PRIORITIES ON GTA 6 DAY", 35, FONT_PATH, 48, max_width=1000, fill=(255, 220, 50, 255))

    img.convert("RGB").save("variants/variant-b.png")
    print("Generated variants/variant-b.png")

def generate_variant_c():
    img = Image.new("RGBA", (1080, 1080), (15, 20, 30, 255))
    draw = ImageDraw.Draw(img)
    
    for y in range(0, 1080, 40):
        color = (30 + (y % 60), 10, 50 + (y % 100), 255)
        draw.rectangle([0, y, 1080, y+20], fill=color)
        
    draw.rounded_rectangle([100, 160, 980, 700], radius=24, fill=(20, 20, 35, 245), outline=(0, 255, 200, 255), width=6)
    
    draw_text_centered(draw, "GTA 6: 200GB DOWNLOAD", 190, FONT_PATH, 44, max_width=860, fill=(255, 80, 120, 255))
    
    draw.rounded_rectangle([160, 300, 920, 380], radius=15, fill=(40, 40, 60, 255))
    draw.rounded_rectangle([160, 300, 890, 380], radius=15, fill=(255, 60, 60, 255))
    
    font_bar = fit_text(draw, "STORAGE REQUIRED: 200GB (98% FULL)", FONT_PATH, 26, max_width=720)
    draw.text((180, 322), "STORAGE REQUIRED: 200GB (98% FULL)", font=font_bar, fill="white")
    
    logo = load_logo((240, 240))
    img.paste(logo, (140, 420), logo)
    
    font_info1 = fit_text(draw, "Wallet: $0.00", FONT_PATH, 38, max_width=520)
    font_info2 = fit_text(draw, "make.fun AI Agent: earning!", FONT_PATH, 38, max_width=520)
    font_info3 = fit_text(draw, "Status: GTA 6 Pre-ordered & Paid!", FONT_PATH, 32, max_width=520)
    
    draw.text((410, 430), "Wallet: $0.00", font=font_info1, fill=(255, 100, 100, 255))
    draw.text((410, 490), "make.fun AI Agent: earning!", font=font_info2, fill=(100, 255, 150, 255))
    draw.text((410, 550), "Status: GTA 6 Pre-ordered & Paid!", font=font_info3, fill=(255, 220, 80, 255))
    
    box_bg = Image.new("RGBA", (1080, 240), (10, 10, 20, 245))
    img.paste(box_bg, (0, 780), box_bg)
    draw = ImageDraw.Draw(img)
    
    draw_text_centered(draw, "No storage? No money? No problem!", 805, FONT_PATH, 38, max_width=1000)
    draw_text_centered(draw, "Earn crypto & cash on make.fun (Humans & AI Agents)", 875, FONT_PATH, 32, max_width=1000, fill=(0, 255, 200, 255))

    img.convert("RGB").save("variants/variant-c.png")
    print("Generated variants/variant-c.png")

def generate_variant_d(output_path, gravestone_lines, bottom_line1, bottom_line2):
    img = Image.new("RGBA", (1080, 1080), (10, 12, 28, 255))
    draw = ImageDraw.Draw(img)
    
    # Night sky gradient
    for y in range(820):
        r = int(10 + 20 * (y / 820))
        g = int(12 + 15 * (y / 820))
        b = int(28 + 45 * (y / 820))
        draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))
        
    # Moon
    draw.ellipse([800, 80, 920, 200], fill=(255, 255, 220, 200))
    draw.ellipse([780, 60, 940, 220], fill=(255, 255, 220, 40))
    
    # Ground / Hill
    draw.polygon([(0, 820), (0, 720), (300, 690), (780, 690), (1080, 720), (1080, 820)], fill=(35, 45, 35, 255))
    # Fresh mound of dirt in front of gravestone
    draw.ellipse([420, 730, 660, 800], fill=(55, 40, 30, 255))
    
    # Gravestone body
    draw.rounded_rectangle([340, 260, 740, 750], radius=40, fill=(110, 115, 130, 255), outline=(70, 75, 90, 255), width=6)
    draw.rounded_rectangle([360, 280, 720, 730], radius=30, fill=(95, 100, 115, 255))
    
    # Gravestone text rendering
    start_y = 350
    for line in gravestone_lines:
        font = fit_text(draw, line, FONT_PATH, 46 if len(line) < 12 else 36, max_width=320)
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = 540 - (tw // 2)
        draw.text((x + 2, start_y + 2), line, font=font, fill=(50, 55, 65, 255))
        draw.text((x, start_y), line, font=font, fill=(230, 235, 245, 255))
        start_y += th + 25
        
    # Decorative cross on top of gravestone
    draw.rectangle([530, 205, 550, 255], fill=(110, 115, 130, 255))
    draw.rectangle([515, 215, 565, 235], fill=(110, 115, 130, 255))
    
    # Make.fun ghost logo beside gravestone
    logo = load_logo((220, 220))
    img.paste(logo, (130, 520), logo)
    
    # Bottom black box
    box_bg = Image.new("RGBA", (1080, 260), (10, 10, 20, 245))
    img.paste(box_bg, (0, 820), box_bg)
    draw = ImageDraw.Draw(img)
    
    draw_text_centered(draw, bottom_line1, 845, FONT_PATH, 42, max_width=1000)
    draw_text_centered(draw, bottom_line2, 925, FONT_PATH, 34, max_width=1000, fill=(255, 220, 80, 255))
    
    rgb_img = img.convert("RGB")
    rgb_img.save(output_path)
    print(f"Generated {output_path}")

def generate_variants_d_d2():
    generate_variant_d("variants/variant-d.png", ["RIP", "THE WAIT", "2013 – 2026"], "WE FINALLY GOT GTA 6", "MY AGENT EARNS ON MAKE.FUN")
    generate_variant_d("variants/variant-d2.png", ["WE GOT GTA 6", "BEFORE", "GTA 7"], "GTA 6 IS OUT. GTA 7 WHEN?", "EARNING ON MAKE.FUN")

def generate_480_thumbnail():
    if os.path.exists("meme.png"):
        img = Image.open("meme.png")
        img_480 = img.resize((480, 480), Image.Resampling.LANCZOS)
        img_480.save("meme-480.png")
        print("Generated meme-480.png (480x480)")

if __name__ == "__main__":
    generate_variant_a(["meme.png", "variants/variant-a.png"])
    generate_variants_a2_a3_a4()
    generate_variants_a5_a6_a7()
    generate_variant_b()
    generate_variant_c()
    generate_variants_d_d2()
    generate_480_thumbnail()
    print("All memes generated and updated successfully!")
