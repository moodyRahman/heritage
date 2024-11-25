<svelte:head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
	<link href="css/custom.css" rel="stylesheet">
	<title>hackNY Mentor Tree</title>
</svelte:head>

<style>
	/* Inline styles to complement custom.css */
	/* PUT ON ANOTHER FILE, code pretty, search to work */
  nav {
		background-color: black;
	}

	.navbar-brand {
		color: red !important;
		background-color: black;
	}

	.container {
		padding: 1rem;
	}
</style>

<nav class="navbar navbar-dark bg-black">
	<div class="container">
		<h1 class="navbar-brand hackny-red">hackNY Mentor Tree</h1>
	</div>
</nav>

<div class="container">
	<h2>Welcome to the HackNY Mentor Tree!</h2>
	<div style="
		display: flex; 
		justify-content: flex-end; 
		align-items: center; 
		margin-top: 1rem;"
	>
		<input 
			type="text" 
			placeholder="Search mentors or topics..." 
			style="
				width: 250px; 
				padding: 0.5rem; 
				border: 1px solid #ccc; 
				border-radius: 4px;"
		/>
		<button 
			style="
				margin-left: 0.5rem; 
				padding: 0.5rem 1rem; 
				background-color: red; 
				color: black; 
				border: none; 
				border-radius: 4px; 
				cursor: pointer;"
		>
			Search
		</button>
	</div>
</div>
