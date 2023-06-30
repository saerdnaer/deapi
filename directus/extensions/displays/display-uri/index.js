import { openBlock as i, createElementBlock as n, withModifiers as e, toDisplayString as a } from 'vue';
// TODO: get list from namespaces table
const namespaces = {
	'wd:': 'http://www.wikidata.org/entity/',
}
var l = {
	props: { value: String },
	methods: {
		handleUri() {
			// open full URLs directly
			if (this.value.includes('//')) {
				window.open(this.value);
				return;
			}
			const uri = new URL(this.value);
			console.log(uri);
			if (uri.protocol in namespaces) {
				window.open(namespaces[uri.protocol] + uri.pathname);
				return;
			}
			window.open(this.value);
		},
	},
};
(l.render = function (l, s, o, r, p, t) {
	return i(), n('a', { class: 'display-link', onClick: s[0] || (s[0] = e((i) => t.handleUri(), ['stop'])) }, a(o.value), 1);
}),
	(l.__file = 'src/display.vue');
var s = { id: 'display-uri', name: 'URI', description: 'Display ID as a clickable link', icon: 'link', component: l, types: ['string', 'text'] };
export { s as default };
