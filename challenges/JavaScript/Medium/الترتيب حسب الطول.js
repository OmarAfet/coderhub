/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function sortByLength(txt) {
	const words = txt.split(" ");
	const sortedWords = words.sort((a, b) => {
		if (a.length !== b.length) {
			return a.length - b.length;
		}
		return a.localeCompare(b);
	});
	return sortedWords.join(" ");
}
