**0x13. Firewall**
---
<p>This directory will contain task on how to setup a firewall</p>
---

0. Task 0 - Let’s install the ufw firewall a
Requirements:

	- The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
	- configure ufw so that it blocks all incoming traffic, except the following TCP ports:
		- 22 (SSH)
		- 443 (HTTPS SSL)
		- 80 (HTTP)
	- Share the ufw commands that you used in your answer file

1. Task 1 - Port forwarding
Requirements:

	- Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
	- Your answer file should be a copy of the ufw configuration file that you modified to make this happen
