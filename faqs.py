main_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Twitch Plays Robotics</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Set height of the grid so .sidenav can be 100% (adjust if needed) */
    .row.content {height: 1500px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      background-color: #e2e2e2;
      height: 100%;
    }
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
      text-align: center;  
    }
    footer
    p
    a{
    text-decoration: underline;
    color: #96d4ec
    }
    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height: auto;} 
    }
   h2{
	text-align: center;
}
p{
margin-left: 7.5%;
margin-right: 7.5%;
line-height: 28px;
font-size: 16px;
}
li:hover
a:hover{
font-weight: bold;
background-color: #e2e2e2;
}
.nav
li
a{
-webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-align: center;
    font-weight: bold;
    color: #111;
    }
    dt{
    padding-top: 15px;
    color: #000;
    }
  </style>
</head>
<body>
<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
<img src="TPR.png" class="img-responsive" style="width: 90%; margin-right:auto; margin-left:auto; margin-top: 1em;" alt="TPR Logo">
      <h4>Menu</h4>
      <ul class="nav nav-pills nav-stacked">
        <li><a href="index.html">Home</a></li>
        <li><a href="users.html">Users</a></li>
        <li><a href="cmds.html">Commands</a></li>
        <li><a href="faqs.html">FAQs</a></li>
      </ul><br>  
    </div>
    <div class="col-sm-9">
      <hr>
      <h2>FAQs</h2>
      <h5 style=text-align:left; margin-left: 4em;><strong>Contents</strong></h5>
      <ul>
      	<li><a href="#project">What is this project about?</a></li>
      	<li><a href="#twitch">Why are we using Twitch?</a></li>
      	<li><a href="#team">Who is the TPR Team?</a></li>
      	<li><a href="#robots">What robots are used in this project?</a></li>
      	<li><a href="#commands">What are commands?</a></li>
      	<li><a href="#reinforcements">How can I give feedback?</a></li>
      	<li><a href="#scores">What are scores?</a></li>
      	<li><a href="#relearning">What is reinforcement learning?</a></li>
      </ul>
      
      <dl>
      	<dt><div id="project">What is this project about?</div></dt>
      	<dd>This project is called Twitch Plays Robotics (TPR,) and was created by the Morphology, Evolution, and Cognition Lab at the University of Vermont.  The main idea of it is "Can the community 
      		teach robots natural language?"  It relies on two basic principles: reinforcement learning, and crowdsourcing.  Reinforcement learning is the method of evolution used for the robots in this 			project (which is described in more detail below,) and crowdsourcing is where the community factor ties in. The whole project revolves around you. While watching the robots, you can vote 
      		on the next command to teach them, give them feedback on what they are currently learning, say if you like or dislike the current robot, or just watch and see what they do (but we
      		really hope you participate one way or another!)</dd>
      	
      	<dt><div id="twitch">Why are we using Twitch?</div></dt>
      	<dd>The Twitch platform was used for this project for the convenience of it. We (the TPR team,) can broadcast the robots and displays to you, and you can provide feedback in real-time
      		using the chat window.  </dd>
      		
      	<dt><div id="team">Who is the TPR Team?</div></dt>
      	<dd>The TPR team consists of the following three UVM affiliates: 
      		<ul>
      			<li>Josh Bongard: Professor, designer and founder of TPR. </li>
      			<li>Zahra Mahoor: Postdoc, database management and backend.</li>
      			<li>Jack Felag: Undergraduate student, frontend design and website.</li>
      		</ul></dd>
      		
      	<dt><div id="robots">What robots are used in this project?</div></dt>
      	<dd>The robots used were designed using Pyrosim, a python robotics wrapper used with Open Dynamics Engine.  The robots have a plethora of different morphologies, with some mimicking animals,
      		and others as odd, unnatural shapes.  The robot displayed will change every thirty (30) seconds. </dd>
      	
      	<dt><div id="commands">What are commands?</div></dt>
      	<dd>Commands are given to the robot in the form !commandName, for example "!move" if you would like to vote for jump as the next command. At the end of each voting cycle, the command with the 
      		most votes will be given to the robots to learn.  The users can then provide feedback on that command, and vote for the next command to learn, thus repeating the cycle. The command 
      		will be changed every three (3) minutes.</dd>
      	
      	<dt><div id="reinforcements">How can I give feedback?</div></dt>
      	<dd>Users can give feedback to the robots through reinforcements.  Reinforcements are typed in the form !C[Y/N], where C is the color of the robot, Y means yes, and N means no.  
      		For example, if you think the red robot is following the command properly, you would type "!ry".  If not, you would type "!rn".  This will then create a correlation between 
      		reinforcements, the command given, and the robot's action, which will then improve its behavior over time given enough feedback.</dd>
      	
      	<dt><div id="scores">What are scores?</div></dt>
      	<dd>Scores in this project are used as a way to gauge user participation and command progress. The higher a user's score, the more they helped in the learning process of the robots.  
      	The higher a command's score is, the more training the robot has done to learn that command.</dd>
      	
      	<dt><div id="relearning">What is reinforcement learning?</div></dt>
      	<dd>Reinforcement learning is the main concept behind the evolutionary algorithm used in this project.  To put it simply, it is like training a dog.  You say sit (the command,) 
      	and when they sit, you give a treat (positive reinforcement.)  The dog will then learn when you say "sit", and they perform the desired action, it will receive food.  </dd>
      	
      </dl>
      
    </div>
  </div>
</div>
<footer class="container-fluid">
  <p><a href="https://www.meclab.org">Morphology, Evolution, Cognition Lab</a></p>
</footer>
</body>
</html>
"""
f = open('faqs.html','w')
f.write(main_page)
f.close()

