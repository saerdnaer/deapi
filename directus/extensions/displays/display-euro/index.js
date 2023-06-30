import { openBlock as e, createElementBlock as r, toDisplayString as u } from 'vue';
var a = { props: { value: Number } };
(a.render = function (a, o, n, t, l, i) {
	return e(), r('a', null, u(new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(n.value)), 1);
}),
	(a.__file = 'src/display.vue');
var o = {
	id: 'display-euro',
	name: 'Euro',
	description: 'Display euro values formatted',
	icon: 'euro',
	component: a,
	types: ['number', 'float', 'integer', 'decimal'],
};
export { o as default };
