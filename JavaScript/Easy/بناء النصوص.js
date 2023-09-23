/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function string_builder(expression) {
	let stack = [];
	let current_str = "";
	let current_num = 0;

	for (let char of expression) {
		if (char.match(/\d/)) {
			current_num = current_num * 10 + parseInt(char);
		} else if (char == "[") {
			stack.push(current_str);
			stack.push(current_num);
			current_str = "";
			current_num = 0;
		} else if (char == "]") {
			let num = stack.pop();
			let prev_str = stack.pop();
			current_str = prev_str + current_str.repeat(num);
		} else {
			current_str += char;
		}
	}

	return current_str;
}
