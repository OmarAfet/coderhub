/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function replaceThe(txt) {
	let arr = txt.split(" ");
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === "the" && arr[i + 1][0].match(/[aeiou]/)) {
			arr[i] = "an";
		} else if (arr[i] === "the") {
			arr[i] = "a";
		}
	}
	return arr.join(" ");
}
