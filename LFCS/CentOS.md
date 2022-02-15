#These notes reflect LinkedIn's "Learning CentOS Linux" course by Scott Simpson

What is CentOS?
  - (C)ommunity (ENT)nterprise (O)perating (S)ystem
  - Dervied from Red Hat Enterprise Linux (RHEL)
  - CentOS is free and community supported
  - Used to be independent, but joined Red Hat in 2014
  - Fedora tests new features -> Red Hat updates with some new changes from Fedora -> CentOS derives from RHEL and lags behind updates
  - Well-established features
  - Organizations often use Red Hat for production systems and CentOS for development

Filesystem Hierarchy Standard (FHS)
  / = root, highest level in the hierarchy
  /bin = command binaries (grep, awk, bash)
  /boot = boot loader (grub), kernel
  /dev = system devices, hardware and software resources (devrandom, devurandom, devnull, disks, sda, sda1)
  /etc = system config files, /etc/sysconfig
  /home = default landing spot for users to connect, keeps user files separate
  /lib = system/service libraries
  /media = mount point for removable media
  /mnt = mount temp filesystems
  /opt = third-party packages, folder structures
  /proc = system information
  /root = home folder for root user
  /run = information on process information
  /sbin = system binaries
  /srv = information and files for various services
  /sys = system information (/proc) in a different format
  /tmp = temporary files (cleared when system restarts)
  /usr = another place for applications to live
  /var = logs and files that change over time
 
 Network Address - Allows a server to communicate with its clients. (CHeck ip with the "ip a" command)
 2 Ways to Assign an Address to a Server:
  Dynamic - Assigned by the Network's DHCP server as needed (can change)
  Static - Fixed Address set locally by administrator or set by DHCP (reserve IP address and assign it consistently)
 2 Ways to Make Configuration Changes to use either option:
  Set via configuration file (Manually) - Interfaces like /etc/sysconfig/network-scripts/ifcfg...
  Controlled wit NetworkManager (Built-In Software) - Application for controlling network interfaces

- Manually setting the network address:
  1. cd /etc/sysconfig/network-scripts (Change directory to network-scripts)
  2. Find ethernet (ifcfg-eno1 or similar; usually first option if you ls)
  3. vi (or other txt editor like nano) ifcfg-eno1(ethernet) file
  4. FOR A DYNAMIC ADDRESS (DHCP):
      Configuring CentOS with DHCP here will tell it to listen for an offer from a DHCP server and accept it to set its IP address.
      Set BOOTPROTO to dhcp, and ONBOOT to yes
      Do not set up other information like IP address, gateway, or netmask.
  5. FOR A STATIC ADDRESS:
      Set BOOTPROTO to static, and ONBOOT to yes
      Add the line IPADDR=10.0.1.20 (or just outside of whatever you configured the DHCP range to be so that this IP is not handed out to any other device)
      Add the line NETMASK=255.255.255.0 (this is for most home network's, but on enterprises it can be different (ask network administrator))
      Add the line GATEWAY=<ip address of the router>
      This is all you need to set up a static IP address, but you won't be handed a DNS server for name resolution.
        Therefore, even if you get an IP, web browsers and other services that nned to try to connect to services with names wouldn't know how to find those servers.
      You can set the DNS with DNS1=8.8.8.8 (one of Google's public DNS servers)
      You can also setup a DNS2=1.1.1.1 (CloudFlare's public DNS; incase the primary one isn't responding)
  6. Add the line: NM_CONTROLLED=no to explicitly tell the network manager software to not make changes to this interface's configuration.
  7. Save and close; then restart the network interface by running "systemctl restart network"
    (Use ip a to see if your new settings have applied)
    (You can ping a DNS server or a website address to check for a response. Ex: ping linkedin.com)
    
- Connecting the Network Address with Network Manager:
  - Network Manager has a GUI, TUI, and CLI (nmcli)
  1. Check that NM_CONTROLLED is removed or set to YES in the /etc/sysconfig/network-scripts/ifcfg-en(whatever your ethernet config file is)
  2. nmcli connection (or "nmcli c" for short) to see your current connection.
      If nothing is listed, then your network is not configured with Network Manager. If it IS listed and green, then it is working.
  3. nmcli c e(edit flag) enf(whatever your connection device is named)
  4. Some important commands: remove, set, describe, and print
  5. FOR A DYNAMIC ADDRESS:
      set ipv4.method auto (Remove static address when prompted)
      remove ipv4.dns
      remove ipv4.gateway
  6. FOR A STATIC ADDRESS:
      set ipv4.method manual
      set ipv4.addresses 10.0.1.10/24 (or whatever ip address)
      set ipv4.dns 8.8.8.8
      set ipv4.gateway 10.0.1.1 (ip address of the router is)
  8. "save" command, then "quit" command, then restart network interface with "systemctl restart network"
    (Use ip a to see if your new settings have applied)
    (You can ping a DNS server or a website address to check for a response. Ex: ping linkedin.com)
 
  - Hostnames should be useful and memorable, >64 characters (alphanumeric and dashes allowed)
      hostnamectl command tells you current hostname/system info
      hostnamectl --static set-hostname "poseidon" (changing your static hostname)
      hostnamectl --pretty set-hostname "Poseidon" (shows up here and there and accepts more special characters)
      cat /etc/hostname to see what the current hostname is
      Restart the machine to see the new hostname (root@poseidon)
      
- Secure Shell (SSH)
  Establishes a secure connection for remote terminal access
    Uses a username and password (easier) or username and keypair (more secure)
  Best practices: do not connect to servers remotely as root or even allow root to log in remotely, and use keys instead of passwords.
  Known host fingerprints are kept locally in ~/.ssh/known_hosts and are checked each time you connect to the server in the future.
  ssh user@(ip address) to connect to an ssh server and work with a system
  Use exit to leave the server.
  - If using a different port for SSH (by default it's 22) then you'll need to add an option to your SSH string about that: ssh user@host -oPort=2222 (whichever port)
  - It is also good practice to use/add a user who has sudo privileges over SSH than to use root. (adduser, passwd, usermod -aG wheel <USER> (adds user to wheel group))
    - Tip: using the -e flag, "sudo passwd -e <USER>" prompts the user to change their password to whatever they'd like after they log in for the first time.
    - The wheel group is the root group of CentOS.
  Within the SSH server, use "sudo vi /etc/ssh/sshd_config" to edit the sshd configuration file.
    - This file has a line PermitRootLogin; change this to no (good practice), then restart with systemctl restart sshd.

- Keypairs with SSH
  Keypairs are made of two parts: a public key (stored on servers you want to connect to) and a private key (stored on your computer)
    - Generating keys is usually done on the client, not server, so users can keep their own private keys instead of being given one by an administrator.
  Use "ssh-keygen" on your home client and follow the steps; 2 files will be generated in your ssh directory, a public and a private.
  Create a .ssh directory on the host, creat an authorized_keys file, and copy the public key generated on the client into this file on the host.
    - Use "sudo vi /etc/ssh/sshd_config" and find PubkeyAuthentication and set it to yes, find PasswordAuthentication and set it to no.
    - Save and reset like usual.
    - Make sure the correct permissions are in place. (700 for .ssh/, 600 for authorized_keys)
  Now log in to your host from your client using a -i flag and explicity listing the path to the private key. (ssh user@host -i ./ssh/id_rsa)
  
- Transferring Files to the Server: sftp (SSH File Transfer Protocol) or scp (secure copy)
  sftp -i .ssh/id_rsa user@hostname (opens a limited shell that allows you to transfer files, use help to see commands)
    Useful commands: get <FILENAME>, put <FILENAME>, bye (exit)
  scp -i .ssh/id_rsa user@hostname:<FILENAME/RELATIVE-PATH/ABSOLUTE-PATH> . (copies a file FROM the server, : represents home folder, copies it to . (client's home folder))
  scp -i .ssh/id_rsa <LOCALFILE> user@hostname: (sends a file to the home folder of the host server, you can add a path after : to specify where it goes)
 
- File Permissions
  -rw-rw-r--. 1 scott wheel 20 Dec 19 23:28 examplefile1
  (USER)(GROUP)(OTHER) (SYMBOLIC LINKS) (USER) (USER'S GROUP) (DATE AND TIME) (FILENAME)
  - denotes a file, d denotes a directory
  r - READ (4), w - WRITE (2), x - EXECUTE (1)
  See permissions with ls -l or stat
  chown (change owner command), chgrp (change group command), chmod (change permissions command)
  groupadd <GROUPNAME> creates an entry for the group in the /etc/group file with a : between the group and users. (usermod -aG <GROUPNAME> <USER>)
  
- Package Management
  Yum (Yellowdog Updater, Modified) package manager that uses RPM (Red Hat package manager)
  - Yum pulls from repositories like apt does for Debian distributions.
  yum repolist shows repositories available; the system will determine which mirrors are closest or fastest.
    - The Base repo has packages that make up other roles that we saw as options for installation (the versions that make up the release).
    - The Extras repo has extra tools.
    - The Updates repo offers updated versions of packages that aren't part of the current release.
    - The system comes with more features, but they are disabled. (Seen by using yum repolist all)
  yum commands:
    To install packages: yum install <PACKAGENAME> (You can list multiple packages within the same line)
    To search for available repos depending on what you want: yum search <TARGET PACKAGE>
    To show all software versions and updates avilable compared to what is on the system: yum check-update 
    To update a particular package: yum update <PACKAGENAME> 
      To install ALL updates available: yum update
    To find out more about a package: yum info <PACKAGENAME>
    To search the repo for any package with a name matching a term: yum list <TERM> (It will show avilable or installed)
      - list searches name only, search searches description text, search all shows possibly relevant packages as well, provides finds packages that offer certain tools
    To remove a package: yum remove <PACKAGENAME>
    - Installing and managing packages by groups allows you to control whole sets of packages without having to keep name of ALL individual packages.
    To see which groups are available: yum grouplist
    To find out more about a group: yum groupinfo "<GROUPNAME>" (shows mandatory and optional packages that will/can be installed)
    To install a group of packages: yum groupinstall "<GROUPNAME>" (and any of the optional packages after separated by a space)
    To remove a group of packages: yum groupremove "<GROUPNAME>"
  2 General Approaches to Adding Packages NOT a Part of Regular Distro Repos: manually from .rpm file OR add third-party repo
    Manual .rpm:
      1. Go to website, download section, copy url, and use wget command. (May need to install wget)
      2. Find the downloaded package in your system, then install with rpm -i(install flag) <PACKAGE.rpm>
      - To update, download the new version then use rpm -U(update flag) <NEWPACKAGEVERSION.rpm>
      - To remove, use rpm -e(remove flag) <PACKAGENAME>
    Third-Party Repo:
      Updates with yum (easier updates)
      - Follow instructions provided for the specific repo.

- SELinux (Security-Enhanced Linux) (BASIC LEVEL)
  - Originally developed by NSA
  - Provides access control policies for Linux
  - Tags every file and resource on the system for more granular security
    - Based on the idea that when processes run, they inheret the permissions of the user that starts them.
  - Many processes are started by root.
  SELinux sets security contexts.
    - Tagged with web server context, no web server context tag = no access.
  Standard Linux uses Discretionary Access Control (DAC): users, groups, permissions
  SELinux uses Mandatory Access Control (MAC): adds labels to objects on the file system for more granular access control
  SELinux Operating States:
    - Enforcing (Strict; targeted): Enforces SELinux policies, granting and preventing access to resources strictly.
    - Permissive (Strict; targeted): Checks for requests, but only logs exceptions, and allows operations to continue.
    - Disabled (No policy): SELinux doesn't participate in system security at all.
  Strict mode: ALL activity subject to SELinux restrictions
  Targeted mode: Only SPECIFIC processses are enforced
  Check SELinux status by using sestatus command (enabled or disabled with policy name)
  ls -Z shows security context of files (where you typically see the date with ls -al)
    (USER CONTEXT):(ROLE CONTEXT):(TYPE CONTEXT):(MLS) (multi-level security context)
    - By default, things created in the user's home folder have a user_home_t(ype) context, and a unconfined_u(ser) context, which means that it's out of the scope for SELinux's protection policy
  SELinux uses Type Enforcement (TE), Role-Based Access Control (RBAC), and Multi-Level Security (MLS) to determine whether an action is permitted.
    - RBAC and MLS are not used in Targeted mode.
  Processes have context as well, seen by running "ps axZ"
    - If the type does not match the type it is trying to access, and policies are being enforced, then access will be denied.
  Many well-known processes are covered, but you can customize policies with booleans.
  - Follows principle of least privilege
  Commands:
    setenforce (1|0) shows/sets whether enforcing or permissive is active. (1 is yes, 0 is no)
      - Changing this only lasts until the system is rebooted. To keep the changes even through boot, edit the /etc/sysconfig/selinux file.
      - It's a good idea to leave type on Targeted.
    chcon changes context of files
    setsebool changes the boolean value
    setenforce 0 changes to permissive mode (as mentioned before) or turns off SELinux for the current session (until boot)
    aureport --avc shows the AVC events in the audit log (any denied messages)
    
Working with Services
  - Services are programs or tolls that run in the background.
  systemctl lists all active services on the system
  systemctl status <UNITNAME> shows info on a specific service
  systemctl start|stop <UNITNAME> starts or stops services temporarily
  systemctl enable|disable <UNITNAME> changes whether or not a service starts at boot
  - Services are defined in unit files found in /usr/lib/systemd
  - Firewalld controls iptables; firewall commands need sudo permissions
    firewall-cmd --get-zones shows security zones on your system
      - Common ones to modify are block, drop, and public
    firewall-cmd --get-active-zone shows the active zone and which interface(s) (network devices) is being used
    firewall-cmd --zone=public --list-all shows what services are allowed through the firewall
    firewall-cmd --zone=public --add-port=80/tcp --permanent adds the tcp protocol to port 80 on the specified zone, and the permanent flag keeps this setting even after reboot
    firewall-cmd --reload updates any changes
    firewall-cmd --zone=public --remove-port=80/tcp --permanent removes the added port permanently
    firewall-cmd --zone=public --add-service=http --permanent adds the http service to the allowed services in the firewall permanently
    firewall-cmd --zone=public --remove-service=http --permanent removes the http service to the allowed services in the firewall permanently
  
    
  
  
