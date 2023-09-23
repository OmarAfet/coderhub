/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function cumulative_addition(elements_array) {
	let sum = 0;
	for (let i = 0; i < elements_array.length; i++) {
		sum += elements_array[i];
	}
	return [sum, elements_array.length];
}
