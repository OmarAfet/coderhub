/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function removeSpecialCharacters(strParam) {
	let str = "";
	for (let i = 0; i < strParam.length; i++) {
		if (strParam[i] == "-" || strParam[i] == "_" || strParam[i] == " " || (strParam[i] >= "a" && strParam[i] <= "z") || (strParam[i] >= "A" && strParam[i] <= "Z")) {
			str += strParam[i];
		}
	}
	return str;
}
