/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function getBiggestShared(a, b) {
	a = a.sort((a, b) => a - b);
	b = b.sort((a, b) => a - b);
	z = [];
	for (let i = 0; i < a.length; i++) {
		const x = a[i];
		for (let j = 0; j < b.length; j++) {
			const y = b[j];
			if (x == y) {
				z.push(x);
			}
		}
	}
	return z.sort((a, b) => a - b).pop();
}
