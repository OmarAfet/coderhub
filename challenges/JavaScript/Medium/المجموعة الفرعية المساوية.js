/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function kSumSubset(numArray, k) {
	function helper(arr, target, idx) {
		if (target === 0) {
			return true;
		}

		if (idx === arr.length) {
			return false;
		}

		if (target >= arr[idx] && helper(arr, target - arr[idx], idx + 1)) {
			return true;
		}

		return helper(arr, target, idx + 1);
	}

	return helper(numArray, k, 0);
}
