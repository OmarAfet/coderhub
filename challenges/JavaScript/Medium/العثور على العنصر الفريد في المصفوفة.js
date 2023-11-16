/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function unique(arr) {
	let arr2 = [];
	for (let i = 0; i < arr.length; i++) {
		let count = 0;
		for (let j = 0; j < arr.length; j++) {
			if (arr[i] == arr[j]) {
				count++;
			}
		}
		if (count == 1) {
			arr2.push(arr[i]);
		}
	}
	return arr2;
}
