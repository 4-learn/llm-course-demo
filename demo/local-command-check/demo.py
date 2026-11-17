"""檢查本機命令"""

import shutil

for command in ("docker", "git", "python3"):
    path = shutil.which(command)
    print(f"{command}: {'available' if path else 'not found'}")
