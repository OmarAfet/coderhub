/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function word_repeat(word, n) {
	x = "";
	for (let i = 0; i < n; i++) {
		x += `${word} `;
	}
	return x.slice(0, -1);
}
