import datetime
from database import DATABASE

db = DATABASE()

start = """
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
 h6{
	text-align: center;
}
table{
    border: thick solid #000;
    border-spacing: 0;
	width: 90%;
color: #000;
margin-left: auto;
margin-right: auto;
}
td{
    border: thin dashed #000;
    width: 300px;
    padding: .3em;
    text-align: center;
}

th{
    border-bottom: thin solid #000;
    width: 300px;
    padding: .3em;
	text-align: center;
}
tr{
   
    width: 300px;
}

tr:nth-child(odd){
    background-color: #e2e2e2;
}
tr:nth-child(even){
    background-color: #fff;
}


tr:last-child
td:nth-child(2){
  border: none;  
  
}

th:nth-child(1){
width:25px;
}
tr:nth-child(n+1):hover{
font-weight: bold;
}
td:nth-child(1){
width: 25px;
text-align: center;
}
td{
text-align: center;
border: none;
}
li:hover
a:hover{
font-weight: bold;
background-color: #e2e2e2;
}
li
a{
-webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-align: center;
    font-weight: bold;
    color: #111;
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
      <h2>User Leaderboard</h2>
      """

start = start + '<h6>Last Updated: ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + ' EST</h6>'
table = """
<table>
  <tr>
    <th>Rank</th>
    <th>Username</th> 
    <th>Score</th>
  </tr>
"""
users = db.Fetch_Top_Users('all')
rank = 1
for i in users:

	table = table + '<tr><td>' + str(rank) + '</td>'
	table = table + '<td>' + i['userName'] + '</td>'
	table = table + '<td>' + str(int(i['score'])) + '</td></tr>'
	rank = rank + 1

table = table + '</table>'


end = """
    </div>
  </div>
</div>
<footer class="container-fluid">
  <p><a href="https://www.meclab.org">Morphology, Evolution, Cognition Lab</a></p>
</footer>
</body>
</html>
"""
f = open('users.html','w')
f.write(start + table + end)
f.close()


