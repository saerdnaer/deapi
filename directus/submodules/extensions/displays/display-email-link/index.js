import{openBlock as i,createElementBlock as l,withModifiers as n,toDisplayString as a}from"vue";var e={id:"display-email-link",name:"Email-Link",description:"Display as a clickable email-link",icon:"link",component:((i,l)=>{const n=i.__vccOpts||i;for(const[i,a]of l)n[i]=a;return n})({props:{value:String},methods:{handleMailLink(){window.open("mailto:"+this.value)}}},[["render",function(e,o,s,t,r,p){return i(),l("a",{class:"display-email-link",onClick:o[0]||(o[0]=n((i=>p.handleMailLink()),["stop"]))},a(s.value),1)}],["__file","display.vue"]]),types:["string"]};export{e as default};
