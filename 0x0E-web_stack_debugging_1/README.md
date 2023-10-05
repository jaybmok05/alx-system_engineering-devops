**0x0E. Web stack debugging #1**
---
<p>This directory will contain a series of tasks on debuging the web server</p>
---

0. Task 0 -  find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80
Requirements:
	- Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
	- Write a Bash script that configures a server to the above requirements

1. Task 1 - Make it sweet and short
Requirements:
	- Your Bash script must be 5 lines long or less
	- There must be a new line at the end of the file
	- You must respect usual Bash script requirements
	- You cannot use ;
	- You cannot use &&
	- You cannot use wget
	- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
	- service (init) must say that nginx is not running ← for real
