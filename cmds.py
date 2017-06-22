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
      background-color: #f1f1f1;
      height: 100%;
    }
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
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
  </style>
</head>
<body>
<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>TPR Data</h4>
      <ul class="nav nav-pills nav-stacked">
        <li><a href="index.html">Home</a></li>
        <li><a href="users.html">Users</a></li>
        <li><a href="https://jfelag.github.io/tprInfo/cmds.html">Commands</a></li>
      </ul><br>  
    </div>
    <div class="col-sm-9">
      <hr>
      <h2>Command Information</h2>
      """

table = """
<table>
  <tr>
    <th>Rank</th>
    <th>Command</th> 
    <th>Score</th>
  </tr>
"""
commands = [ (1, 'Jump', 1000) , (2, 'Walk', 999), (3, 'Run', 923), (4, 'Stand still', 600) , (5, 'Roll', 20) ]

for i in commands:

	table = table + '<tr><td>' + str(i[0]) + '</td>'
	table = table + '<td>' + i[1] + '</td>'
	table = table + '<td>' + str(i[2]) + '</td></tr>'

table = table + '</table>'


end = """
    </div>
  </div>
</div>
<footer class="container-fluid">
  <p>TEXT</p>
</footer>
</body>
</html>
"""
f = open('cmds.html','w')
f.write(start + table + end)
f.close()


