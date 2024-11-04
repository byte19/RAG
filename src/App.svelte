<script>
    import Camera from "./camera.svelte";
import FileDrop from "./fileDrop.svelte";
</script>


<main>
	<FileDrop/>
	<!-- <Camera /> -->
</main>
<button style="color: blue">
	Submit for Processing
</button>

<style>
	main {
		background-color: grey;
		text-align: center;	
		display: block;
		margin: auto;
		padding: 10%;
		padding-bottom: 25%;
		max-width: 70%;
		height: fit-content;
	}
	button {
		display: block;
		margin: auto;
		margin-top: 5%;
	}
</style>
