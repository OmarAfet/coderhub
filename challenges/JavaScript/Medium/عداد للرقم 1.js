/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function count_ones(num) {
	let binary = num.toString(2);
	let count = 0;
	for (let i = 0; i < binary.length; i++) {
		if (binary[i] == 1) {
			count++;
		}
	}
	return count;
}
