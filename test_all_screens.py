import subprocess, json, time

# Start server on a different port
import http.server, socketserver, threading, os
os.chdir('/home/ubuntu/Brandpilot-AI')
port = 9095
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", port), handler)
thread = threading.Thread(target=httpd.serve_forever, daemon=True)
thread.start()
print(f"Server running on port {port}")

# Give server time to start
time.sleep(1)

# Use Python to fetch the page and check if data-i18n attributes are present
import requests
resp = requests.get(f'http://localhost:{port}/index.html')
html = resp.text

# Check for data-i18n on key elements
checks = {
    'heroTitle': 'data-i18n="heroTitle"' in html,
    'inputHint': 'data-i18n="inputHint"' in html,
    'assumptionText': 'data-i18n="assumptionText"' in html,
    'reflectionPromptText': 'data-i18n="reflectionPromptText"' in html,
    'buyerQuestion': 'data-i18n="buyerQuestion"' in html,
    'buyerPrompt': 'data-i18n="buyerPrompt"' in html,
    'roadmapTitle': 'data-i18n="roadmapTitle"' in html,
    'reflectionQ2': 'data-i18n="reflectionQ2"' in html,
    'buyerAnswerPlaceholder': 'data-i18n-placeholder="buyerAnswerPlaceholder"' in html,
    'reflectionPlaceholder': 'data-i18n-placeholder="reflectionPlaceholder"' in html,
}

print("\n=== data-i18n attribute check ===")
for key, found in checks.items():
    status = "✅" if found else "❌"
    print(f"{status} {key}")

# Count total data-i18n attributes
import re
i18n_attrs = re.findall(r'data-i18n="([^"]+)"', html)
placeholder_attrs = re.findall(r'data-i18n-placeholder="([^"]+)"', html)
print(f"\nTotal data-i18n attributes: {len(i18n_attrs)}")
print(f"Total data-i18n-placeholder attributes: {len(placeholder_attrs)}")

httpd.shutdown()
print("\nDone")
