import re
import os

def update_portfolio():
    src_path = r'C:/Users/gabri/Downloads/portfolio-premium.html'
    dest_path = r'C:/Users/gabri/Desktop/Antigravity/portfolio-premium/index.html'
    
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Security Meta Tags
    meta_tags = """<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests; frame-ancestors 'none'; object-src 'none'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com;">
<meta name="referrer" content="no-referrer">"""
    content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', meta_tags)

    # 2. Fix Palette (Brutalist Acid Green/Signal Orange)
    content = content.replace('--purple:  #7B2FFF;', '--purple:  #CCFF00; /* Acid Green */')
    content = content.replace('--magenta: #FF2D78;', '--magenta: #FF4400; /* Signal Orange */')
    content = content.replace('rgba(123,47,255', 'rgba(204,255,0')
    content = content.replace('0x7B2FFF', '0xCCFF00')
    content = content.replace('0xFF2D78', '0xFF4400')
    content = content.replace('rgba(255,45,120', 'rgba(255,68,0')

    # 3. Change Hero CSS to Massive Typographic Hero Layout
    old_hero = """#hero{
  min-height:100vh;
  display:grid;grid-template-columns:1fr 1fr;
  align-items:center;padding:0 3.5rem;
  gap:0;position:relative;overflow:hidden;
  padding-top:90px;
}"""
    new_hero = """#hero{
  min-height:100vh;
  display:flex;flex-direction:column;justify-content:center;
  align-items:center;text-align:center;padding:0 3.5rem;
  position:relative;overflow:hidden;
  padding-top:90px;
}"""
    content = content.replace(old_hero, new_hero)
    
    content = content.replace('.hero-left{position:relative;z-index:1;padding-right:2rem}', 
                              '.hero-left{position:relative;z-index:10;max-width:1100px;margin:0 auto;display:flex;flex-direction:column;align-items:center;pointer-events:none;}')
    
    content = content.replace('border-left:2px solid rgba(0,240,255,.3);padding-left:1.2rem;', 'border-left:none;padding-left:0;text-align:center;')
    
    content = content.replace('font-size:clamp(3.5rem,6vw,6.5rem);', 'font-size:clamp(4.5rem,10vw,11.5rem); letter-spacing:-0.03em;')

    old_right = """.hero-right{
  position:relative;z-index:1;height:620px;
  display:flex;align-items:center;justify-content:center;
}"""
    new_right = """.hero-right{
  position:absolute;inset:0;z-index:1;
  display:flex;align-items:center;justify-content:center;
  opacity:0.8;
}"""
    content = content.replace(old_right, new_right)
    content = content.replace('.hero-btns{', '.hero-btns{pointer-events:auto;justify-content:center;')
    
    # Process Grid styling changes (Staggered layout instead of safe grids)
    content = content.replace('.proc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(0,240,255,.06);border:1px solid rgba(0,240,255,.06);margin-top:3.5rem}',
                              '.proc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:3.5rem}')
                              
    content = content.replace('.proc-step{', '.proc-step{border-left:1px solid var(--border);\n').replace('.proc-step:hover{', '.proc-step:nth-child(even) { margin-top: 4rem; }\n.proc-step:hover{')
    content = content.replace('height:2px;\n  background:linear-gradient(90deg,var(--purple),var(--cyan));\n  transform:scaleX(0);transition:transform .4s ease;transform-origin:left;',
                              'top:0;bottom:0;width:2px;background:linear-gradient(to bottom,var(--purple),var(--cyan));transform:scaleY(0);transition:transform .4s ease;transform-origin:top;')
    content = content.replace('transform:scaleX(1)', 'transform:scaleY(1)')

    # 4. Iframes Security sandbox
    content = re.sub(r'<iframe(.*?)>', r'<iframe\1 sandbox="allow-scripts allow-same-origin" referrerpolicy="no-referrer">', content)
    
    # 5. Extract onclicks
    content = content.replace('class="nav-cta" onclick="window.open(\'https://wa.me/5519989776905\')"', 'class="nav-cta" id="nav-cta"')
    content = content.replace('class="btn-primary" onclick="document.getElementById(\'portfolio\').scrollIntoView({behavior:\'smooth\'})"', 'class="btn-primary" id="btn-hero-portfolio"')
    content = content.replace('class="btn-secondary" onclick="document.getElementById(\'cta\').scrollIntoView({behavior:\'smooth\'})"', 'class="btn-secondary" id="btn-hero-cta"')
    
    content = content.replace('class="proj proj-a rev" onclick="window.open(\'https://doce-supremo.vercel.app/\',\'_blank\')"', 'class="proj proj-a rev proj-link-wrapper" data-href="https://doce-supremo.vercel.app/"')
    content = content.replace('class="proj proj-b rev d1" onclick="window.open(\'https://code-store-nine.vercel.app/\',\'_blank\')"', 'class="proj proj-b rev d1 proj-link-wrapper" data-href="https://code-store-nine.vercel.app/"')
    content = content.replace('class="proj proj-c rev d2" onclick="window.open(\'https://modelos-cardapio.vercel.app/\',\'_blank\')"', 'class="proj proj-c rev d2 proj-link-wrapper" data-href="https://modelos-cardapio.vercel.app/"')
    content = content.replace('class="proj proj-d rev" onclick="window.open(\'https://barbearia-carlim-cortes.vercel.app/\',\'_blank\')"', 'class="proj proj-d rev proj-link-wrapper" data-href="https://barbearia-carlim-cortes.vercel.app/"')
    
    content = content.replace('class="btn-mag" onclick="window.location.href=\'mailto:gabrieltimoteooficial8@gmail.com\'"', 'class="btn-mag" id="btn-cta-email"')
    content = content.replace('class="btn-cyan" onclick="window.open(\'https://wa.me/5519989776905\')"', 'class="btn-cyan" id="btn-cta-wapp"')
    
    # Inject JS for onclicks at the end
    js_inject = """
/* ── SECURITY EVENT LISTENERS ── */
document.getElementById('nav-cta')?.addEventListener('click', () => window.open('https://wa.me/5519989776905', '_blank', 'noopener,noreferrer'));
document.getElementById('btn-hero-portfolio')?.addEventListener('click', () => document.getElementById('portfolio').scrollIntoView({behavior:'smooth'}));
document.getElementById('btn-hero-cta')?.addEventListener('click', () => document.getElementById('cta').scrollIntoView({behavior:'smooth'}));
document.getElementById('btn-cta-email')?.addEventListener('click', () => window.location.href='mailto:gabrieltimoteooficial8@gmail.com');
document.getElementById('btn-cta-wapp')?.addEventListener('click', () => window.open('https://wa.me/5519989776905', '_blank', 'noopener,noreferrer'));
document.querySelectorAll('.proj-link-wrapper').forEach(el => {
    el.style.cursor = 'none'; 
    el.addEventListener('click', () => {
        const url = el.getAttribute('data-href');
        if(url) window.open(url, '_blank', 'noopener,noreferrer');
    });
});
</script>
</body>"""
    content = content.replace('</script>\n</body>', js_inject)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
if __name__ == "__main__":
    update_portfolio()
