/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function sub_arrays(arr1, arr2) {
	let result = [];
	for (let i = 0; i < arr1.length; i++) {
		result.push(arr2[i] - arr1[i]);
	}
	return result;
}
