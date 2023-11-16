/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function input_type(value) {
	if (/^[^\d]+$/.test(value)) {
		return "string";
	} else if (/^\d+$/.test(value)) {
		return "integer";
	} else if (/^\d+\.\d+$/.test(value)) {
		return "double";
	}
}
