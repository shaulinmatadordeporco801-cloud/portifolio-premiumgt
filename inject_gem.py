import re

fp = r'C:/Users/gabri/Desktop/Antigravity/portfolio-premium/index.html'

new_three_block = '''      /* THREE.JS — SCROLL-DRIVEN GEM */
      var gemCanvas = document.getElementById('gem-canvas');
      var GW = gemCanvas.clientWidth || Math.round(window.innerWidth * 0.48);
      var GH = window.innerHeight;
      var gemRenderer = new THREE.WebGLRenderer({ canvas: gemCanvas, antialias: true, alpha: true });
      gemRenderer.setPixelRatio(Math.min(devicePixelRatio, 2));
      gemRenderer.setSize(GW, GH);
      gemRenderer.toneMapping = THREE.ACESFilmicToneMapping;
      gemRenderer.toneMappingExposure = 1.5;
      gemRenderer.outputEncoding = THREE.sRGBEncoding;

      var gemScene = new THREE.Scene();
      var gemCam = new THREE.PerspectiveCamera(38, GW / GH, 0.1, 100);
      gemCam.position.set(0, 0, 7);

      gemScene.add(new THREE.AmbientLight(0x111111, 1.5));
      var keyL = new THREE.PointLight(0xFF5500, 20, 18);
      keyL.position.set(4, 4, 5);
      gemScene.add(keyL);
      gemScene.add((function(){ var l=new THREE.PointLight(0xFF2000,8,14); l.position.set(-5,-3,2); return l; })());
      gemScene.add((function(){ var l=new THREE.DirectionalLight(0xffeedd,1.2); l.position.set(0,8,-6); return l; })());

      var pmrem2 = new THREE.PMREMGenerator(gemRenderer);
      pmrem2.compileEquirectangularShader();
      var eScene = new THREE.Scene();
      eScene.add((function(){ var l=new THREE.PointLight(0xFF6600,12,20); l.position.set(5,5,5); return l; })());
      eScene.add((function(){ var l=new THREE.PointLight(0x331100,6,14); l.position.set(-5,-3,3); return l; })());
      eScene.add(new THREE.AmbientLight(0x1a0800,3));
      var envMap2 = pmrem2.fromScene(eScene).texture;
      gemScene.environment = envMap2;

      var gemGroup = new THREE.Group();

      /* Main diamond — OctahedronGeometry stretched to gem shape */
      var mainGeo = new THREE.OctahedronGeometry(1.5, 0);
      mainGeo.applyMatrix4(new THREE.Matrix4().makeScale(1, 1.45, 0.85));
      var gemMat = new THREE.MeshPhysicalMaterial({
        color: 0xFF3000, metalness: 0.05, roughness: 0.02,
        transmission: 0.4, transparent: true, thickness: 2.0,
        reflectivity: 1.0, clearcoat: 1.0, clearcoatRoughness: 0.04,
        ior: 2.4, envMap: envMap2, envMapIntensity: 3,
        emissive: 0xFF1000, emissiveIntensity: 0.1,
      });
      gemGroup.add(new THREE.Mesh(mainGeo, gemMat));

      /* Wireframe edge overlay */
      var wireGeo = new THREE.OctahedronGeometry(1.53, 0);
      wireGeo.applyMatrix4(new THREE.Matrix4().makeScale(1, 1.45, 0.85));
      var wireOverlay = new THREE.Mesh(wireGeo,
        new THREE.MeshBasicMaterial({ color: 0xFF6600, wireframe: true, transparent: true, opacity: 0.14 }));
      gemGroup.add(wireOverlay);

      /* Inner shard */
      var innerGeo = new THREE.OctahedronGeometry(0.75, 0);
      innerGeo.applyMatrix4(new THREE.Matrix4().makeScale(0.9, 1.3, 0.8));
      var innerMesh = new THREE.Mesh(innerGeo, new THREE.MeshPhysicalMaterial({
        color: 0xFF4400, metalness: 0.0, roughness: 0.0,
        transmission: 0.65, transparent: true, clearcoat: 1.0, reflectivity: 1.0, ior: 2.2,
        envMap: envMap2, envMapIntensity: 2, emissive: 0xFF2000, emissiveIntensity: 0.16,
      }));
      innerMesh.rotation.y = Math.PI / 4;
      gemGroup.add(innerMesh);

      /* Orbiting ring */
      var ring3d = new THREE.Mesh(
        new THREE.TorusGeometry(2.1, 0.008, 6, 80),
        new THREE.MeshBasicMaterial({ color: 0xFF4400, transparent: true, opacity: 0.3 })
      );
      ring3d.rotation.x = Math.PI / 3;
      gemGroup.add(ring3d);

      /* Particle halo */
      var pCount = 200, pPos = new Float32Array(pCount * 3);
      for (var i = 0; i < pCount; i++) {
        var r = 2.4 + Math.random() * 1.5, th = Math.random() * Math.PI * 2, ph = Math.acos(2 * Math.random() - 1);
        pPos[i*3] = r*Math.sin(ph)*Math.cos(th); pPos[i*3+1] = r*Math.sin(ph)*Math.sin(th); pPos[i*3+2] = r*Math.cos(ph);
      }
      var pGeo = new THREE.BufferGeometry();
      pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
      var particles = new THREE.Points(pGeo, new THREE.PointsMaterial({ color: 0xFF5500, size: 0.024, transparent: true, opacity: 0.45 }));
      gemGroup.add(particles);

      gemScene.add(gemGroup);

      /* Mouse subtle effect */
      var mouseNX2 = 0;
      document.addEventListener('mousemove', function(e) { mouseNX2 = (e.clientX / window.innerWidth - 0.5) * 2; });

      /* Section keyframes: y position + scale when scrolling */
      var gemRotY = 0, curYG = 0, curScaleG = 1, curRXG = 0;
      function getScrollProg() {
        var scrollY = window.scrollY;
        var portTop = document.getElementById('portfolio').offsetTop;
        var ctaTop  = document.getElementById('cta').offsetTop;
        if (scrollY < portTop) return scrollY / portTop * 0.5;
        if (scrollY < ctaTop) return 0.5 + (scrollY - portTop) / (ctaTop - portTop) * 0.5;
        return 1;
      }
      function lrp(a, b, t) { return a + (b - a) * t; }

      var kf = [
        { y:  0.0, sc: 1.0,  rx:  0.0 },  /* 0 = hero */
        { y: -0.9, sc: 0.68, rx:  0.5 },  /* 0.5 = portfolio */
        { y:  0.7, sc: 0.82, rx: -0.3 },  /* 1 = cta */
      ];

      function gemTick() {
        requestAnimationFrame(gemTick);
        var prog = getScrollProg();
        var tNow = performance.now() * 0.001;
        var tY, tSc, tRX;
        if (prog <= 0.5) {
          var p = prog / 0.5;
          tY = lrp(kf[0].y, kf[1].y, p); tSc = lrp(kf[0].sc, kf[1].sc, p); tRX = lrp(kf[0].rx, kf[1].rx, p);
        } else {
          var p = (prog - 0.5) / 0.5;
          tY = lrp(kf[1].y, kf[2].y, p); tSc = lrp(kf[1].sc, kf[2].sc, p); tRX = lrp(kf[1].rx, kf[2].rx, p);
        }
        curYG     += (tY  - curYG)     * 0.05;
        curScaleG += (tSc - curScaleG) * 0.05;
        curRXG    += (tRX - curRXG)    * 0.05;

        gemRotY += 0.005 + mouseNX2 * 0.002;
        gemGroup.position.y = curYG;
        gemGroup.scale.setScalar(curScaleG);
        gemGroup.rotation.x = curRXG + Math.sin(tNow * 0.4) * 0.06;
        gemGroup.rotation.y = gemRotY;
        ring3d.rotation.z  += 0.008;
        particles.rotation.y += 0.001;
        keyL.position.x = Math.sin(tNow) * 5;
        keyL.position.z = Math.cos(tNow) * 4;
        gemRenderer.render(gemScene, gemCam);
      }
      gemTick();

      window.addEventListener('resize', function() {
        var nGW = gemCanvas.clientWidth || Math.round(window.innerWidth * 0.48);
        var nGH = window.innerHeight;
        gemRenderer.setSize(nGW, nGH);
        gemCam.aspect = nGW / nGH;
        gemCam.updateProjectionMatrix();
      });
'''

with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the THREE.JS block
start_marker = "      /* THREE.JS BRUTALIST SCULPTURE */"
end_marker = "      window.addEventListener('resize', function () {\n        var nW = canvas.parentElement.clientWidth || 480;\n        renderer.setSize(nW, H);\n        cam.aspect = nW / H;\n        cam.updateProjectionMatrix();\n      });"

start_idx = content.find(start_marker)
end_idx   = content.find(end_marker)

if start_idx == -1:
    # Try alternate marker (after previous edits)
    start_marker = "      /* THREE.JS — SCROLL-DRIVEN GEM */"
    start_idx = content.find(start_marker)

if start_idx == -1:
    # Find via PMREMGenerator reference (from previous run)
    start_marker = "      /* GEM fallback */"
    start_idx = content.find(start_marker)

# Fallback: find end marker differently
if end_idx == -1:
    end_marker_alt = "      window.addEventListener('resize', function () {"
    end_idx = content.rfind(end_marker_alt, 0, content.find("/* IFRAME SCALE */"))
    if end_idx != -1:
        # find the closing }); of resize
        end_idx = content.find("});", end_idx) + 3

print(f"Start: {start_idx}, End: {end_idx}")

if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
    new_content = content[:start_idx] + new_three_block + "\n" + content[end_idx+1:]
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done! Three.js block replaced.")
else:
    # Direct search by line content
    lines = content.split('\n')
    start_line = -1
    end_line   = -1
    for j, line in enumerate(lines):
        if 'THREE.JS' in line and 'SCULPTURE' in line:
            start_line = j
        if start_line > 0 and 'parentElement.clientWidth || 480' in line:
            # Find closing of this resize block
            for k in range(j, min(j+4, len(lines))):
                if '});' in lines[k]:
                    end_line = k
                    break
            break
    if start_line > 0 and end_line > 0:
        new_lines = lines[:start_line] + [new_three_block] + lines[end_line+1:]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"Done via line method! Lines {start_line}–{end_line} replaced.")
    else:
        print(f"Could not find markers. start_line={start_line}, end_line={end_line}")
