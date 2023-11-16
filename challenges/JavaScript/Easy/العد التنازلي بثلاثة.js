/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function countdown(num) {
	if (num <= 3) {
		return [0];
	} else {
		let even_numbers = [];
		let countdown = num;
		while (countdown > 0) {
			if (countdown % 2 == 0 && countdown != num) {
				even_numbers.push(countdown);
			}
			countdown -= 3;
		}
		return even_numbers.sort((a, b) => a - b);
	}
}
