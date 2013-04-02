<html>
<head>
	<title>THE FINAL COUNTDOWN</title>
</head>
<body>
        <?php echo '<p>Hello! You are a visitor number:</p>'; ?>	
	<?php system('python viewcount.cgi'); ?>
	<?php echo '<p>What hour of the day to people visit the most?</p>'; ?>
	<?php system('python times.cgi'); ?>
</body>
</html>
