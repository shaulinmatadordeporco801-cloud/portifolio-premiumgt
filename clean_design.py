import re
import os

def clean_design():
    file_path = r'C:/Users/gabri/Desktop/Antigravity/portfolio-premium/index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Colors & Palette ---
    
    # Change core CSS variables
    content = content.replace('--bg:      #050810;', '--bg:      #000000;')
    content = content.replace('--surface: #0D1225;', '--surface: #0A0A0A;')
    content = content.replace('--surface2:#111827;', '--surface2:#141414;')
    
    content = content.replace('--cyan:    #00F0FF;', '--cyan:    #FF5E00; /* Orange */')
    content = content.replace('--purple:  #CCFF00; /* Acid Green */', '--purple:  #FF2A00; /* Deep Orange */')
    content = content.replace('--magenta: #FF4400; /* Signal Orange */', '--magenta: #FF9900; /* Light Orange */')
    
    # Text colors to be cleaner
    content = content.replace('--text:    #E8F4FF;', '--text:    #FFFFFF;')
    content = content.replace('--muted:   #4A5980;', '--muted:   #888888;')

    # Replace hardcoded RGBA
    # Old Cyan (0,240,255) -> Orange (255,94,0)
    content = content.replace('rgba(0,240,255', 'rgba(255,94,0')
    # Old Acid Green (204,255,0) -> Deep Orange (255,42,0)
    content = content.replace('rgba(204,255,0', 'rgba(255,42,0')
    # Old Signal Orange (255,68,0) -> Light Orange (255,153,0)
    content = content.replace('rgba(255,68,0', 'rgba(255,153,0')

    # Replace hardcoded hex in ThreeJS
    content = content.replace('0x00F0FF', '0xFF5E00') # Light 1 / Wireframe
    content = content.replace('0xCCFF00', '0xFF2A00') # Light 2
    content = content.replace('0xFF4400', '0xFF9900') # Light 3
    # Mute the ThreeJS background light
    content = content.replace('0x0a1020', '0x050505')

    # --- 2. Clean Design (Removing noisy overlays) ---
    # Remove the repeating-linear-gradient scanline for a cleaner look
    content = re.sub(r'body::after{.*?}', 'body::after{display:none;}', content, flags=re.DOTALL)
    
    # Grid lines bg on hero -> cleaner, subtler
    content = content.replace('linear-gradient(rgba(255,94,0,.04) 1px,transparent 1px)', 'linear-gradient(rgba(255,255,255,.01) 1px,transparent 1px)')
    content = content.replace('linear-gradient(90deg,rgba(255,94,0,.04) 1px,transparent 1px)', 'linear-gradient(90deg,rgba(255,255,255,.01) 1px,transparent 1px)')

    # --- 3. Gradients requested by user ---
    # Text gradients on Headers (.hero-h1 .cyan, .about-h2 .cyan)
    old_h1_cyan = """.hero-h1 .cyan{
  color:var(--cyan);
  text-shadow:0 0 30px rgba(255,94,0,.6),0 0 60px rgba(255,94,0,.2);
}"""
    new_h1_cyan = """.hero-h1 .cyan{
  background: linear-gradient(135deg, var(--cyan), var(--purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: var(--cyan);
  text-shadow: none; /* Cleaner, no noisy glow */
}"""
    content = content.replace(old_h1_cyan, new_h1_cyan)
    
    old_cta_h = """.cta-h .cyan{
  color:var(--cyan);
  text-shadow:0 0 40px rgba(255,94,0,.5),0 0 80px rgba(255,94,0,.15);
}"""
    new_cta_h = """.cta-h .cyan{
  background: linear-gradient(135deg, #FF5E00, #FF9900);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none;
}"""
    content = content.replace(old_cta_h, new_cta_h)
    
    old_cta_purple = """.cta-h .purple{
  color:var(--purple);
  text-shadow:0 0 40px rgba(255,42,0,.5),0 0 80px rgba(255,42,0,.15);
}"""
    new_cta_purple = """.cta-h .purple{
  color: var(--text);
  text-shadow: none;
}"""
    content = content.replace(old_cta_purple, new_cta_purple)

    # Change Buttons to sleek gradients
    old_btn_primary = """.btn-primary{
  font-family:var(--ff-mono);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;
  background:var(--cyan);color:var(--bg);
  border:none;padding:.9rem 2rem;
  border-radius:2px;cursor:none;font-weight:700;
  clip-path:polygon(10px 0%,100% 0%,calc(100% - 10px) 100%,0% 100%);
  transition:box-shadow .25s,transform .2s;
}"""
    new_btn_primary = """.btn-primary{
  font-family:var(--ff-mono);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;
  background: linear-gradient(90deg, var(--cyan), var(--purple));
  color:var(--bg);
  border:none;padding:.9rem 2rem;
  border-radius:2px;cursor:none;font-weight:700;
  clip-path:polygon(10px 0%,100% 0%,calc(100% - 10px) 100%,0% 100%);
  transition:box-shadow .25s,transform .2s;
}"""
    content = content.replace(old_btn_primary, new_btn_primary)

    # Make cursor ring match gradient or clean orange
    content = content.replace('border-color:var(--cyan);box-shadow:0 0 16px rgba(255,94,0,.3);', 
                              'border-color:var(--cyan);box-shadow:none;')
    
    # Save back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    clean_design()
