python ../YGitBookIntegration/integrate.py .
echo "---
description: Sitede neler olup bittiğinin raporudur.
---
" > CHANGELOG.md

ygitchangelog.exe >> CHANGELOG.md
bash github .
