/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function get_duplicate_elements(arr) {
	let x = [];
	let y = [];

	for (let i = 0; i < arr.length; i++) {
		const e = arr[i];

		if (x.includes(e) && !y.includes(e)) {
			y.push(e);
		} else {
			x.push(e);
		}
	}

	return y;
}
