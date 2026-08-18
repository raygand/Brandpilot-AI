# Let me check if there's a CSS issue - maybe the lang buttons are overlapped by another element
# Or check if there's a z-index issue
# Actually, let me just look at the git diff to see what changed recently
import subprocess
result = subprocess.run(['git', 'diff', 'HEAD~1', '--name-only'], capture_output=True, text=True)
print(result.stdout)
