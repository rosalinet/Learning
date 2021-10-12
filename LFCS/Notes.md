# LFCS Notes
## About Linux
- The creator/founder of Linux is Linus Torvalds.
	- He said it should be free
	- It was ripped off of Unix (which costs $$$ and is the "company" version of Linux)
- Linux started off as a shell.
- Linux is free, open source, and non-profit.
- The terminal is the REAL computer.
	- Think of it as the "inside" of your body
	- The interface is just the "pretty skin"
- MacOS and Windows were made to be more user-friendly with a nice GUI (graphical user interface).
	- These operating systems do cost money for their ease-of-use
	- MacOS uses bash shell like Linux, but Windows uses powershell
- EVERYTHING revolves around the shell.
- ZShell is a pretty mod for bash that helps color-code it.
- CentOS -> The server side of Linux (Ubuntu 18 is also common and VERY similar. 
	- Most notable difference (at the moment) is the difference in package managers (apt vs yum)

## Basic Linux Info
- The main user is root. ("/")
	- You can use root's power/privilege with "sudo"
	- "sudo" -> a command that lets users pretend to be root for commands that need authentication.
	- You can specify which users can use root permissions (who is in the "root" group?)
	- root has FULL access to the computer. 
	- If you aren't in the root group, you'll need root's password to do big commands
- Every user has a home.
- Paths can be condensed together in one line for ease of access. 
	- Ex: (User) cd Doc, change position, then cd File OR SIMPLY (User) cd Doc/File instead
- You can use the tab button to auto-fill in your commands with acceptable entries.
- You can use up and down arrow keys to sift through old commands.
- A "directory" is another term for folder.
- "~" is the home directory.
- "drwx-----" these are permissions; if there is no "d" you can assume it is a file.
	- Usually looks like "drwx----- 1 user123 staff 96kb Oct 4 11:47"
	- This is read as permissions, user, group, size of file, and date last modified.
- "." is your current location.
- You can run two commands at once with && (this is a logical AND).

## Basic Commands
- cd : change directory
- pwd : print working directory
- ls : list contents
	- "-l" will list a small description of the folders
	- "-ahl" ('all') will list ALL files (inlcuding hidden (".") files)
- whoami : print current user
- history: print all commands ever used
- man <command> : short manual if you need help
	- "-" these are flags that you can use for that specific command
- touch : make a new file
- vim or vi : edit word documents
	- vimtutor : how to use vim
- nano : edit word documents (simple)
- rm : remove a file
	- rm -rf : remove a file BY FORCE
- rmdir : remove directory (you cannot remove a directory with contents unless you sudo)
- cat : show what's in a file
- cp : copy a file (format: cp (file-to-copy) (location))
- mv : move a file (format: mv (file-to-move) (new location))
	- mv can also rename files (format: mv (file-to-rename) (file's new name))
- sudo : super-user do ("sudo su -" gets you to root, password-prompted)
