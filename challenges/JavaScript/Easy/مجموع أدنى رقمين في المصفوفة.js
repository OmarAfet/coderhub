/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function sum_two_smallest_nums(arr) {
	arr = arr.sort((a, b) => a - b);
	return arr[0] + arr[1];
}
