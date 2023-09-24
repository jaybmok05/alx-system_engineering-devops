<h1>0x0B. SSH</h1>
<hr>
<p>This directory contains a series of tasks on SSH. The goal of this project was to gain experience utilising the SSH protocol to connect to and interact with servers.</p>

1. Task 0 - Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
	- Requirements:
		- Only use ssh single-character flags
		- You cannot use -l
		- You do not need to handle the case of a private key protected by a passphrase

2. Task 1 - Write a Bash script that creates an RSA key pair.
	- Requirements:
		- Name of the created private key must be school
		- Number of bits in the created key to be created 4096
		- The created key must be protected by the passphrase betty

3. Task 2 - Client configuration file
	- Requirements:
		- Your SSH client configuration must be configured to use the private key ~/.ssh/school
		- Your SSH client configuration must be configured to refuse to authenticate using a password

4. Task 4 - using Puppet to make changes to our configuration file
	- Requirements:
		- Your SSH client configuration must be configured to use the private key ~/.ssh/school
		- Your SSH client configuration must be configured to refuse to authenticate using a password
