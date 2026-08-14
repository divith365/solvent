import re

sections = [
    ("What We Build", "IT Infrastructure Foundation", [
        ("Clean Cabling", "Neat, labeled cabling for zero clutter and maximum reliability."),
        ("Fast Switching", "Right-sized switches built for high-speed connectivity."),
        ("Strong Servers", "Powerful servers built to handle your critical workloads."),
        ("Safe Storage", "Centralized backup storage you can trust."),
        ("Power Backup", "UPS and power backup that keeps your business running."),
        ("Speed Tuned", "Optimized network and systems for real performance."),
        ("Quick On-Site Help", "On-site support with ready maps, docs and diagnostics."),
        ("Always Connected", "Multi-WAN failover keeps your internet always on.")
    ]),
    ("What We Deliver", "Complete Networking Made Simple", [
        ("Always-On Internet", "24/7 leased line internet for reliable connectivity"),
        ("Wi-Fi Everywhere", "Seamless office-wide Wi-Fi coverage"),
        ("Secure Gateway", "Enterprise firewall protection and secure gateway"),
        ("OfficeLink Network", "Secure WAN link connecting multiple offices"),
        ("TeamVPN Access", "Secure VPN connection for remote teams"),
        ("Fair Speed For All", "Bandwidth management ensures fair balanced speed"),
        ("Central File Hub", "Central NAS server for secure file storage"),
        ("Live Network View", "Real-time network monitoring and map-based status view"),
        ("Care and Support", "AMC and on-site support technician services"),
        ("Future-Ready Design", "Scalable network designed for future growth")
    ]),
    ("Enterprise Wireless", "Fast, Secure Wi-Fi Everywhere", [
        ("Full Coverage", "No dead zones in your workplace with complete coverage"),
        ("Guest Wi-Fi", "Separate safe access for visitors and guests"),
        ("Fast Roaming", "Move freely without dropping connection"),
        ("User Control", "Decide who can access what on your network"),
        ("High Density Ready", "Handles hundreds of users at once without lag"),
        ("Secure Login", "Encrypted and password-protected access"),
        ("Fair Speed", "Bandwidth control ensures fair speed for everyone"),
        ("Outdoor Coverage", "Extends Wi-Fi to parking areas and yards"),
        ("One Dashboard", "Manage all access points from one central place"),
        ("Health Check", "Continuous signal monitoring and uptime tracking")
    ]),
    ("What We Protect", "Endpoint Security Made Simple", [
        ("Virus Shield", "Real-time protection that blocks viruses instantly"),
        ("Device Control", "Controls USB and external device access securely"),
        ("Web Protection", "Blocks malicious links and phishing websites"),
        ("Ransomware Guard", "Stops encryption attacks before they cause damage"),
        ("Safe Files", "Scans downloads and attachments automatically"),
        ("App Safety", "Prevents risky applications from running"),
        ("Data Lock", "Keeps sensitive files encrypted and protected"),
        ("Lost Device Protection", "Locks or wipes data remotely if lost"),
        ("Patch Updates", "Keeps your systems up to date automatically"),
        ("Device Monitoring", "Continuous monitoring of all endpoints 24/7"),
        ("Performance Check", "Monitors system health and performance"),
        ("Threat Monitoring", "Detects and blocks threats in real-time")
    ]),
    ("Firewall & Network Security", "Keep Your Business Safe Online", [
        ("Digital Gatekeeper", "Controls inbound and outbound traffic to block unwanted access"),
        ("Safe Browsing", "Filters harmful sites and malicious links automatically"),
        ("Threat Alerts", "Instant alerts for phishing, malware and scam attempts"),
        ("Watch for Intruders", "Monitor and detect suspicious activity 24/7"),
        ("Fair Internet Speed", "Bandwidth control for fair, consistent speed across all devices"),
        ("Lock Your Website", "SSL security and HTTPS to secure your websites"),
        ("Always Connected", "Multi-WAN failover keeps your internet running reliably"),
        ("Secure Remote Work", "VPN connection to keep remote work safe and private"),
        ("Health Check", "Continuous monitoring to keep your network healthy and performing")
    ]),
    ("How We Connect", "Connect Securely From Anywhere", [
        ("Encrypted Tunnel", "Your data travels through a private secure path."),
        ("Remote Office Access", "Work as if you are in the office."),
        ("Cloud Safe Connect", "Secure access to AWS, Azure and Google Cloud."),
        ("Site-to-Site Link", "Connects branches together securely."),
        ("Multi-Device VPN", "Works on laptop, mobile and tablet."),
        ("No Snoop Shield", "Hides your activity from hackers and trackers."),
        ("Always-On Protection", "VPN connects automatically for protection."),
        ("Fast and Stable", "Optimized speed for video calls and files."),
        ("Access Control", "Only authorized users can enter."),
        ("VPN Monitoring", "Continuous tracking of uptime and security.")
    ])
]

html_parts = []
html_parts.append('<div class="visual-text-solutions" style="padding-top: 40px;">')

for title, subtitle, items in sections:
    html_parts.append(f'''
    <div class="build-section reveal reveal-stagger" style="margin-top: 60px;">
      <h3 style="text-align: center; color: var(--navy); margin-bottom: 8px; font-size: 2rem; text-transform: uppercase;">{title}</h3>
      <p style="text-align: center; color: var(--cyan); margin-bottom: 32px; font-weight: 600; font-size: 1.1rem; letter-spacing: 1px;">{subtitle}</p>
      <div class="text-cards-grid">''')
      
    for heading, desc in items:
        html_parts.append(f'''
        <div class="text-card">
          <h4>{heading}</h4>
          <p>{desc}</p>
        </div>''')
        
    html_parts.append('      </div>\n    </div>')
    
html_parts.append('</div>')

new_html = '\n'.join(html_parts)

css_addition = """
  .text-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-bottom: 40px;
  }
  .text-card {
    background: #ffffff;
    padding: 30px 24px;
    border-radius: 16px;
    box-shadow: 0 4px 16px rgba(11, 42, 107, 0.04);
    border: 1px solid rgba(11, 42, 107, 0.06);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .text-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 40px rgba(11, 42, 107, 0.12);
  }
  .text-card h4 {
    color: var(--navy);
    font-family: 'Montserrat', sans-serif;
    font-size: 1.2rem;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .text-card h4::before {
    content: '✓';
    color: var(--cyan);
    font-weight: 900;
    font-size: 1.4rem;
    background: rgba(41, 182, 246, 0.1);
    border-radius: 50%;
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .text-card p {
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.6;
    margin: 0;
  }
"""

with open('index.html', 'r') as f:
    content = f.read()

# Replace visual-grid
start_marker = '<div class="visual-grid"'
end_marker = '<!-- ================= TESTIMONIALS'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

content = content[:start_idx] + new_html + '\n\n  ' + content[end_idx:]

# Inject CSS
css_marker = '/* ================= TESTIMONIALS'
css_idx = content.find(css_marker)

content = content[:css_idx] + css_addition + '\n  ' + content[css_idx:]

with open('index.html', 'w') as f:
    f.write(content)
