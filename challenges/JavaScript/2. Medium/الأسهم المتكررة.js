/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function arrowDuplicates(word) {
	let table = word.toLowerCase().split("");
	let result = "";

	for (let i of table) {
		if (table.filter((x) => x === i).length > 1) {
			result += "<";
		} else {
			result += ">";
		}
	}

	return result;
}
