import re

def modify():
    file_path = r'C:/Users/gabri/Desktop/Antigravity/portfolio-premium/index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Left Alignment Tweaks
    content = content.replace("align-items:center;text-align:center;padding:0 3.5rem;\n  position:relative;overflow:hidden;\n  padding-top:90px;",
                              "align-items:flex-start;text-align:left;padding:0 3.5rem;\n  position:relative;overflow:hidden;\n  padding-top:90px;")
    
    content = content.replace(".hero-left{position:relative;z-index:10;max-width:1100px;margin:0 auto;display:flex;flex-direction:column;align-items:center;pointer-events:none;}",
                              ".hero-left{position:relative;z-index:10;max-width:1100px;margin:0;display:flex;flex-direction:column;align-items:flex-start;pointer-events:none;}")
    
    content = content.replace("border-left:none;padding-left:0;text-align:center;",
                              "border-left:none;padding-left:0;text-align:left;")
    
    content = content.replace(".hero-btns{pointer-events:auto;justify-content:center;",
                              ".hero-btns{pointer-events:auto;justify-content:flex-start;")

    # 2. Removing 3D background object HTML
    hero_right_block = """  <div class="hero-right">
    <canvas id="three-canvas"></canvas>
    <div class="canvas-label">// drag to interact</div>
  </div>"""
    content = content.replace(hero_right_block, "")

    # 3. Removing JS script tag for Three.js
    content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n', '')

    # 4. Removing Three.js logic block
    content = re.sub(r'/\* ── THREE.JS — FUTURISTIC TORUS KNOT ── \*/.*?\)\(\);\n', '', content, flags=re.DOTALL)

    # Ensure CTA is also left aligned to match the new dynamic layout
    content = content.replace("#cta{\n  padding:9rem 3.5rem;text-align:center;\n  border-top:1px solid var(--border);position:relative;overflow:hidden;\n}",
                              "#cta{\n  padding:9rem 3.5rem;text-align:left;\n  border-top:1px solid var(--border);position:relative;overflow:hidden;\n}")
    content = content.replace(".cta-pre{\n  font-family:var(--ff-mono);font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;\n  color:var(--cyan);margin-bottom:1.8rem;\n  display:flex;align-items:center;justify-content:center;gap:12px;\n  position:relative;z-index:1;\n}",
                              ".cta-pre{\n  font-family:var(--ff-mono);font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;\n  color:var(--cyan);margin-bottom:1.8rem;\n  display:flex;align-items:center;justify-content:flex-start;gap:12px;\n  position:relative;z-index:1;\n}")
    content = content.replace(".cta-btns{display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;position:relative;z-index:1}",
                              ".cta-btns{display:flex;justify-content:flex-start;gap:1rem;flex-wrap:wrap;position:relative;z-index:1}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    modify()
