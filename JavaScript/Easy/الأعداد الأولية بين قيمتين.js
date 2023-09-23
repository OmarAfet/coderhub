/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function getPrimesBetween(a, b) {
	if (a < 2) {
		a = 2;
	}
	if (b < a) {
		return [];
	}

	let primes = [];

	for (let num = a; num <= b; num++) {
		let is_prime = true;

		for (let i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				is_prime = false;
				break;
			}
		}

		if (is_prime) {
			primes.push(num);
		}
	}

	return primes;
}
