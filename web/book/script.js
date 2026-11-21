async function test() {
	const content = fetch("api/test");
	const data = (await content).json;
	console.log(data.message);
}