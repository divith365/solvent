<script>
  window.addEventListener('scroll', function() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    document.getElementById('scrollProgress').style.width = progress + '%';
  });

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
</script>

<!-- Interactive Globe using globe.gl -->
<style>
  @keyframes blinkDevice {
    0% { opacity: 0.2; transform: scale(0.6); }
    100% { opacity: 1; transform: scale(1.4); }
  }
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
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
</body>
</html>
