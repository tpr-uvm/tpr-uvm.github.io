main_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>FAQs</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Set height of the grid so .sidenav can be 100% (adjust if needed) */
    .row.content {height: 1950px}
    
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
color: #111;
}
.nav
li
{
-webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-align: center;
    font-weight: bold;
    color: #111;
   
    }
    li.button1{

    background-color: #22bf22;
    }
    
    .nav
    li:hover
{
-webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-align: center;
    font-weight: bold;
    color: #111;
   
    }
    li.button1
    a:hover{
    background-color: #01bf01;
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
      	<li class="button1"><a href="consent.html">Play TPR!</a></li>
        <li><a href="index.html">Home</a></li>
        <li><a href="users.html">Users</a></li>
        <li><a href="cmds.html">Commands</a></li>
        <li><a href="faqs.html">FAQs</a></li>
        <li><a href="https://discord.gg/HEwMhfP">Discord Chat</a></li>
        <li><a href="abusepolicy.html">Abuse Policy</a></li>
        
      </ul><br>  
    </div>
    <div class="col-sm-9">
      <hr>
      <h2>FAQs</h2>
      <h5 style=text-align:left; margin-left: 4em;><strong>Contents</strong></h5>
      <ul>
      	<li><a href="#project">What is this project about?			</a></li>
      	<li><a href="#teach">How do I teach the robots?				</a></li>
      	<li><a href="#commands">What are commands?				</a></li>
      	<li><a href="#learn">How do the robots learn?				</a></li>
      	<li><a href="#liking">Why should I like (or dislike) a robot?		</a></li>
      	<li><a href="#whatcommands">What commands are available?		</a></li>
      	<li><a href="#robots">What robots are used in this project?		</a></li>
      	<li><a href="#silver">What is the silver robot that's displayed?	</a></li>
      	<li><a href="#twitch">Why are we using Twitch?				</a></li>
      	<li><a href="#team">Who is the TPR Team?				</a></li>
      	<li><a href="#myscore">How is my score calculated?			</a></li>
      	<li><a href="#cmdscore">How are command scores calculated? 		</a></li>
      	<li><a href="#more">Where can I learn more?  				</a></li>
      	<li><a href="#abuse">Why can't I swear on your stream? 			</a></li>
      	<li><a href="#realpeople">I'd like to speak to an operator.		</a></li>
      	<!-- <li><a href="# ">  </a></li> -->
      </ul>
      
      <dl>
      	<dt><div id="project">What is this project about?</div></dt>
      	<dd>Twitch Plays Robotics (TPR) is, in effect, a "school" for robots. Here, robots attempt to learn the meaning of words; you act as the teacher by helping them to learn. However, learning goes both ways: We are not sure what words these robots can learn; it is your job to figure that out.</dd>
      	
      	<dt><div id="teach">How do I teach the robots?</div></dt>
      	<dd>Think of the robots as pets. If you want to teach your pet something, you issue a command to it like "sit". You then give your pet a treat if it obeys and withhold a treat if it doesn't. Here in TPR, if the robot is obeying the current command, you type in the robot's color and 'y' for 'yes' (this is equivalent to giving the robot a treat). If you think the robot is not obeying the current command, type its color and then 'n' for 'no' (this is equivalent to withholding a treat from the robot).
 </dd>
      		
      	<dt><div id="commands">What are commands?</div></dt>
      	<dd>Here in TPR, you can vote on which command to teach the robots next simply by typing ![command], where [command] is one or more English words. Every three minutes, the most voted-on command is issued to the robots. Each robot over the next three minutes "hears" this command.
</dd>
      	
      	<dt><div id="learn">How do the robots learn?</div></dt>
      	<dd>At any one time, there is a population of robots, and one after the other is shown to the crowd. Over time, robots collect yes and no votes, as well as likes and dislikes, from the crowd. Periodically, robots that are less obedient (many no's and few yes's) and less popular (many dislikes and few likes) are deleted. They are replaced by randomly-modified copies of the more obedient and popular robots. Thus, the robots evolve rather than learn to become more obedient.</dd>
      	
      	<dt><div id="liking">Why should I like (or dislike) a robot?</div></dt>
      	<dd>As mentioned above, a disobedient robot may "die". However, despite its disobedience, the robot may act in an interesting, funny, or it may exhibit the potential to learn other commands (for example, it may have jumped when the command was 'do not jump'). By 'liking' a robot, you can decrease the probability that it will be killed.</dd>
      	
      	<dt><div id="whatcommands">What commands are available?</div></dt>
      	<dd>It's up to you: there are no prespecified commands we wish to teach the robots. You can generate a vote for any command you like simply by typing ![command]. The full list of commands issued by the crowd so far is available <a href="cmds.html">here.</a></dd>
      	
      	<dt><div id="robots">What robots are used in this project?</div></dt>
      	<dd>As you'll notice, the bodies and behaviors of the robots are all different. Indeed, what we wish to discover it not just which commands the robots can learn, but which robots are able to learn more command than others. When a robots spawns an offspring robot, the offspring has a slightly different morphology and/or behavior from its parent. Also, every hour, a new robot is "injected" into the population. Thus, like commands, there are no-prespecified robots. </dd>
      	
      	<dt><div id="silver">What is the silver robot that's displayed?</div></dt>
      	<dd>Every hour, a silver robot will pop up onto the screen. This robot is before unseen, and if you're there to watch it, you can be the first to help train it!</dd>
      	
      	<dt><div id="twitch">Why are we using Twitch?</div></dt>
      	<dd>Twitch is ideal for our project because it supports bidirectional communication. You can easily speak to the robots, and the robots can show you which commands they've learned by obeying, or failing to obey, the current command.</dd>
      	
      	<dt><div id="team">Who is the TPR Team?</div></dt>
      	<dd>We're based at the University of Vermont and we are...
      		<ul>
      			<li>Josh Bongard: Professor of computer science and team lead. 				</li>
      			<li>Zahra Mahoor: Postdoctoral associate, database management and backend development.	</li>
      			<li>Jack Felag: Undergraduate student, front-end development and website. 		</li>
      		</ul></dd>
      		
      	<dt><div id="myscore">How is my score calculated?</div></dt>
      	<dd>Users collect points by helping the robots to learn. More specifically: if you propose a command that robots subsequent learn, you get more points. More technically: your score is a function of how many yes's were provided by other users, under commands that you proposed or voted for.
      	</dd>
      	
      	<dt><div id="cmdscore">How are command scores calculated?</div></dt>
      	<dd>The higher a command's score, the better that command has been learned by the robots. More specifically, if a command collects increasing numbers of yes's as time passes, that command receives more points. It's the rate of increase in yes's that's important: a command that always collects yes's --- such as !be a robot --- will receive a low score.
      	</dd>
      	
      	<dt><div id="more">Where can I learn more?</div></dt>
      	<dd><ul>
      			<li>We published a <a href="http://www.cs.uvm.edu/~jbongard/papers/2016_ALife_Anetsberger.pdf">paper,</a> after we launched TPR v1.0 (this is v2.0).</li>
      			<li>There is also a <a href="https://www.reddit.com/r/artificial/comments/3qpm87/twitch_plays_robotics/">reddit conversation thread</a> that grew up around TPR v1.0.</li>
      			<li>Josh gave a <a href="https://www.youtube.com/watch?v=vzND2qKGKAk">lecture</a> about it at the ALife conference in 2016.	</li>
      		</ul></dd>
      	
      		<dt><div id="abuse">Why can't I swear on your stream?</div></dt>
      	<dd>This is a publicly-funded scientific experiment. Thus, we maintain a <strong>zero-tolerance abuse policy:</strong> users who attempt to abuse the site or other users will be banned upon their first offence.
      	</dd>
      	
      	
      	<dt><div id="realpeople">I'd like to speak to an operator.</div></dt>
      	<dd><ul>
      			<li>Jack Felag will be available on stream (chat only) 11am-1pm ET Monday through Friday</li>
      			<li>Zahra Mahoor will be available on stream (chat only) 1-3pm ET Monday through Friday.</li>
      			<li>Josh Bongard will be available on stream 3-5pm ET Monday through Friday.</li>
      		</ul></dd>
      	
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


