/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function coins_combinations(amount, coins) {
	if (amount == 0) return 1;
	if (amount < 0) return 0;
	if (coins.length == 0) return 0;
	return coins_combinations(amount - coins[0], coins) + coins_combinations(amount, coins.slice(1));
}
