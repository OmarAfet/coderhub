/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function count_char(sentence, ch) {
	let count = 0;
	for (let i = 0; i < sentence.length; i++) {
		if (sentence[i] == ch) {
			count++;
		}
	}
	return count;
}
