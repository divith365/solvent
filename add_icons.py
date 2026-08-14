import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add FontAwesome CDN
fa_link = '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>'
content = content.replace('</head>', fa_link)

# 2. Update CSS: Remove the ::before block and add styling for <i>
old_css = """  .text-card h4::before {
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
  }"""
new_css = """  .text-card h4 i {
    color: var(--cyan);
    background: rgba(41, 182, 246, 0.1);
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
  }"""
content = content.replace(old_css, new_css)

# 3. Map headings to icons
icon_map = {
    # Build
    "Clean Cabling": "fa-network-wired",
    "Fast Switching": "fa-server",
    "Strong Servers": "fa-database",
    "Safe Storage": "fa-hard-drive",
    "Power Backup": "fa-plug",
    "Speed Tuned": "fa-gauge-high",
    "Quick On-Site Help": "fa-wrench",
    "Always Connected": "fa-wifi",
    
    # Deliver
    "Always-On Internet": "fa-globe",
    "Wi-Fi Everywhere": "fa-wifi",
    "Secure Gateway": "fa-shield-halved",
    "OfficeLink Network": "fa-building",
    "TeamVPN Access": "fa-user-shield",
    "Fair Speed For All": "fa-scale-balanced",
    "Central File Hub": "fa-folder-tree",
    "Live Network View": "fa-desktop",
    "Care and Support": "fa-headset",
    "Future-Ready Design": "fa-layer-group",
    
    # Wireless
    "Full Coverage": "fa-tower-broadcast",
    "Guest Wi-Fi": "fa-users",
    "Fast Roaming": "fa-person-running",
    "User Control": "fa-sliders",
    "High Density Ready": "fa-people-group",
    "Secure Login": "fa-lock",
    "Fair Speed": "fa-gauge",
    "Outdoor Coverage": "fa-tree",
    "One Dashboard": "fa-chart-pie",
    "Health Check": "fa-heart-pulse",
    
    # Protect
    "Virus Shield": "fa-shield-virus",
    "Device Control": "fa-usb",
    "Web Protection": "fa-earth-americas",
    "Ransomware Guard": "fa-file-shield",
    "Safe Files": "fa-file-circle-check",
    "App Safety": "fa-box-archive",
    "Data Lock": "fa-lock",
    "Lost Device Protection": "fa-mobile-screen-button",
    "Patch Updates": "fa-download",
    "Device Monitoring": "fa-eye",
    "Performance Check": "fa-chart-line",
    "Threat Monitoring": "fa-radar",
    
    # Firewall
    "Digital Gatekeeper": "fa-door-closed",
    "Safe Browsing": "fa-compass",
    "Threat Alerts": "fa-bell",
    "Watch for Intruders": "fa-binoculars",
    "Fair Internet Speed": "fa-gauge",
    "Lock Your Website": "fa-globe",
    "Secure Remote Work": "fa-laptop-house",
    
    # Connect
    "Encrypted Tunnel": "fa-tunnel-water",
    "Remote Office Access": "fa-briefcase",
    "Cloud Safe Connect": "fa-cloud",
    "Site-to-Site Link": "fa-link",
    "Multi-Device VPN": "fa-mobile",
    "No Snoop Shield": "fa-user-secret",
    "Always-On Protection": "fa-shield",
    "Fast and Stable": "fa-bolt",
    "Access Control": "fa-id-badge",
    "VPN Monitoring": "fa-display"
}

# Add default icon for any unmapped items
def get_icon(match):
    heading = match.group(1)
    icon_class = icon_map.get(heading, "fa-check-circle")
    return f'<h4><i class="fa-solid {icon_class}"></i> {heading}</h4>'

content = re.sub(r'<h4>(.*?)</h4>', get_icon, content)

with open('index.html', 'w') as f:
    f.write(content)
