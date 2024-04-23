#!/bin/sh
ssh-keygen -A

su -s /bin/sh -c 'ssh-keygen -t rsa -C "$HOSTNAME" -f "$HOME/.ssh/id_rsa" -P "" && cat ~/.ssh/id_rsa.pub' user

exec /usr/sbin/sshd -D -e "$@"