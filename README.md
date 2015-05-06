# PythonUbuntuSimpleApp

##Introduction:##
This tutorial will walk you through deploying a simple Hello World Python Application to any server with <a href="https://www.distelli.com" target="_blank">Distelli</a>.

<a href="https://www.distelli.com" target="_blank">Distelli</a> makes it fast and easy for developers to deploy code to any server with the push of a button. Our platform empowers developers and their teams to spend less time building and maintaining complex deployment tools and homegrown scripts so they can focus their valuable time and effort on creating the software that powers their business. Distelli is funded by <a href="http://www.a16z.com" target="_blank">Andreessen Horowitz</a>.

##Prerequisites:##
* <a href="https://www.python.org/download/releases/2.6/" target="_blank">Install Python 2.6+ on your local machine</a>.
* <a href="https://www.distelli.com/signup" target="_blank">Sign up for a free Distelli account</a>.
* <a href="https://www.distelli.com/docs/setup" target="_blank">Install the Distelli CLI Tool</a>.
* <a href="https://www.distelli.com/docs/agent-setup" target = "_blank">Install the Distelli agent on your server</a>.

##Deploying Your Python Application With Distelli##

1. Enter the following commands to clone this repository onto your local machine:
<pre>git clone https://github.com/Distelli/SimplyPythonApp.git</pre>
You should see the following message on successful clone:
<img src="https://monosnap.com/file/dO7WxGYQHEUzSHdpgIutwEiu6r9eqN.png">
Then, use the cd command to enter the directory:
<pre>cd PythonUbuntuSimpleApp</pre>

2. To create an application with Distelli, enter the following command into your terminal replacing "username" with your Distelli username:
<pre> $ distelli create username/PythonUbuntuSimpleApp</pre>
You'll be prompted to login, use the email address and password associated with your Distelli account:
<img src="https://monosnap.com/file/B5d2EA6aIUpy8XNmnf4BhbLCzzvlTK.png">
You should see the following message on successful app creation:
<img src="https://monosnap.com/file/reWlkTc98g3C7FcZ5XVnAozZkhXIKT.png">

3. To create an environment with Distelli, <a href="https://www.distelli.com/login" target="_blank">login to your Distelli account<a>. Once logged in, you should see the Python application you just created. Select the PythonUbuntuSimpleApp:
<img src="https://monosnap.com/file/Y3jmF6LY0T0bV8bySsj8MgLv0WKGht.png">
Select the environments tab:
<img src="https://monosnap.com/file/4hsF0MH3GVwmhJ6Qdpi4gbJe7XGEHa.png">
Create a new environment by selecting "New Environment":
<img src="https://monosnap.com/file/egJJz43Spp77lKCMRWibdf5wZzFmnP.png">
Name the environment "PythonEnvironment" then select the "Create Environment" button:
<img src="https://monosnap.com/file/SCF2VcjYqeViDzm7rx8yugnBaCmKkm.png">

4. Now, let's add a server to the environment. Select the "Servers" button on the top right of the page:
<img src="https://monosnap.com/file/qzW5wBqG1wa4NgcL802l356QeRgbEm.png">
Now select the "Add/Remove Servers" button on the top right of the page:
<img src="https://monosnap.com/file/Ls53cvbKibv0aItzHAe1VWQbSUGwGf.png">
You should see the server you installed the agent on prior to starting this tutorial. Add that server to the environment by selecting the add button:
<img src="https://monosnap.com/file/QCWj8EXMnIgT6mdeaUlus1e13XYxAJ.png">

5. Open the distelli-manifest.yml file with your favorite text editor. Replace <username> with your Distelli username:
<img src="https://monosnap.com/file/f8a4a7UZOQFdZi8cp7m37pGvDNZVrj.png">
<i><b>Note:</b> This is not the email you used to sign up for your Distelli account, this is the unique username selected after signup.</i>

7. Now we're ready to push our first release. Enter the following command into your terminal:
<pre>$ distelli push -m "First push with Distelli"</pre>
<img src="https://monosnap.com/file/L5dGTGGGk15fZBdxZAqEkZ9L49q1p2.png">
Enter the email and password associated with your Distelli account:
<img src="https://monosnap.com/file/eYQlme07NadLNptpqpW4TJu1q7CNTQ.png">
You should see the following message on successful push:
<img src="https://monosnap.com/file/zy6WW9hnyHL5sqQOqBSyiyqeFASgSD.png">
8. Now we're ready to deploy our first release. Navigate back to <a href="https://www.distelli.com" target="blank">Distelli.com</a>.

Select your application and then click the green lightning bolt:
<img src="https://monosnap.com/file/XBqqtNiCSmOfqN270mVF0QivA2ygOa.png">
Congrats, you've just deployed your first application with Distelli!

Questions? Shoot us an email at <a href="mailto:support@disteli.com" target="_blank">support@distelli.com</a>.
