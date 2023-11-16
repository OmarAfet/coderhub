/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function kSumSubset(dateString) {
	currentYear = 2023;
	givenYear = Number(dateString.slice(0, 4));
	if (givenYear <= currentYear - 4 && givenYear > currentYear - 200) {
		return true;
	} else {
		return false;
	}
}
