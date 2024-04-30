printf "\x1bc\x1b[43;37m give me a .c file to compile ? "
read ai
nasm -o /tmp/boot.bin boot.asm
cp -f "$ai" /tmp/kernel.bas
fbc -c /tmp/kernel.bas 
ld -T link.ld /tmp/kernel.o -o /tmp/hello.com -nostdlib
objcopy -O binary  /tmp/hello.com  /tmp/hellos.com
dd if=/tmp/hellos.com of=/tmp/boot.bin seek=1 conv=notrunc
cp -f /tmp/boot.bin ./
/usr/bin/qemu-system-x86_64 -boot c -hda boot.bin
