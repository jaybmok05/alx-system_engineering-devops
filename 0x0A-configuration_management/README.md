<h1>0x0A. Configuration management</h1>
<p>Thisbdirecctory will contain serie of tasks on puppet configuration</p>
<hr>

0. Task 0 - Create a file
	- Using Puppet, create a file in /tmp.

	- Requirements:

		- File path is /tmp/school
		- File permission is 0744
		- File owner is www-data
		- File group is www-data
		- File contains I love Puppet

1. Task 1 - Install a package
	- Using Puppet, install flask from pip3.

	- Requirements:
		- Install flask
		- Version must be 2.1.0

2. Task 2 - Execute a command
	- Using Puppet, create a manifest that kills a process named killmenow.

	- Requirements:
		- Must use the exec Puppet resource
		- Must use pkill
