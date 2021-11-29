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
- Root, Top-level directories, etc, var, home
- What is BASH? Shell -> Operating System Software -> Kernel -> Hardware
- 5 Linux Navigation Must-Have Commands: ls, pwd, cd, cat, and less
common ls flags: h - human-readable format, l - lists files permissions, owners, size, timestamp, et, R - displays subdirectories and the files and subdirectories they contain
- touch command creates files/updates time stamps
- Text-editors: nano, vim, LibreOffice, MS Word, gedit
- rm, rmdir, mkdir, cp, mv, file globbing (* and ?)
- Keyboard Tricks: Tab auto-fill, history, Shift Ctrl C/V
- sudo masking the root user for permissions (password-required)
3.
- man, info (interactive), jounralctl (system logs), grep (filter command)
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

