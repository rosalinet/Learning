#These notes serve to record notes for the book titled LINUX IN ACTION by DAVID CLINTON

Chapter 1
Key Terms:
open source, distribution (distro), file system, index, partition, terminal, process, BASH, Plain text, File globbing, Tab completion, Pseudo file systems
What it covered:
	1 - What makes Linux different
	2 - Basic survival skills
	3 - Getting help
1. 
- Linux is free, true mulituser OS, and open source.
2.
- Understanding the Linux file system and how the directory tree works.
- Root, Top-level directories: bin, etc, var, home
- What is BASH? Shell -> Operating System Software -> Kernel -> Hardware
- 5 Linux Navigation Must-Have Commands: ls, pwd, cd, cat, and less
common ls flags: h - human-readable format, l - lists files permissions, owners, size, timestamp, et, R - displays subdirectories and the files and subdirectories they contain
- touch command creates files/updates time stamps
- Text-editors: nano, vim, LibreOffice, MS Word, gedit
- rm, rmdir, mkdir, cp, mv, file globbing (* and ?)
- Keyboard Tricks: Tab auto-fill, history, Shift Ctrl C/V
- sudo masking the root user for permissions (password-required)
3.
- man, info (interactive), journalctl (system logs), grep (filter command)
ex: journalctl | grep filename.php | grep error
This prints off system logs including only lines that include the string filename.php, and then those files are also filtered by the filename.php files that contain the string 'error'
You can use the flag -v to invert your results (everything that DOESN'T say error)
- Use the internet for help, someone else has probably encountered your problem


Chapter 2
Key Terms:
virtualization, hypervisor, container, dynamically-allocated, software repository, fixed-size disk
What it covered:
	1 - Finding the right virtualization technology
	2 - Using Linux repository managers
	3 - Building effective environments using VirtualBox
	4 - Building containers with LXC
	5 - How and when to closely manage VMs
1.
- Linux dominates the virtual space; virtualization makes it easier to learn any technology
- 2 Approaches to Virtualization: Hypervisors and Containers
	- Hypervisors control host system hardware to one degree or another, providing each guest OS the resources it needs. 
	- Containers are extremely lightweight virtual servers that, rather than running as full operating systems, share the underlying kernel of their host OS.
- VirtualBox is a type 2 hypervisor, and LXC (The Linux Container) is a container manager.
2.
- Repository/package managers: Advanced Package Tool = apt (Debian/Ubuntu) first: apt update second: apt install <REPO>
- The manager handles local indeces to track repos and their content, track the status of all software located on machine, ensures that all software is updated and has all their necessary dependencies, installs and removes packages.
- If downloading from the website, navigate to the directory that contains the software (usually Downloads), and use the command dpkg -i (install flag). 
- You can check your OS bit (32 or 64) by using the arch command.
- You can search for available packages with apt search, and you can display package info with apt show.
- Use checksum to make sure you have a non-corrupted file. You can find it from where you downloaded it and then compare it to your download by going into the same directory of the download and runing shasum <FILE> and if they match then you're okay. If not, you may need to download the file again.
- Cloning VM's: Full Clone vs Linked Clone
- VBox comes with its own command-line shell invoked by vboxmanage. You can use list vms to see all your VM's or vboxmanage clonevm to create a clone. --register <OG VM> --name <NEWNAME>
3.
- Creating a container: lxc-create -n <NAME> -t <TEMPLATE> Template can be Ubuntu, Windows, etc
- May need to download templates first (sudo apt-get install lxc-templates)
- Ubuntu containers default to ubuntu as the user and password. Change password by using the passwd command. Check for the container with sudo lxc-ls -f.
- To start the container, use lxc-start -d(detach so that you are not dropped into an interactive session where you can only leave by shutting down the container) -n(name) myContainer(MY CONTAINER's NAME)
- To run a root shell session within a running container, use lxc-attach -n (NAMEofCONTAINER)
- In the root shell session you can run commands like ip addr to see what's going on in the container. To leave, just type exit, and you won't shut down the container. If you DO want to shut it down, use shutdown -h(halt) now (if you used the -r(reboot) flag, it would reboot) 
- You can find the main Filesystem Hierarchy Standard (FHS) in the /var/lib/lxc/<YOURCONTAINER> rootfs file. (You can use sudo su to do this in sudo)

