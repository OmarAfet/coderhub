/*

Creator: OmarAfet
https://profile.satr.codes/OmarAfet/public/overview
https://github.com/OmarAfet

*/

function hashtag_it(my_array) {
	let hashtags = [];
	for (let i = 0; i < my_array.length; i++) {
		hashtags.push("#" + my_array[i]);
	}
	return hashtags.join(" ");
}
