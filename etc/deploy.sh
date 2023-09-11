#!/usr/bin/env bash

set -euo pipefail

PROJECT_ROOT=$(git rev-parse --show-toplevel)
PROJECT_NAME=$(basename $PROJECT_ROOT)

printf " --\n"
printf " -- deploying $PROJECT_NAME (from $PROJECT_ROOT)\n"
printf " --\n"
cd "$PROJECT_ROOT/etc"

printf "copying files"

## static files
rsync -az $PROJECT_ROOT/static/ root@164.92.180.216:/var/www/html/volt-watch/
printf ".\n"

## service recomposition
printf " --\n"
printf " -- reloading services\n"
printf " --\n"

ssh root@164.92.180.216 /bin/bash <<'EOT'
set -euo pipefail

chown django:www-data /var/www/html/volt-watch

systemctl daemon-reload
systemctl restart gunicorn
systemctl reload nginx

printf " done\n"
EOT
