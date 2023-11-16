/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function sum_even(arr) {
	x = 0;
	for (let i = 0; i < arr.length; i++) {
		const e = arr[i];
		if (e % 2 == 0) {
			x += e;
		}
	}
	return x;
}
