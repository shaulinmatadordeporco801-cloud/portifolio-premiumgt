import re

def reduce_visuals():
    file_path = r'C:/Users/gabri/Desktop/Antigravity/portfolio-premium/index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Smaller fonts
    content = re.sub(r'font-size:\s*clamp\(4\.5rem,\s*10vw,\s*11\.5rem\);', 'font-size: clamp(3rem, 6vw, 5.5rem);', content)
    content = re.sub(r'font-size:\s*clamp\(3rem,\s*8vw,\s*7\.5rem\);', 'font-size: clamp(2rem, 5vw, 4.5rem);', content)
    content = re.sub(r'font-size:\s*clamp\(2\.2rem,\s*4vw,\s*3\.6rem\);', 'font-size: clamp(1.8rem, 3.5vw, 2.5rem);', content)
    
    # 2. Less visual pollution (Remove grids and glows completely)
    content = re.sub(r'#hero::before\s*\{[^}]+\}', '#hero::before { display: none; }', content, flags=re.DOTALL)
    content = re.sub(r'#hero::after\s*\{[^}]+\}', '#hero::after { display: none; }', content, flags=re.DOTALL)
    content = re.sub(r'#cta::before\s*\{[^}]+\}', '#cta::before { display: none; }', content, flags=re.DOTALL)
    content = re.sub(r'#cta::after\s*\{[^}]+\}', '#cta::after { display: none; }', content, flags=re.DOTALL)
    
    # Remove text-shadow if it exists to be cleaner
    content = re.sub(r'text-shadow:\s*0\s*0\s*10px[^;]+;', 'text-shadow: none;', content)
    
    # Remove project corner brackets purely for cleaner UI
    content = re.sub(r'\.proj::before,\s*\.proj::after\s*\{[^}]+\}', '.proj::before, .proj::after { display: none; }', content, flags=re.DOTALL)
    
    # Clean up the projects grid container for more breathing room
    content = re.sub(r'background:\s*rgba\(255,\s*94,\s*0,\s*\.06\);', 'background: transparent;', content)
    content = re.sub(r'border:\s*1px\s*solid\s*rgba\(255,\s*94,\s*0,\s*\.06\);', 'border: none;', content)
    content = re.sub(r'(\.proj-grid\s*\{[^}]*gap:\s*)[^\s;]+', r'\1 3.5rem', content)
    
    # 3. More distance
    # #portfolio
    content = re.sub(r'(#portfolio\s*\{[^}]*padding:\s*)(.*?);', r'\1 12rem 3.5rem;', content)
    # #cta
    content = re.sub(r'(#cta\s*\{[^}]*padding:\s*)(.*?);', r'\1 14rem 3.5rem;', content)
    # #hero pt
    content = re.sub(r'padding-top:\s*90px;', 'padding-top: 140px;', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    reduce_visuals()
