/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function longestAlternatingSubstring(digits) {
	let longest = "";
	let current = "";
	let lastEven = false;
	let lastOdd = false;
	for (let i = 0; i < digits.length; i++) {
		if (digits[i] % 2 == 0) {
			if (lastEven) {
				current = digits[i];
			} else {
				current += digits[i];
			}
			lastEven = true;
			lastOdd = false;
		} else {
			if (lastOdd) {
				current = digits[i];
			} else {
				current += digits[i];
			}
			lastEven = false;
			lastOdd = true;
		}
		if (current.length > longest.length) {
			longest = current;
		}
	}
	return longest;
}
