import { useStores as e, defineDisplay as t } from '@directus/extensions-sdk';
import {
	computed as n,
	defineComponent as o,
	resolveComponent as a,
	resolveDirective as i,
	openBlock as l,
	createBlock as r,
	createElementBlock as c,
	withDirectives as u,
	resolveDynamicComponent as d,
	unref as p,
	withCtx as s,
	createElementVNode as v,
	normalizeClass as y,
	toDisplayString as f,
	withModifiers as h,
	createCommentVNode as m,
	createVNode as k,
} from 'vue';
import { useI18n as g } from 'vue-i18n';
const b = { key: 1, class: 'action-display' },
	_ = ['href'];
var w = o({
		__name: 'display',
		props: {
			value: { type: String, default: null },
			type: { type: String, required: !0 },
			interfaceOptions: { type: Object, default: {} },
			contentType: { type: String, default: 'other' },
			clickAction: { type: String, default: 'default' },
			showCopy: { type: Boolean, default: !1 },
			showLink: { type: Boolean, default: !1 },
		},
		setup(t) {
			const o = t,
				{ isCopySupported: w, copyToClipboard: x } = (function () {
					const { t: e } = g();
					return {
						isCopySupported: n(() => {
							var e;
							return !!(null === (e = null === navigator || void 0 === navigator ? void 0 : navigator.clipboard) || void 0 === e
								? void 0
								: e.writeText);
						}),
						isPasteSupported: n(() => {
							var e;
							return !!(null === (e = null === navigator || void 0 === navigator ? void 0 : navigator.clipboard) || void 0 === e
								? void 0
								: e.readText);
						}),
						copyToClipboard: async function (t, n, o) {
							var a, i, l;
							try {
								return (
									await (null === (a = null === navigator || void 0 === navigator ? void 0 : navigator.clipboard) || void 0 === a
										? void 0
										: a.writeText(t)),
									n.add({ title: null !== (i = null == o ? void 0 : o.success) && void 0 !== i ? i : e('copy_raw_value_success') }),
									!0
								);
							} catch (t) {
								return (
									n.add({
										type: 'error',
										title: null !== (l = null == o ? void 0 : o.fail) && void 0 !== l ? l : e('copy_raw_value_fail'),
									}),
									!1
								);
							}
						},
						pasteFromClipboard: async function (t, n) {
							var o, a, i;
							try {
								const i = await (null === (o = null === navigator || void 0 === navigator ? void 0 : navigator.clipboard) || void 0 === o
									? void 0
									: o.readText());
								return (
									t.add({ title: null !== (a = null == n ? void 0 : n.success) && void 0 !== a ? a : e('paste_raw_value_success') }), i
								);
							} catch (o) {
								return (
									t.add({
										type: 'error',
										title: null !== (i = null == n ? void 0 : n.fail) && void 0 !== i ? i : e('paste_raw_value_fail'),
									}),
									null
								);
							}
						},
					};
				})(),
				{ useNotificationsStore: C } = e(),
				T = C();
			async function A() {
				await x(o.value, T);
			}
			function S(e) {
				'copy' === o.clickAction && (e.stopPropagation(), A());
			}
			const O = n(() => 'default' !== o.clickAction && (!('copy' !== o.clickAction || !w) || 'link' === o.clickAction)),
				{ computedLink: D } = (function (e) {
					return {
						computedLink: n(() =>
							'url' === e.contentType
								? e.value
								: 'email' === e.contentType
								? `mailto:${e.value}`
								: 'phone' === e.contentType
								? `tel:${e.value}`
								: e.value,
						),
					};
				})(o),
				L = n(() => ('copy' === o.clickAction && w ? 'Copy value' : 'link' === o.clickAction ? 'Open link' : void 0));
			return (e, n) => {
				const o = a('value-null'),
					g = a('v-icon'),
					x = i('tooltip');
				return t.value
					? (l(),
					  c('span', b, [
							u(
								(l(),
								r(
									d('link' === t.clickAction ? 'a' : 'span'),
									{ class: 'dynamic-wrapper', href: p(D) },
									{ default: s(() => [v('span', { class: y(p(O) ? 'action-background' : ''), onClick: S }, f(t.value), 3)]), _: 1 },
									8,
									['href'],
								)),
								[[x, p(L)]],
							),
							t.showCopy && p(w)
								? u((l(), r(g, { key: 0, name: 'content_copy', right: '', onClick: h(A, ['stop']) }, null, 8, ['onClick'])), [
										[x, `Copy to clipboard: ${t.value}`],
								  ])
								: m('v-if', !0),
							t.showLink
								? u(
										(l(),
										c(
											'a',
											{ key: 1, href: p(D), target: '_blank', rel: 'noopener noreferrer', onClick: n[0] || (n[0] = h(() => {}, ['stop'])) },
											[k(g, { name: 'open_in_new', right: '' })],
											8,
											_,
										)),
										[[x, `Follow link: ${p(D)}`]],
								  )
								: m('v-if', !0),
					  ]))
					: (l(), r(o, { key: 0 }));
			};
		},
	}),
	x = [],
	C = [];
function T(e) {
	const t = [
		{ text: 'Other', value: 'other' },
		{ text: 'Phone', value: 'phone' },
	];
	return e && t.push({ text: 'URL', value: 'url' }, { text: 'E-Mail', value: 'email' }), t;
}
function A(e) {
	const t = [
		{ text: 'Copy to clipboard', value: 'copy' },
		{ text: 'Default click action', value: 'default' },
	];
	return e && t.push({ text: 'Open link', value: 'link' }), t;
}
!(function (e, t) {
	if (e && 'undefined' != typeof document) {
		var n,
			o = !0 === t.prepend ? 'prepend' : 'append',
			a = !0 === t.singleTag,
			i = 'string' == typeof t.container ? document.querySelector(t.container) : document.getElementsByTagName('head')[0];
		if (a) {
			var l = x.indexOf(i);
			-1 === l && ((l = x.push(i) - 1), (C[l] = {})), (n = C[l] && C[l][o] ? C[l][o] : (C[l][o] = r()));
		} else n = r();
		65279 === e.charCodeAt(0) && (e = e.substring(1)),
			n.styleSheet ? (n.styleSheet.cssText += e) : n.appendChild(document.createTextNode(e));
	}
	function r() {
		var e = document.createElement('style');
		if ((e.setAttribute('type', 'text/css'), t.attributes))
			for (var n = Object.keys(t.attributes), a = 0; a < n.length; a++) e.setAttribute(n[a], t.attributes[n[a]]);
		var l = 'prepend' === o ? 'afterbegin' : 'beforeend';
		return i.insertAdjacentElement(l, e), e;
	}
})(
	'.action-display[data-v-900f700e] .v-icon {\n  --v-icon-size: 18px;\n  --v-icon-color: var(--border-normal-alt);\n}\n.action-display[data-v-900f700e] .v-icon:hover {\n  --v-icon-color: var(--primary);\n}\n.action-display .action-background[data-v-900f700e] {\n  background-color: var(--primary-10);\n  padding: 0.5rem 1rem;\n  border-radius: 5rem;\n}\n.action-display .action-background[data-v-900f700e]:hover {\n  background-color: var(--primary-25);\n}',
	{},
),
	(w.__scopeId = 'data-v-900f700e'),
	(w.__file = 'src/display.vue');
var S = t({
	id: 'custom',
	name: 'Action display',
	icon: 'ads_click',
	description:
		'Display content with actions like linking or copy to clipboard. (By clicking on the content (only at readonly) and seperate buttons)! NOTE: the content needs to match the schema',
	component: w,
	types: ['uuid', 'string', 'text', 'bigInteger', 'integer', 'decimal', 'float'],
	options: ({ field: e }) => {
		var t;
		const n = ['string', 'text'].includes(null !== (t = e.type) && void 0 !== t ? t : 'unknown'),
			o = (function (e) {
				return [
					{
						field: 'contentType',
						name: 'Fields content type',
						type: 'string',
						meta: { width: 'full', interface: 'select-dropdown', options: { choices: T(e) } },
						schema: { default_value: 'other' },
					},
					{
						field: 'showCopy',
						name: 'Display copy icon',
						type: 'boolean',
						meta: { width: 'full', interface: 'boolean', options: { label: 'Display a copy button next to the item' } },
						schema: { default_value: !1 },
					},
					{
						field: 'showLink',
						name: 'Display link icon',
						type: 'boolean',
						meta: { width: 'full', interface: 'boolean', options: { label: 'Display a link button next to the item' } },
						schema: { default_value: !1 },
					},
				];
			})(n);
		return [
			...o,
			...[
				{
					field: 'clickAction',
					name: 'Click Action (when clicking on the value)',
					type: 'string',
					meta: { width: 'full', interface: 'select-dropdown', options: { choices: A(n) } },
					schema: { default_value: 'default' },
				},
			],
		];
	},
});
export { S as default };
