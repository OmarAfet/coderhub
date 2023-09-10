/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function reverse_case(strParam) {
	let newStr = "";
	for (let i = 0; i < strParam.length; i++) {
		if (strParam[i] == strParam[i].toUpperCase()) {
			console.log(strParam[i]);
			console.log(strParam[i].toUpperCase());
			newStr += strParam[i].toLowerCase();
		} else {
			newStr += strParam[i].toUpperCase();
		}
	}
	return newStr;
}
