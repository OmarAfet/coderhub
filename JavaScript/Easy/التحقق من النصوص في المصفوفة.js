/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function stringCheck(value) {
	let x = null;
	for (let i = 0; i < value.length; i++) {
		const e = value[i];
		if (x == null) {
			x = e;
		} else if (x !== e) {
			return false;
		}
	}
	return true;
}
