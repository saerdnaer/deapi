import { openBlock as i, createElementBlock as a, withModifiers as l, toDisplayString as e } from 'vue';
var n = {
	props: { value: String },
	methods: {
		handleMailLink() {
			window.open('mailto:' + this.value);
		},
	},
};
(n.render = function (n, s, o, r, t, p) {
	return i(), a('a', { class: 'display-email-link', onClick: s[0] || (s[0] = l((i) => p.handleMailLink(), ['stop'])) }, e(o.value), 1);
}),
	(n.__file = 'src/display.vue');
var s = {
	id: 'display-email-link',
	name: 'Email-Link',
	description: 'Display as a clickable email-link',
	icon: 'link',
	component: n,
	types: ['string'],
};
export { s as default };
