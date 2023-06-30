import { openBlock as e, createElementBlock as l, withModifiers as i, toDisplayString as n } from 'vue';
var a = {
	props: { value: String },
	methods: {
		handleTelLink() {
			window.open('tel:' + this.value);
		},
	},
};
(a.render = function (a, t, s, o, p, r) {
	return e(), l('a', { class: 'display-tel-link', onClick: t[0] || (t[0] = i((e) => r.handleTelLink(), ['stop'])) }, n(s.value), 1);
}),
	(a.__file = 'src/display.vue');
var t = {
	id: 'display-tel-link',
	name: 'Telephone-Link',
	description: 'Display as a clickable tel-link',
	icon: 'link',
	component: a,
	types: ['string'],
};
export { t as default };
