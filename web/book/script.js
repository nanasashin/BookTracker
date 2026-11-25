$("#save-book").on("click", async function() {
	try {
		const content = await fetch("api/test");
		const data = await content.json();
	} catch (error) {
		console.error("Failed to fetch: ", error);
	}
})