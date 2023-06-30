import { openBlock as i, createElementBlock as n, withModifiers as e, toDisplayString as a } from 'vue';
var l = {
	props: { value: String },
	methods: {
		handleLink() {
			window.open(this.value);
		},
	},
};
(l.render = function (l, s, o, r, p, t) {
	return i(), n('a', { class: 'display-link', onClick: s[0] || (s[0] = e((i) => t.handleLink(), ['stop'])) }, a(o.value), 1);
}),
	(l.__file = 'src/display.vue');
var s = { id: 'display-link', name: 'Link', description: 'Display as a clickable link', icon: 'link', component: l, types: ['string', 'text'] };
export { s as default };
