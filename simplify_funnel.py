import re

def simplify():
    file_path = r'C:/Users/gabri/Desktop/Antigravity/portfolio-premium/index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove unnecessary sections
    content = re.sub(r'<!-- MARQUEE -->.*?<!-- NUMBERS -->', '<!-- NUMBERS -->', content, flags=re.DOTALL)
    content = re.sub(r'<!-- NUMBERS -->.*?<!-- ABOUT -->', '<!-- ABOUT -->', content, flags=re.DOTALL)
    content = re.sub(r'<!-- ABOUT -->.*?<!-- PORTFOLIO -->', '<!-- PORTFOLIO -->', content, flags=re.DOTALL)
    content = re.sub(r'<!-- TESTIMONIAL -->.*?<!-- PROCESS -->', '<!-- PROCESS -->', content, flags=re.DOTALL)
    content = re.sub(r'<!-- PROCESS -->.*?<!-- CTA -->', '<!-- CTA -->', content, flags=re.DOTALL)

    # 2. Update Nav Links
    nav_links_new = """  <ul class="nav-links">
    <li><a href="#portfolio">Projetos</a></li>
    <li><a href="#cta">Contato</a></li>
  </ul>"""
    content = re.sub(r'<ul class="nav-links">.*?</ul>', nav_links_new, content, flags=re.DOTALL)
    
    foot_nav_new = """  <ul class="foot-nav">
    <li><a href="#portfolio">Projetos</a></li>
    <li><a href="#cta">Contato</a></li>
  </ul>"""
    content = re.sub(r'<ul class="foot-nav">.*?</ul>', foot_nav_new, content, flags=re.DOTALL)

    # 3. Simplify Hero CTAs to a single funnel
    old_hero_btns = """<div class="hero-btns">
      <button class="btn-primary" id="btn-hero-portfolio">Ver projetos</button>
      <button class="btn-secondary" id="btn-hero-cta">Orçamento grátis</button>
    </div>"""
    new_hero_btns = """<div class="hero-btns" style="pointer-events:auto;justify-content:center;">
      <button class="btn-primary" id="btn-hero-wapp" style="padding: 1.2rem 3rem; font-size: 0.9rem;">Iniciar Projeto 🔥</button>
    </div>"""
    content = content.replace(old_hero_btns, new_hero_btns)
    
    # If the previous regex didn't work because styles were injected:
    content = re.sub(r'<div class="hero-btns".*?>.*?</div>', new_hero_btns, content, flags=re.DOTALL)

    # 4. Simplify Bottom CTA to a single focused pipeline
    old_cta_btns = r'<div class="cta-btns.*?</div>'
    new_cta_btns = """<div class="cta-btns rev d3">
    <button class="btn-primary" id="btn-cta-wapp" style="padding: 1.2rem 3rem; font-size: 0.9rem;">Agendar no WhatsApp →</button>
  </div>"""
    content = re.sub(old_cta_btns, new_cta_btns, content, flags=re.DOTALL)
    
    # 5. Fix Javascript bindings
    js_listener_new = """
/* ── SECURITY EVENT LISTENERS ── */
document.getElementById('nav-cta')?.addEventListener('click', () => window.open('https://wa.me/5519989776905', '_blank', 'noopener,noreferrer'));
document.getElementById('btn-hero-wapp')?.addEventListener('click', () => window.open('https://wa.me/5519989776905', '_blank', 'noopener,noreferrer'));
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
    content = re.sub(r'/\* ── SECURITY EVENT LISTENERS ── \*/.*?</script>\n</body>', js_listener_new, content, flags=re.DOTALL)

    # Save
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    simplify()
