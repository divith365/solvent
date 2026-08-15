import sys

with open('index_static.html', 'r') as f:
    static_lines = f.readlines()

visual_section_lines = static_lines[512:859]

with open('index.html', 'r') as f:
    lines = f.readlines()

insert_idx = -1
for i, line in enumerate(lines):
    if '<!-- ================= TESTIMONIALS' in line:
        insert_idx = i
        break

if insert_idx != -1:
    lines = lines[:insert_idx] + visual_section_lines + lines[insert_idx:]

script_start = -1
script_end = -1
for i, line in enumerate(lines):
    if '<script src="https://unpkg.com/three"></script>' in line:
        script_start = i
    if '</body>' in line and script_start != -1:
        script_end = i
        break

new_script = """<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://unpkg.com/globe.gl"></script>
<script>
  const container = document.getElementById('globe-canvas-container');
  if (container) {
    const globe = Globe({ animateIn: false })
      (container)
      .backgroundColor('rgba(0,0,0,0)')
      .showGlobe(false)
      .showAtmosphere(true)
      .atmosphereColor('#29B6F6')
      .atmosphereAltitude(0.15)
      .hexPolygonResolution(3)
      .hexPolygonMargin(0.4)
      .hexPolygonColor(() => 'rgba(10, 143, 163, 0.7)');

    globe.controls().autoRotate = true;
    globe.controls().autoRotateSpeed = 1.2;
    globe.controls().enableZoom = false;

    const N = 80;
    const colors = ['#25D366', '#29B6F6', '#FF3B30', '#FFCC00', '#A200FF', '#ffffff'];
    const gData = [...Array(N).keys()].map(() => ({
      lat: (Math.random() - 0.5) * 160,
      lng: (Math.random() - 0.5) * 360,
      size: Math.random() * 0.8 + 0.4,
      color: colors[Math.floor(Math.random() * colors.length)],
      duration: Math.random() * 1.5 + 0.5
    }));

    globe.htmlElementsData(gData)
      .htmlElement(d => {
        const el = document.createElement('div');
        el.style.width = `${d.size * 6}px`;
        el.style.height = `${d.size * 6}px`;
        el.style.borderRadius = '50%';
        el.style.backgroundColor = d.color;
        el.style.boxShadow = `0 0 12px ${d.color}, 0 0 4px ${d.color}`;
        el.style.animation = `blinkDevice ${d.duration}s infinite alternate`;
        return el;
      });

    fetch('https://unpkg.com/globe.gl/example/datasets/ne_110m_admin_0_countries.geojson')
      .then(res => res.json())
      .then(countries => {
        globe.hexPolygonsData(countries.features);
      })
      .catch(err => console.error("Globe map loading error:", err));
      
    window.addEventListener('resize', () => {
      globe.width(container.clientWidth);
      globe.height(container.clientHeight);
    });
  }
</script>
"""

if script_start != -1 and script_end != -1:
    lines = lines[:script_start] + [new_script] + lines[script_end:]
    
with open('index.html', 'w') as f:
    f.writelines(lines)
