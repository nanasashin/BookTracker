async function test() {
	try {
		const content = await fetch("api/test");
		const data = await content.json();
		console.log(data);
	} catch (error) {
		console.error("Failed to fetch: ", error);
	}
}