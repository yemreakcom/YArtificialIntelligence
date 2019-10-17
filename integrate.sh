python ../YGitBookIntegration/integrate.py . -ll 1 -l ../YWiki/Yapay\ Zeka/README.md -u https://ai.yemreak.com
echo "---
description: Sitede neler olup bittiğinin raporudur.
---" > CHANGELOG.md
ygitchangelog -d >> CHANGELOG.md
bash github
