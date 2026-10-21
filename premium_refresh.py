from pathlib import Path
p=Path.home()/'Projects'/'hortifruti-bom-preco-pages'/'index.html'
s=p.read_text(encoding='utf-8')
style="""
/* Premium refresh — Hortifruti Bom Preço */
:root{--verde-profund:#103d20;--laranja:#f47a13}
html{scroll-behavior:smooth;scroll-padding-top:96px}
body{background:linear-gradient(180deg,#fffdf7 0%,#f7f9ef 55%,#fffdf8 100%)}
.topbar{backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:0 8px 30px rgba(16,61,32,.08)}
.hero{background:radial-gradient(ellipse at 85% 22%,rgba(244,122,19,.16),transparent 36%),radial-gradient(ellipse at 0% 85%,rgba(105,181,47,.12),transparent 46%);isolation:isolate}
.hero h1{font-size:clamp(2.6rem,6vw,5.2rem);line-height:1.06;letter-spacing:-.055em;text-wrap:balance}
.hero h1 em{background:linear-gradient(100deg,#e86b0b,#ff9d2c);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.hero .lead{max-width:54ch;line-height:1.75}
.hero-visual .photo-card{filter:drop-shadow(0 25px 38px rgba(17,61,30,.14))}
.btn{transition:transform .22s ease,box-shadow .22s ease,background .22s ease;min-height:46px}
.btn-primary{box-shadow:0 12px 26px rgba(29,103,45,.2)}
.btn:hover{transform:translateY(-3px)}
#ofertas{position:relative;background:linear-gradient(150deg,#f2f8e8 0%,#fff9ed 65%,#ffffff 100%)}
#ofertas .section-head h2,#galeria .section-head h2{letter-spacing:-.035em}
.card{border:1px solid rgba(31,94,48,.12);box-shadow:0 12px 30px rgba(16,61,32,.07);transition:transform .3s ease,box-shadow .3s ease}
.card:hover{box-shadow:0 20px 48px rgba(16,61,32,.17)}
.card .ph img{transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.card:hover .ph img{transform:scale(1.045)}
#gal button img{transition:transform .45s ease,filter .45s ease}
#gal button:hover img{transform:scale(1.045);filter:saturate(1.12)}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #f47a13;outline-offset:3px}
.premium-ribbon{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap;margin:0 0 1.1rem;font-size:.76rem;font-weight:800;text-transform:uppercase;letter-spacing:.11em;color:#246a35}
.premium-ribbon:before{content:'';display:inline-block;width:22px;height:3px;border-radius:3px;background:#f47a13}
.fresh-divider{height:5px;background:linear-gradient(90deg,#1c6532,#81b935,#f47a13);border-radius:99px;margin:1.6rem 0;max-width:132px}
@media(max-width:640px){.hero h1{font-size:clamp(2.35rem,10vw,3.1rem)}.hero{padding-top:110px}.hero-ctas .btn{flex:1 1 150px;text-align:center}.hero-visual{min-height:310px}.premium-ribbon{font-size:.68rem}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn,.card,.card .ph img,#gal button img{transition:none!important}}
"""
s=s.replace('</style>',style+'\n</style>',1)
s=s.replace('<h1>Frescor e economia', '<div class="premium-ribbon">Direto do Campo Largo para sua mesa</div>\n<h1>Frescor e economia',1)
s=s.replace('<div class="hero-ctas">','<div class="fresh-divider" aria-hidden="true"></div>\n<div class="hero-ctas">',1)
p.write_text(s,encoding='utf-8')
print('UPDATED',p,len(s),s.count('premium-ribbon'))
