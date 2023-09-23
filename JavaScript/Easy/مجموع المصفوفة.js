/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function calculate_sum(lst) {
	let sum = 0;
	for (let i = 0; i < lst.length; i++) {
		if (lst[i] == 7) {
			break;
		} else {
			sum += lst[i];
		}
	}
	return sum;
}
