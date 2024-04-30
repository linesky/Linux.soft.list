printf "\x1bc\x1b[43;37m"
apt-cache search "$1" | grep "$1"
