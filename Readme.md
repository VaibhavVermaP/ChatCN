<h1>Terminal Chat in Python with RSA</h1>


![FastChatDemo](https://user-images.githubusercontent.com/93963406/147853981-6cc5c56f-36f1-40c1-a09b-8d7a6f522e14.gif)


<h3>Prerequisites</h3>
	<ul><li>python3</li></ul>

<h3>How to run server</h3>
	<ul><li>run server.bat</li></ul>

<h3>How to run client</h3>
	<ul><li>run client.bat</li></ul>

<h3>Choosing an encryption</h3>
	<ul><li>RSA with user selected primes(dont make the primes too big or too small)</li>
	<li>RSA with random primes</li></ul>

<h3>Important points</h3>
<ul><li>make sure to give recievers public key (shown on recievers termnial)</li>
<li>make sure server is running before starting client (ie enter clients public key in server first)</li>

<li>you may change <b><i>localhost</i></b> to the ip of the server if it is not being run on the same device</li></ul>


<h3>Running through Terminal</h3>
<ol><li>open directory in cmd/shell</li>
<li>to run server use command <i><b> python server.py [port] </b></i>
</li>

<li>to run client use command <i><b>python client.py localhost [ip adress] [port]</b></i></li></ol>


