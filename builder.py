import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Barebone Builder")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="build",command=self.run_kernel )
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="cpio", command=self.build_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="open", command=self.copy_file)
        self.copy_button.pack(pady=5)

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):#filename = tk.filedialog.askdirectory(title="Select folder to build")
        self.text_area.delete(1.0, tk.END)
        f1=open("f1","w")
        
        f1.close()
        self.execute_command("cd /tmp/isos ; find . | cpio --quiet -H newc -o | gzip -9 -n > /tmp/initrd.img",False)
        
    def run_kernel(self):
        f1=open("f1","w")
        
        f1.close()
        self.text_area.delete(1.0, tk.END)
        self.execute_command("mkdir /tmp/isos",False)
        self.execute_command("chmod 777 /tmp/isos",False)
        self.execute_command('mkdir /tmp/isos/bin',True)
        self.execute_command('mkdir /tmp/isos/sys',True)
        self.execute_command('mkdir /tmp/isos/usr',True)
        self.execute_command('mkdir /tmp/isos/usr/bin',True)
        self.execute_command('mkdir /tmp/isos/proc',True)
        self.execute_command('mkdir /tmp/isos/tmp',True)
        self.execute_command('mkdir /tmp/isos/dev',True)
        
        
        self.execute_command('cp ./linuxrc /tmp/isos',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/stdio',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/stdout',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/stdin',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/tty2',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/tty1',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/console',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/zero',True)
        self.execute_command('cp ./f1 /tmp/isos/dev/null',True)
        self.execute_command('cp /usr/bin/bash /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/sh /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/echo /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/mount /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/printf /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/cp /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/mkdir /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/ls /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/cat /tmp/isos/bin',True)
        self.execute_command('cp /usr/bin/ps /tmp/isos/bin',True)
        self.execute_command('cp /tmp/isos/bin/* /tmp/isos/usr/bin',True)
       
        


    def copy_file(self):
        self.text_area.delete(1.0, tk.END)
        
        if 0==0:
            self.execute_command("nautilus --browser /tmp/isos",False)
            


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
