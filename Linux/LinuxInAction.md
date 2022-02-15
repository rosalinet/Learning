#These notes serve to record notes for the book titled LINUX IN ACTION by DAVID CLINTON

Chapter 1 – Welcome to Linux
Key Terms:
open source, distribution (distro), file system, index, partition, terminal, process, BASH, Plain text, File globbing, Tab completion, Pseudo file systems
What it covered:
	1. What makes Linux different
	2. Basic survival skills
	3. Getting help
1.1 
- Linux is free, true mulituser OS, and open source.
1.2
- Understanding the Linux file system and how the directory tree works.
- Root, Top-level directories: bin, etc, var, home
- What is BASH? Shell -> Operating System Software -> Kernel -> Hardware
- 5 Linux Navigation Must-Have Commands: ls, pwd, cd, cat, and less
common ls flags: h - human-readable format, l - lists files permissions, owners, size, timestamp, et, R - displays subdirectories and the files and subdirectories they contain
- touch command creates files/updates time stamps
- Text-editors: nano, vim, LibreOffice, MS Word, gedit
- rm, rmdir, mkdir, cp, mv, file globbing (\* and ?)
- Keyboard Tricks: Tab auto-fill, history, Shift Ctrl C/V
- sudo masking the root user for permissions (password-required)
1.3
- man, info (interactive), journalctl (system logs), grep (filter command)
ex: journalctl | grep filename.php | grep error
This prints off system logs including only lines that include the string filename.php, and then those files are also filtered by the filename.php files that contain the string 'error'
You can use the flag -v to invert your results (everything that DOESN'T say error)
- Use the internet for help, someone else has probably encountered your problem


Chapter 2 – Linux Virtualization: Building a Linux Working Environment
Key Terms:
virtualization, hypervisor, container, dynamically-allocated, software repository, fixed-size disk
What it covered:
	1. Finding the right virtualization technology
	2. Using Linux repository managers
	3. Building effective environments using VirtualBox
	4. Building containers with LXC
	5. How and when to closely manage VMs
2.1
- Linux dominates the virtual space; virtualization makes it easier to learn any technology
- 2 Approaches to Virtualization: Hypervisors and Containers
	- Hypervisors control host system hardware to one degree or another, providing each guest OS the resources it needs. 
	- Containers are extremely lightweight virtual servers that, rather than running as full operating systems, share the underlying kernel of their host OS.
- VirtualBox is a type 2 hypervisor, and LXC (The Linux Container) is a container manager.
2.2
- Repository/package managers: Advanced Package Tool = apt (Debian/Ubuntu) first: apt update second: apt install <REPO>
- The manager handles local indeces to track repos and their content, track the status of all software located on machine, ensures that all software is updated and has all their necessary dependencies, installs and removes packages.
- If downloading from the website, navigate to the directory that contains the software (usually Downloads), and use the command dpkg -i (install flag). 
- You can check your OS bit (32 or 64) by using the arch command.
- You can search for available packages with apt search, and you can display package info with apt show.
- Use checksum to make sure you have a non-corrupted file. You can find it from where you downloaded it and then compare it to your download by going into the same directory of the download and runing shasum <FILE> and if they match then you're okay. If not, you may need to download the file again.
- Cloning VM's: Full Clone vs Linked Clone
- VBox comes with its own command-line shell invoked by vboxmanage. You can use list vms to see all your VM's or vboxmanage clonevm to create a clone. --register <OG VM> --name <NEWNAME>
2.3
- Creating a container: lxc-create -n <NAME> -t <TEMPLATE> Template can be Ubuntu, Windows, etc
- May need to download templates first (sudo apt-get install lxc-templates)
- Ubuntu containers default to ubuntu as the user and password. Change password by using the passwd command. Check for the container with sudo lxc-ls -f.
- To start the container, use lxc-start -d(detach so that you are not dropped into an interactive session where you can only leave by shutting down the container) -n(name) myContainer(MY CONTAINER's NAME)
- To run a root shell session within a running container, use lxc-attach -n (NAMEofCONTAINER)
- In the root shell session you can run commands like ip addr to see what's going on in the container. To leave, just type exit, and you won't shut down the container. If you DO want to shut it down, use shutdown -h(halt) now (if you used the -r(reboot) flag, it would reboot) 
- You can find the main Filesystem Hierarchy Standard (FHS) in the /var/lib/lxc/<YOURCONTAINER> rootfs file. (You can use sudo su to do this in sudo)


Chapter 3 – Remote Connectivity: Safely Accessing Networked Machines
Key Terms: 
password, RSA, X11 forwarding, Y Shell, C parent shell
What it covered:
	1. Encryption and secure remote connections
	2. Linux system process management with systemd
	3. Extra secure and convenient password-free SSH access
	4. Safely copying files between remote locations with SCP
	5. Using remote graphic programs over SSH connections
3.1
- To protect the privacy of data even if it falls into the wrong hands, security software can use what's known as an encryption key, which is a small file containing a random sequence of characters. The Secure Shell (SSH) network does this quickly and invisibly.
- Many Linux distro's come with OpenSSH installed already, if not use apt install openssh-server
- RSA is a popular encryption algorithm.
3.2
- A common reason for Linux programs to not run: use systemctl status <PROGRAM> to find out whether SSH is running on your machine. If inactive, type start in place of status.
- systemctl stop <PROGRAM> stops the program, and you can also use enable or diable to automatically load or unload processes on system startup.
- The config file whose settings control how remote clients will be able to log in to your machine is /etc/ssh/sshd\_config.
3.3
- Password-free SSH access requires a key and key pair. Use ssh-keygen on the client computer. You'll be prompted for a passphrase, and it will save to a file. Use ls -l .ssh to find the key. The .pub is the public one that you'll copy to the host.
- Then make a directory if you do not already have one, with ssh <CONNECTION> mkdir -p .ssh
- Now on the client computer, use cat .ssh/id\_rsa.pub | ssh ubuntu@10.0.3.222 "cat >> .ssh/authorized\_keys" this command reads the key generated on the host computer, then connects to the client and adds the key to the clients' authorized\_keys. Now, you should be able to log in without being prompted for a password.
3.4 
- You can safely copy files over the network by using the scp command. ex: scp <FILEPATH> <example@10.0.3.222:home/ubuntu/...>
- ssh-copy-id -i .ssh/id\_rsa.pub <ubuntu@10.0.3> safely copies encryption (standard)
3.5 
- You can use graphic programs over SSH, but it may not meet your expectations. Run ssh with the -x flag for X11 forwarding. (Don't try this on a server, the OS versions usually come with little to no graphic functionality)
- Host machine: nano /etc/ssh/sshd\_confi
	X11Forwarding yes
- Client machine: nano /etc/ssh\_config
	ForwardX11 yes
- Then systemctl restart ssh on both host and client, then ssh with the -x flag and start a program, like gnome-mines!
Extra 6.
- ps command is used to view running processes, and is useful for planning and troubleshooting. You use it early and often. Adding the -e flag will show processes in the child shell and all parent shells back up to init. ([1] PID) seen with ps -ef | grep init
- You can visualize the parent and child shell/processes by using the pstree command. (the -p flag adds the PID)
- systemctl is like Task Manager.
- systemd also has networkd, journald, and udevd as services


Chapter 4 - Archive Management: Backing up or Copying Entire File Systems
Key Terms:
archive, compression, image, permissions, ownership, group
What it covered:
	1. Why, what and where to archive
	2. Archiving files and file systems using tar
	3. Searching for system files
	4. Securing files with object permissions and ownership
	5. Archiving partitions with dd
	6. Synchronizing remote archives with rsync
4.1
- An archive is a single file containing a collection of objects: files, directories, or a combo of both.
- What exactly is compression? Files are compressed into an unreadable format in order to reduce the amount of disk space it takes, but can be decompressed back through the same algorithm in reverse.
- 2 main reasons to create archives: building a reliable file system image and to create efficient data backups.
	- Images are created from all or parts of a live OS so you can copy and paste the contents onto a second computer. This is commonly used for providing identical system setups to multiple users.
	- Reasons for back-ups: hardware failure, fat fingers, insecure data loss, ransomware, etc. Back-up data should also be tested to ensure it works. Generating and monitoring log messages can help spot some problems. 
- Archiving small amounts of data: use scp command to secure location. Otherwise, use df to see how much space the partition of data that you want to back-up is. (The -h flag changes the sizes to readable byte formatting)
- If a file designation is tmpfs and the number of bytes in the Used column is 0, then you’re most-likely looking at a pseudo/temp file system.
- Where should you archive? Somewhere RELIABLE, TESTED, ROTATED, DISTRIBUTED, SECURE, COMPLIANT, UP TO DATE, AND SCRIPTED.
4.2
- 3 Things to Successfully Complete your Archive:
	Find and identify the files you want to include
	Identify the location on a storage drive that you want your archive to use
	Add your files to an archive, and save it to its storage location
	You can do all of this with tar!
- tar cvf archivename.tar * This command creates (c) a new archive, sets the screen output to verbose (v), and points to a filename you want the archive to get. All files below and within the working directory will be archived into archivename.tar.
- The tar command never moves or deletes any original directories. Using a . instead of a * will include hidden files whoes names begin with a dot.
- You can use different extensions to specify which files you'd like to archive if you don't want to archive all of them. (*.mp4, czvf (zip argument), .tar.gz to compress the archive, etc), and you can also specify the location of what you'd like to archive after the archivename.tar.gz.
- You can break down archive files into smaller parts:
	split -b 1G archivename.tar.gz "archivename.tar.gz.part" specifies 1GB per part
	To recreate the archive, you can read each part in a sequence and direct the output to a new file: cat archivename.tar.gz.part* > archivename.tar.gz
- Archive image of a working Linux installation streamed to a remote storage location:
	tar czvf - --one-file-system / /usr /var --exclude=/home/andy/ | ssh username@10.0.2.444 "cat > /home/username/workstation-backup-feb-01.tar.gz"
- Smaller example: create a zip archive of a directory called importantstuff/:
	tar czvf - importantstuff/ | ssh user@10.0.3.444 <linearrow /> "cat > /home.user/myfiles.tar.gz"
- The - flag outputs data to standard output, so we don't need to specify the filename yet. The unnamed archive is then piped into an ssh login on a remote server. The command in quotations cats the archive to the file specified in the path on the remote host.
- This command allows the archive to be transferred directly without having to be saved on the source machine. 
- Larger example: create a zip archive on a USB drive:
	tar czvf /dev/sdc1/workstation-backup-feb-01.tar.gz --one-file-system / /usr /var --exclude=/home/andy/
- The --one-file-system argument excludes all data from any filesystem besides the current one, so pseudo partitions wont be added. (They can but will need to be explicitly added) You can also explicitly exclude files with the --exclude=/pathToFileToBeExcluded. In this example, usr and var were explicitly included.
- Now looking at the previous command "Archive image of a working Linux install..." you can understand it through the smaller, broken down examples.
- To extract an archive, you'd run tar xvf archive.tar (the x is for extract) This will overwrite any files with the same names in the current directory WITHOUT warning!
- Creating an archive WITHOUT sudo will not save the permissions and ownership details.
4.3 
- The find command:
	find /pathname/ -iname <1> "*.mp4" =exec tar -rvf videos.tar {} 
- The -iname flag returns upper and lowercase results, -name returns case-sensitive. The {} tells the find command to apply the tar command to each found file. This command is looking for any .mp4 files within the give /pathname/
- The similar locate command is used when results are needed quicker. (ex: locate *video.mp4 locates any file that ends withe video.mp4). Locate is faster than find, but this is because it isn't actually searching the filesystem but instead running the search string against a preexisting index. If the index falls out of date, the searches are less accurate. You can manually update them by running updatedb
4.4
- Permissions and Ownership!
	- Permissions start with either - (file) or d (directory)
	- The permissions are then split into three sections: owner, group, and others.
	- r = read, w = write, and x = execute rights
- -rwxr-xr-x (permissions) 1 (links) root (owner) root (groupname) 13:25 Jan 01 2022 (date) thisfile (filename)
- To change permissions, you'd use the chmod tool.
	- chmod o-r /bin/thisfile (removes ability of others (o) to read the file)
	- chmod g+w /bin/thisfile (adds write permissions for the group (g))
- Numeric permissions: between 0 and 7
	- 4: Read Permission
	- 2: Write Permission
	- 1: Execute Permission
	- 7: All 3 Permissions Allowed (4+2+1)
	- 6: Read and Write Allowed (4+2)
	- 5: Read and Execute Allowed (4+1)
	- 0: NO PERMISSIONS
- So 644 would mean that the owner of the file can read and write, and the group and everyone else can only read it.
- To change number positions, you'd do chmod 644 /bin/thisfile
- Ownership can be changed using chown. (sudo chown otheruser:otheruser newfile)
4.5 
- Archiving partitions with dd can make perfect byte-for-byte images of just about anything digital, and they do not require a running host OS to serve as a base.
- HOWEVER, one wrong character in a dd command can instantly and permanently wipe out an entire drive worth of valuable data, so it is wise to be cautious.
- Example: creating an exact image of an entire disk of data follows a simple syntax
	dd if=/dev/sda of=/dev/sdb (if defines source, of defines where you want the data saved)
	dd if... of=/home.username/sdadisk.img (This saves a .img archive to the home directory)
	dd if... of=/home.username/partition2.img bs=4096 (You can create single partition archives as well AND specify the number of bytes to copy at a single time)
- To restore, just reverse the values of if and of.
	dd if=sdadisk.img of=/dev/sdb
- You should always test and confirm that your archive works.
4.6
- To regularly back up and update an archive to only save new changes instead of manually writing over an existing one, you would use rsync. (You'll need it downloaded to both machines)
- Make sure rsync is donwloaded on both machines.
- Firstly create a directory to hold your copied files on the remote server. You can do this without entering the server by typing ssh user@10.0.0.000 "mkdir syncdir"
- Then, use the command rsync -av * user@10.0.0.000:syncdir
- It'll prompt you for the password for the user account on the remote server. Then, you can double check, but your files should be on the remote server! The -a flag is a super-argument that means even subdirectories and their contents are included.
- To update your changes to any files, just run the rsync -ac * ... command again and it will output only the new/updated files!
- Considerations when measuring the value of your data:
	- How often should you create new archives, and how long will you retain old copies?
	- How many layers of validation will you build into your backup process?
	- How many concurrent copies of your data will you maintain?
	- How important is maintaining geographically remote archives?
	- Should you consider incremental or differential backups?
- Differential backup: full backup once a week (Monday), and smaller and quicker backups on each of the next 6 days. Tuesday-Friday will all backup the files changed since the Monday. On a good note, restoring a differential backup requires only the last full abckup and the most recent differential backup!
- Incremental backup: full backup once a week (Monday), and each day after will only backup new files from the previous day. These are fast and efficient, but with the data spread across multiple files, restoring can be time-consuming and complicated.

Chapter 5: Automated Administration: Configuring Automated Offsite Backups
Key Terms: exit codes, access keys, bucket, /etc directory, script
What it Covered:
	1. Automating Administrative Tasks with Scripts
	2. Increasing Security and System Efficiency
	3. Backing Up Local Data
	4. Scheduling Automated Tasks
5.1
- Example code found in /etc/cron.daily/passwd file:
	#!/bin/sh
	cd /var/backups || exit 0
	
	for FILE in passwd group shadow gshadow; do
		test -f /etc/$FILE	|| continue
		cmp -s $FILE.back /etc/$FILE	&& continue
		cp -p /etc/$FILE $FILE.bak && chmod 600 $FILE.bak
	done
- Now what does this code say/mean/do???
- "#!/bin/sh" is known as the "shebang" line; it tells the cron which shell is the active shell.
- "cd /var/backups" changes the working directory to /var/backups, and if it doesn't exist, it exits the script with an exit status code of 0. The || can be read as the logical "or"
	- Exit codes are passed when a Linux command completes. 0 is passed to indicate success, and other numbers can be configured to represent other errors/outputs.
- "for FILE in passwd group shadow gshadow; do" creates a for-loop that will take every filename within each of the four groups and test the conditions between "do" and "done" on them.
- "test -f /etc/$FILE	|| continue" tests for a matching filename in the etc directory, and if found, it assigns the next string as $FILE; the loop continues if the condition is met, if not its exits after running through all files.
- "cmp -s $FILE.back /etc/$FILE && continue" compares (if found) the contents of this.$FILE versus the $FILE backup's contents. If they are NOT identical, then the loop continues.
- "cp -p /etc/$FILE $FILE.bak && chmod 600 $FILE.bak" copies the current version in the /etc/ directory to the /var/backups/ directory and adds .bak to its name, and then it changes the file's permissions to prevent unauthorized users from reading it. The -p flag preserves original ownerships and timestamps.
- passwd, group, shadow, and gshadow are the files whose contents determine how individual users and groups will be able to access particular resources. 
- Under the /etc/passwd file, you can see user ID's, their home directory, and their default shell. A bin/false shell indicates a non-user account that shouldn't be used for login.
	- You can add a new user to your system with either useradd -m <NAME> or adduser <NAME>
	- Using adduser will create a home directory automatically, and useradd needs a -m argument.
	- adduser also prompts for a password right away. useradd will also need a sudo passwd command to assign one to the new user.
- The /etc/shadow directory shows encrypted passwords on your system.
- The /etc/group file contains info on the system and user groups.
	- You can manually give admin rights to new users by adding their names to the sudo group:
	- sudo:x:27:steve,newuser,newuser,etc (NO SPACES)
- The /etc/gshadow fiel contains encrypted versions of group passwords for use in case you want to allow group resources to non-group users.
- Here's a script called upgrade.sh to have apt automate updates!
	#!/bin/bash
	#script to automate regular software updates
	
	apt update
	apt upgrade -y
- Create the script, then make it executable (chmod +x upgrade.sh), then copy it to the /etc/cron.daily/ directory where it can run each day! (cp upgrade.sh /etc/cron.daily/
- Cron will always run as root by default.
	- If you want to run a command at the command line, you just need to write sudo ./upgrade.sh
- Here's a script that can convert spaces in filenames to underscores!
	#!/bin/bash
	echo "which directory would you like to check?"
	read directory
		find $directory -type f | while read file; do
		if [[ "$file" = *[[:space:]]* ]]; then
		mv "$file" 'echo $file | tr ' ' '_'`
		fi;
	done
