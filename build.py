import markdown, pathlib

ROOT = pathlib.Path(__file__).parent
SITE_NAME = "Influvia"
DOMAIN = "https://influvia.app"  # alan adı netleşince değişir
SUPPORT = "destek@moonnect.com"
PLAY_URL = "https://play.google.com/store/apps/details?id=com.moonnect.app"
LANDMASK = (ROOT / "content" / "landmask.txt").read_text().strip()

FONTCSS = """@font-face{font-family:"Instrument Serif";font-style:italic;font-weight:400;font-display:swap;src:url("{FP}assets/fonts/instrument-serif-latin-ext-400-italic.woff2") format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Instrument Serif";font-style:italic;font-weight:400;font-display:swap;src:url("{FP}assets/fonts/instrument-serif-latin-400-italic.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Instrument Serif";font-style:normal;font-weight:400;font-display:swap;src:url("{FP}assets/fonts/instrument-serif-latin-ext-400-normal.woff2") format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Instrument Serif";font-style:normal;font-weight:400;font-display:swap;src:url("{FP}assets/fonts/instrument-serif-latin-400-normal.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Inter";font-style:normal;font-weight:400;font-display:swap;src:url("{FP}assets/fonts/inter-latin-ext-400-normal.woff2") format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Inter";font-style:normal;font-weight:400;font-display:swap;src:url("{FP}assets/fonts/inter-latin-400-normal.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Inter";font-style:normal;font-weight:500;font-display:swap;src:url("{FP}assets/fonts/inter-latin-ext-500-normal.woff2") format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Inter";font-style:normal;font-weight:500;font-display:swap;src:url("{FP}assets/fonts/inter-latin-500-normal.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Inter";font-style:normal;font-weight:600;font-display:swap;src:url("{FP}assets/fonts/inter-latin-ext-600-normal.woff2") format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Inter";font-style:normal;font-weight:600;font-display:swap;src:url("{FP}assets/fonts/inter-latin-600-normal.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}"""

CSS = """
:root{--bg:#050507;--bg2:#0b0b10;--text:#F4F4F7;--dim:#A3A3AF;--dim2:#6E6E7A;--mint:#00CC88;--teal:#1FD1C2;--violet:#6D4AFF;--violet2:#8B6DFF;--line:rgba(255,255,255,.09);--line2:rgba(255,255,255,.16)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}img,video{max-width:100%;display:block}
.serif{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
::selection{background:rgba(109,74,255,.45)}

/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:18px 32px;pointer-events:none}
.nav>*{pointer-events:auto;position:relative}
.nav:before{content:'';position:absolute;left:0;right:0;top:0;height:150%;background:linear-gradient(to bottom,rgba(5,5,7,.92),rgba(5,5,7,.55) 55%,rgba(5,5,7,0));pointer-events:none;z-index:-1}
.logo{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:var(--text);font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:27px;letter-spacing:-.01em}
.logo img{width:30px;height:30px;border-radius:8px}
.pill{display:flex;gap:2px;padding:5px;border-radius:999px;background:rgba(20,20,26,.72);border:1px solid var(--line2);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.pill a{padding:9px 18px;border-radius:999px;font-size:14px;color:#D4D4DC;text-decoration:none;transition:background .2s,color .2s;white-space:nowrap}
.pill a:hover{color:#fff;background:rgba(255,255,255,.07)}
.pill a.on{background:#fff;color:#0b0b10;font-weight:500}
.nav .right{justify-self:end}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:14px 26px;border-radius:999px;font-weight:500;font-size:15px;text-decoration:none;color:#fff;background:var(--violet);box-shadow:0 0 0 1px rgba(255,255,255,.06) inset,0 12px 40px rgba(109,74,255,.35);transition:transform .2s,background .2s,box-shadow .2s;border:0;cursor:pointer;font-family:inherit}
.btn:hover{background:var(--violet2);transform:translateY(-1px);box-shadow:0 16px 50px rgba(109,74,255,.45)}
.btn.white{background:#fff;color:#0b0b10;box-shadow:none;padding:10px 18px;font-size:14px}
.btn.white:hover{background:#e9e9ef}
.btn.ghost{background:transparent;border:1px solid var(--line2);box-shadow:none;color:var(--text)}
.btn.ghost:hover{background:rgba(255,255,255,.06);box-shadow:none}
.bnav{display:none}

/* globe */
#globe{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}

/* hero */
.hero{position:relative;z-index:1;min-height:100svh;display:flex;flex-direction:column;justify-content:space-between;padding:150px 0 40px}
.hero h1{margin:0;text-align:center;line-height:.92;font-weight:400;font-size:clamp(54px,9.4vw,138px);letter-spacing:-.02em}
.hero h1 .l1{display:block;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400}
.hero h1 .l2{display:block;font-family:Inter,sans-serif;font-weight:500;letter-spacing:-.045em;font-size:.92em}
.hero .sub{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:end;margin-top:auto;padding-top:60px}
.hero .sub p{margin:0;max-width:380px;color:#D9D9E0;font-size:16px;line-height:1.65}
.hero .sub .r{justify-self:end;text-align:right;display:flex;flex-direction:column;align-items:flex-end;gap:20px}
.hero .sub .r p{text-align:left}
.cta{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.soon{font-size:13px;color:var(--dim)}
.scrollhint{position:absolute;left:50%;bottom:18px;transform:translateX(-50%);width:46px;height:26px;border-radius:999px;border:1px solid var(--line2);background:rgba(20,20,26,.6);display:flex;align-items:center;justify-content:center;gap:3px}
.scrollhint i{display:block;width:2px;height:8px;background:#bbb;border-radius:2px;animation:eq 1.2s infinite ease-in-out}
.scrollhint i:nth-child(2){animation-delay:.2s;height:12px}.scrollhint i:nth-child(3){animation-delay:.4s}
@keyframes eq{0%,100%{transform:scaleY(.5)}50%{transform:scaleY(1.2)}}

/* content over globe */
#content{position:relative;z-index:1;background:linear-gradient(to bottom,rgba(5,5,7,0) 0,var(--bg) 220px);padding-top:120px}
section{padding:110px 0}
.h2{margin:0 0 18px;text-align:center;line-height:.95;font-weight:400;font-size:clamp(42px,6vw,84px);letter-spacing:-.02em}
.h2 .l1{display:block;font-family:"Instrument Serif",Georgia,serif;font-style:italic}
.h2 .l2{display:block;font-family:Inter,sans-serif;font-weight:500;letter-spacing:-.045em;font-size:.9em}
.lead{color:var(--dim);max-width:560px;margin:0 auto 64px;text-align:center;font-size:16px}
.eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--violet2);font-weight:600}

.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;text-align:center;padding:40px 0 0}
.stats b{display:block;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(48px,6vw,78px);line-height:1;letter-spacing:-.02em}
.stats span{display:block;margin-top:12px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim)}
.quote{max-width:820px;margin:96px auto 0;text-align:center;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:clamp(26px,3.4vw,40px);line-height:1.25;letter-spacing:-.01em}
.quote small{display:block;margin-top:22px;font-family:Inter,sans-serif;font-style:normal;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim2)}

.rows{border-top:1px solid var(--line);margin-top:20px}
.row{display:grid;grid-template-columns:220px 1fr 150px;gap:28px;align-items:baseline;padding:30px 0;border-bottom:1px solid var(--line)}
.row .n{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:30px;letter-spacing:-.01em;line-height:1.1}
.row p{margin:0;color:var(--dim);font-size:15.5px}
.row .t{text-align:right;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--violet2);font-weight:600}

.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{border:1px solid var(--line);border-radius:24px;padding:30px 30px 34px;background:linear-gradient(180deg,rgba(255,255,255,.025),rgba(255,255,255,0));transition:border-color .25s,transform .25s}
.card:hover{border-color:var(--line2);transform:translateY(-2px)}
.card .eyebrow{display:block;margin-bottom:22px}
.card h3{margin:0 0 10px;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:32px;line-height:1.05;letter-spacing:-.01em}
.card p{margin:0;color:var(--dim);font-size:15px}

.shots{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:10px}
.shot{border-radius:26px;overflow:hidden;border:1px solid var(--line);background:#0b0b10;box-shadow:0 30px 80px rgba(0,0,0,.6);transition:transform .35s}
.shot:hover{transform:translateY(-6px)}
.shot img{width:100%;height:auto}
.shots figure{margin:0}.shots figcaption{margin-top:12px;text-align:center;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim2)}

.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.plan{position:relative;border:1px solid var(--line);border-radius:26px;padding:34px 30px 30px;display:flex;flex-direction:column;background:rgba(255,255,255,.015)}
.plan.hi{border-color:rgba(109,74,255,.7);background:radial-gradient(120% 90% at 50% 0%,rgba(109,74,255,.22),rgba(109,74,255,.04) 60%,rgba(0,0,0,0))}
.plan .tag{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--violet);color:#fff;font-size:11px;letter-spacing:.2em;text-transform:uppercase;font-weight:600;padding:7px 16px;border-radius:999px;white-space:nowrap}
.plan .eyebrow{display:block;margin-bottom:26px}
.plan .price{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:56px;line-height:1;letter-spacing:-.02em}
.plan .price small{font-family:Inter,sans-serif;font-style:normal;font-size:15px;color:var(--dim);margin-left:8px;letter-spacing:0}
.plan .d{color:var(--dim);font-size:15px;margin:18px 0 22px;min-height:48px}
.plan ul{list-style:none;margin:0 0 30px;padding:0;display:grid;gap:12px;font-size:15px}
.plan li{display:flex;gap:14px}.plan li:before{content:"—";color:var(--violet2)}
.plan .btn{margin-top:auto;width:100%}

.faq{max-width:900px;margin:0 auto;border-top:1px solid var(--line)}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;padding:28px 44px 28px 0;position:relative;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:26px;letter-spacing:-.01em;line-height:1.2}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"";position:absolute;right:6px;top:50%;width:10px;height:10px;border-right:1.5px solid var(--dim);border-bottom:1.5px solid var(--dim);transform:translateY(-70%) rotate(45deg);transition:transform .25s}
.faq details[open] summary:after{transform:translateY(-30%) rotate(-135deg)}
.faq .a{padding:0 0 28px;color:var(--dim);font-size:16px;max-width:760px}
.faq .a a{color:var(--text)}

#cta{position:relative;z-index:1;min-height:92svh;display:flex;flex-direction:column;align-items:center;text-align:center;padding:150px 28px 0}
#cta .h2{font-size:clamp(52px,8vw,120px)}
#cta p{color:#D9D9E0;max-width:440px;margin:22px auto 34px}

footer{position:relative;z-index:1;background:var(--bg);border-top:1px solid var(--line);padding:56px 0 40px;font-size:14px;color:var(--dim)}
footer .top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:32px}
footer h4{margin:0 0 16px;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--violet2);font-weight:600}
footer ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
footer a{color:var(--dim);text-decoration:none}footer a:hover{color:#fff}
footer .tag{margin-top:12px;max-width:280px;color:var(--dim2)}
footer .bottom{margin-top:48px;padding-top:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;color:var(--dim2);font-size:13px}

/* docs */
.doc{position:relative;z-index:1;max-width:760px;margin:0 auto;padding:150px 24px 100px;background:var(--bg)}
.doc h1{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(40px,6vw,64px);letter-spacing:-.02em;line-height:1;margin:0 0 10px}
.doc h2{font-size:22px;margin:40px 0 10px;font-weight:600;letter-spacing:-.02em}.doc h3{font-size:17px;margin:26px 0 8px;font-weight:600}
.doc p,.doc li{color:#CFCFD8;font-size:16px}.doc ul,.doc ol{padding-left:22px}
.doc table{border-collapse:collapse;width:100%;font-size:14px}.doc td,.doc th{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
.doc strong{color:var(--text)}.doc a{color:var(--text)}
.docpage #globe{opacity:.35}

/* reveal */
.rv{opacity:0;transform:translateY(26px);filter:blur(6px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1),filter .9s}
.rv.in{opacity:1;transform:none;filter:none}
.rv.d1{transition-delay:.08s}.rv.d2{transition-delay:.16s}.rv.d3{transition-delay:.24s}.rv.d4{transition-delay:.32s}.rv.d5{transition-delay:.4s}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;filter:none;transition:none}}

@media(max-width:1000px){
 .nav{grid-template-columns:1fr auto;padding:14px 18px}.pill{display:none}
 .bnav{display:flex;position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:40;gap:2px;padding:5px;border-radius:999px;background:rgba(20,20,26,.82);border:1px solid var(--line2);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
 .bnav a{padding:9px 14px;border-radius:999px;font-size:13px;color:#D4D4DC;text-decoration:none;white-space:nowrap}.bnav a.on{background:#fff;color:#0b0b10}
 .hero{padding:120px 0 90px}.hero .sub{grid-template-columns:1fr;gap:24px}.hero .sub .r{justify-self:start;align-items:flex-start}
 .stats{grid-template-columns:repeat(2,1fr);gap:36px 16px}
 .row{grid-template-columns:1fr;gap:6px;padding:24px 0}.row .t{text-align:left;order:-1}
 .cards,.plans{grid-template-columns:1fr}
 .shots{grid-template-columns:repeat(5,72vw);overflow-x:auto;scroll-snap-type:x mandatory;padding:0 0 12px;margin:0 -28px;padding-left:28px;scrollbar-width:none}
 .shots::-webkit-scrollbar{display:none}.shots figure{scroll-snap-align:start}
 footer .top{grid-template-columns:1fr 1fr}
 section{padding:80px 0}.faq summary{font-size:22px}
 footer{padding-bottom:90px}
 #content{padding-top:30px}.hero{min-height:100svh;padding-bottom:70px}
}
@media(min-width:1001px) and (max-width:1200px){.shots{grid-template-columns:repeat(5,1fr)}}
"""

JS = """
(function(){
 // reveal
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.08});
 document.querySelectorAll('.rv').forEach(function(el){io.observe(el)});
 // nav active
 var links=[].slice.call(document.querySelectorAll('.pill a[href^="#"],.bnav a[href^="#"]'));
 var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))}).filter(Boolean);
 function setActive(){var y=window.scrollY+innerHeight*.4,cur=null;secs.forEach(function(s){if(s.offsetTop<=y)cur=s.id});links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+cur)})}
 addEventListener('scroll',setActive,{passive:true});setActive();
 // hero fade
 var h=document.querySelector('.hero h1'),sub=document.querySelector('.hero .sub');
 function fade(){if(!h)return;var p=Math.min(1,scrollY/(innerHeight*.55));h.style.opacity=1-p;h.style.transform='translateY('+(-scrollY*.18)+'px)';h.style.filter='blur('+(p*10)+'px)';if(sub){sub.style.opacity=1-Math.min(1,scrollY/(innerHeight*.35))}}
 addEventListener('scroll',fade,{passive:true});fade();

 // globe
 var c=document.getElementById('globe');if(!c)return;var ctx=c.getContext('2d');
 var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 var MASK=atob('__MASK__'),W=240,H=120;
 function land(ix,iy){var i=iy*W+ix,b=MASK.charCodeAt(i>>3);return (b>>(7-(i&7)))&1}
 var pts=[];for(var iy=0;iy<H;iy++){var lat=(90-(iy+.5)*180/H)*Math.PI/180;var step=Math.max(1,Math.round(1/Math.max(.2,Math.cos(lat))));for(var ix=0;ix<W;ix+=step){if(land(ix,iy)){var lon=((ix+.5)*360/W-180)*Math.PI/180;pts.push([Math.cos(lat)*Math.cos(lon),Math.sin(lat),Math.cos(lat)*Math.sin(lon)])}}}
 var stars=[];for(var i=0;i<260;i++)stars.push([Math.random(),Math.random(),Math.random()*1.4+.3,Math.random()*6.28]);
 var dpr=Math.min(1.5,devicePixelRatio||1),vw,vh,cx,cy,R,rot=0,t=0,vis=true,run=true;
 function size(){vw=innerWidth;vh=innerHeight;c.width=vw*dpr;c.height=vh*dpr;c.style.width=vw+'px';c.style.height=vh+'px';ctx.setTransform(dpr,0,0,dpr,0,0);R=Math.min(vw*.31,vh*.5);if(vw<1000)R=Math.min(vw*.58,vh*.42);cx=vw/2;cy=vh*1.04;draw()}
 var tilt=-.38,cs=Math.cos(tilt),sn=Math.sin(tilt);
 function ring(front){ctx.save();ctx.translate(cx,cy);ctx.rotate(-.22);var rx=R*1.42,ry=R*.30;ctx.beginPath();if(front)ctx.ellipse(0,0,rx,ry,0,0,Math.PI);else ctx.ellipse(0,0,rx,ry,0,Math.PI,2*Math.PI);var g=ctx.createLinearGradient(-rx,0,rx,0);g.addColorStop(0,'rgba(109,74,255,'+(front?.0:.0)+')');g.addColorStop(.5,'rgba(139,109,255,'+(front?.55:.22)+')');g.addColorStop(1,'rgba(31,209,194,'+(front?.0:.0)+')');ctx.strokeStyle=g;ctx.lineWidth=front?7:5;ctx.lineCap='round';ctx.stroke();
  // comets
  for(var k=0;k<2;k++){var a=t*.5+k*Math.PI;var f=Math.sin(a)>0;if(f!==front)continue;var x=Math.cos(a)*rx,y=Math.sin(a)*ry;var gg=ctx.createRadialGradient(x,y,0,x,y,26);gg.addColorStop(0,'rgba(255,255,255,.95)');gg.addColorStop(.25,'rgba(190,175,255,.7)');gg.addColorStop(1,'rgba(139,109,255,0)');ctx.fillStyle=gg;ctx.beginPath();ctx.arc(x,y,26,0,6.29);ctx.fill();ctx.beginPath();ctx.strokeStyle='rgba(255,255,255,.9)';ctx.lineWidth=3;ctx.ellipse(0,0,rx,ry,0,a-.5,a);ctx.stroke()}
  ctx.restore()}
 function draw(){ctx.clearRect(0,0,vw,vh);
  // stars
  for(var i=0;i<stars.length;i++){var s=stars[i];var tw=.35+.65*Math.abs(Math.sin(t*.6+s[3]));ctx.fillStyle='rgba(200,205,255,'+(tw*.55)+')';ctx.fillRect(s[0]*vw,s[1]*vh,s[2],s[2])}
  // outer glow
  var g=ctx.createRadialGradient(cx,cy,R*.9,cx,cy,R*1.8);g.addColorStop(0,'rgba(109,74,255,.28)');g.addColorStop(.35,'rgba(31,209,194,.08)');g.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=g;ctx.fillRect(0,0,vw,vh);
  ring(false);
  // sphere body
  var sg=ctx.createRadialGradient(cx-R*.35,cy-R*.45,R*.1,cx,cy,R);sg.addColorStop(0,'#141a3a');sg.addColorStop(.55,'#0a0c22');sg.addColorStop(1,'#04050c');ctx.fillStyle=sg;ctx.beginPath();ctx.arc(cx,cy,R,0,6.29);ctx.fill();
  // rim
  var rg=ctx.createRadialGradient(cx,cy,R*.86,cx,cy,R*1.02);rg.addColorStop(0,'rgba(0,0,0,0)');rg.addColorStop(.85,'rgba(120,90,255,.35)');rg.addColorStop(1,'rgba(31,209,194,.55)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(cx,cy,R*1.02,0,6.29);ctx.fill();
  // dots
  var cr=Math.cos(rot),sr=Math.sin(rot);
  for(var i=0;i<pts.length;i++){var p=pts[i];var x=p[0]*cr+p[2]*sr,z=-p[0]*sr+p[2]*cr,y=p[1];var y2=y*cs-z*sn,z2=y*sn+z*cs;if(z2<0.02)continue;var sx=cx+x*R,sy=cy-y2*R;if(sy>vh+4)continue;var l=Math.pow(z2,.9);var d=(0.8+1.3*l)*(R/420+.5);
   var lit=Math.max(0,(x*-.5+y2*.6+z2*.62));var a=.25+.75*lit;
   ctx.fillStyle='rgba('+Math.round(120+100*(1-lit))+','+Math.round(215+40*lit)+','+Math.round(200+55*(1-lit))+','+a+')';ctx.fillRect(sx-d/2,sy-d/2,d,d)}
  // specular
  var hg=ctx.createRadialGradient(cx-R*.3,cy-R*.5,0,cx-R*.3,cy-R*.5,R*.9);hg.addColorStop(0,'rgba(120,255,220,.12)');hg.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=hg;ctx.beginPath();ctx.arc(cx,cy,R,0,6.29);ctx.fill();
  ring(true)}
 function loop(){if(run&&vis&&!reduce){rot+=.0022;t+=.016;draw()}requestAnimationFrame(loop)}
 addEventListener('resize',size);size();
 document.addEventListener('visibilitychange',function(){vis=!document.hidden});
 var hero=document.querySelector('.hero'),cta=document.getElementById('cta'),hv=true,cv=false;
 var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.target===hero)hv=e.isIntersecting;if(e.target===cta)cv=e.isIntersecting;run=hv||cv;c.style.opacity=run?1:0})},{threshold:0});
 if(hero)io2.observe(hero);if(cta)io2.observe(cta);else run=true;
 c.style.transition='opacity .6s';
 loop();
})();
""".replace("__MASK__", LANDMASK)

NAV_LINKS = [("#uygulama", "Uygulama"), ("#nasil", "Nasıl çalışır"), ("#ekranlar", "Ekranlar"), ("#kimler", "Kimler için"), ("#sss", "SSS")]

def shell(title, body, desc, path_prefix="", doc=False, og="assets/og.jpg"):
    home = path_prefix if path_prefix else ""
    pill = "".join(f'<a href="{home}{h}">{l}</a>' for h, l in NAV_LINKS)
    bnav = "".join(f'<a href="{home}{h}">{l}</a>' for h, l in NAV_LINKS[:3]) + f'<a href="{PLAY_URL}">İndir</a>'
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#050507">
<link rel="icon" type="image/png" href="{path_prefix}assets/favicon.png">
<link rel="apple-touch-icon" href="{path_prefix}assets/icon-192.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="Influvia">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{DOMAIN}/{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" as="font" type="font/woff2" href="{path_prefix}assets/fonts/instrument-serif-latin-ext-400-italic.woff2" crossorigin><link rel="preload" as="font" type="font/woff2" href="{path_prefix}assets/fonts/inter-latin-ext-500-normal.woff2" crossorigin>
<style>{FONTCSS.replace("{FP}", path_prefix)}{CSS}</style>
</head>
<body class="{'docpage' if doc else ''}">
<canvas id="globe" aria-hidden="true"></canvas>
<nav class="nav">
 <a class="logo" href="{home or './'}"><img src="{path_prefix}assets/icon-192.png" alt="">Influvia</a>
 <div class="pill">{pill}</div>
 <div class="right"><a class="btn white" href="{PLAY_URL}">Google Play</a></div>
</nav>
<div class="bnav">{bnav}</div>
{body}
<footer><div class="wrap">
 <div class="top">
  <div><a class="logo" href="{home or './'}"><img src="{path_prefix}assets/icon-192.png" alt="">Influvia</a><p class="tag">İçerik üreticileri için kampanya, teslim, ödeme ve performans — tek uygulamada.</p></div>
  <div><h4>Keşfet</h4><ul><li><a href="{home}#uygulama">Uygulama</a></li><li><a href="{home}#nasil">Nasıl çalışır</a></li><li><a href="{home}#kimler">Markalar için</a></li><li><a href="{PLAY_URL}">Google Play</a></li></ul></div>
  <div><h4>Şirket</h4><ul><li><a href="https://moonnect.com">Moonnect</a></li><li><a href="{path_prefix}destek/">Destek</a></li><li><a href="mailto:{SUPPORT}">{SUPPORT}</a></li></ul></div>
  <div><h4>Yasal</h4><ul><li><a href="{path_prefix}gizlilik/">Gizlilik Politikası</a></li><li><a href="{path_prefix}kullanim-kosullari/">Kullanım Koşulları</a></li><li><a href="{path_prefix}hesap-silme/">Hesap ve Veri Silme</a></li></ul></div>
 </div>
 <div class="bottom"><span>© 2026 Moonnect Digital, LLC · Sheridan, WY · İstanbul</span><span>Google Play, Google LLC'nin ticari markasıdır.</span></div>
</div></footer>
<script>{JS}</script>
</body></html>"""

INDEX = f"""
<header class="hero wrap">
 <h1><span class="l1">Etki yarat,</span><span class="l2">karşılığını al.</span></h1>
 <div class="sub">
  <p class="rv d2">Influvia, içerik üreticileri için tek uygulama: sana açık marka kampanyalarını gör, tek dokunuşla başvur, içeriğini teslim et, ödemeni takip et.</p>
  <div class="r rv d3">
   <p>Instagram'ını bağla; büyümen gerçek verilerle ölçülsün, Influvia Skorun markaların önüne çıksın.</p>
   <div class="cta"><a class="btn" href="{PLAY_URL}">Google Play'den indir</a><span class="soon">App Store sürümü yakında</span></div>
  </div>
 </div>
 <div class="scrollhint" aria-hidden="true"><i></i><i></i><i></i></div>
</header>

<div id="content">
<section id="uygulama" class="wrap" style="padding-top:0">
 <div class="stats">
  <div class="rv"><b>₺0</b><span>Üreticiler için ücret</span></div>
  <div class="rv d1"><b>1</b><span>Dokunuşla başvuru</span></div>
  <div class="rv d2"><b>3</b><span>Ödül türü · ürün, ödeme, ikisi</span></div>
  <div class="rv d3"><b>100</b><span>Puanlık Influvia Skoru</span></div>
 </div>
 <p class="quote rv">"Markaya DM atıp günlerce cevap beklemek yok. Brief, teslim ve ödeme — hepsi tek yerde, hepsi takip edilebilir."<small>Influvia ne için var</small></p>
</section>

<section class="wrap">
 <h2 class="h2 rv"><span class="l1">Uygulamada</span><span class="l2">neler var</span></h2>
 <p class="lead rv d1">Bir markayla çalışmanın her adımı: keşfetten ödemeye, tek ekranda.</p>
 <div class="cards">
  <div class="card rv"><span class="eyebrow">01 — Keşif</span><h3>Kampanyalar</h3><p>Sana açık kampanyaları brief, ödül türü ve son teslim tarihiyle birlikte gör; tek dokunuşla başvur.</p></div>
  <div class="card rv d1"><span class="eyebrow">02 — Süreç</span><h3>Teslim ve ödeme</h3><p>Kabul edilince bildirim al, içerik linkini gönder, doğrulama ve ödeme durumunu uygulamadan izle.</p></div>
  <div class="card rv d2"><span class="eyebrow">03 — Ölçüm</span><h3>Influvia Skoru</h3><p>Instagram'ını bağla; takipçi büyümen, izlenme gelişimin ve paylaşım düzenin gerçek verilerden ölçülsün.</p></div>
  <div class="card rv"><span class="eyebrow">04 — Analiz</span><h3>Performans</h3><p>Reels performansını, en güçlü içeriklerini ve kitle dağılımını tek ekranda gör.</p></div>
  <div class="card rv d1"><span class="eyebrow">05 — Yapay zekâ</span><h3>İçerik analizi</h3><p>Galerinden bir görsel ya da video seç, paylaşmadan önce yapay zekâ destekli geri bildirim al.</p></div>
  <div class="card rv d2"><span class="eyebrow">06 — Gelişim</span><h3>Hedefler ve Akademi</h3><p>Haftalık hedefler koy, görevlerini takip et, Akademi içerikleriyle gelişmeye devam et.</p></div>
 </div>
</section>

<section id="nasil" class="wrap">
 <h2 class="h2 rv"><span class="l1">Nasıl</span><span class="l2">çalışır</span></h2>
 <p class="lead rv d1">Altı adım, tek uygulama. Her adımda nerede olduğunu görürsün.</p>
 <div class="rows">
  <div class="row rv"><div class="n">Keşfet</div><p>Sana açık kampanyaları brief, ödül türü ve son teslim tarihiyle gör.</p><div class="t">Adım 01</div></div>
  <div class="row rv"><div class="n">Başvur</div><p>Uygunsa tek dokunuşla başvur; kabul kararı bildirimle gelir.</p><div class="t">Adım 02</div></div>
  <div class="row rv"><div class="n">Üret</div><p>Brief'e uygun içeriğini hazırla; istersen paylaşmadan önce analiz ettir.</p><div class="t">Adım 03</div></div>
  <div class="row rv"><div class="n">Teslim et</div><p>Paylaştığın içeriğin linkini gönder; doğrulama başlasın.</p><div class="t">Adım 04</div></div>
  <div class="row rv"><div class="n">Ödemeni al</div><p>Doğrulama tamamlanınca ödeme süreci başlar; durumunu Bakiye ekranından izle.</p><div class="t">Adım 05</div></div>
  <div class="row rv"><div class="n">Büyü</div><p>Influvia Skoru ve performans ekranlarıyla nerede güçlendiğini gör, sonraki kampanyaya daha güçlü gir.</p><div class="t">Adım 06</div></div>
 </div>
</section>

<section id="ekranlar" class="wrap">
 <h2 class="h2 rv"><span class="l1">Uygulamadan</span><span class="l2">ekranlar</span></h2>
 <p class="lead rv d1">Karanlık, sade, hızlı. Her şey başparmağının altında.</p>
 <div class="shots">
  <figure class="rv"><div class="shot"><img src="assets/02-anasayfa.jpg" alt="Influvia ana sayfa" loading="lazy"></div><figcaption>Ana sayfa</figcaption></figure>
  <figure class="rv d1"><div class="shot"><img src="assets/01-kampanyalar.jpg" alt="Kampanya listesi" loading="lazy"></div><figcaption>Kampanyalar</figcaption></figure>
  <figure class="rv d2"><div class="shot"><img src="assets/03-kampanya-detay.jpg" alt="Kampanya detayı" loading="lazy"></div><figcaption>Kampanya detayı</figcaption></figure>
  <figure class="rv d3"><div class="shot"><img src="assets/05-performans.jpg" alt="Performans ve Influvia Skoru" loading="lazy"></div><figcaption>Performans</figcaption></figure>
  <figure class="rv d4"><div class="shot"><img src="assets/04-gorevler.jpg" alt="Görevler" loading="lazy"></div><figcaption>Görevler</figcaption></figure>
 </div>
</section>

<section id="kimler" class="wrap">
 <h2 class="h2 rv"><span class="l1">Kimler</span><span class="l2">için</span></h2>
 <p class="lead rv d1">Üreticiler için ücretsiz. Markalar ve ajanslar için birlikte kurguluyoruz.</p>
 <div class="plans">
  <div class="plan rv"><span class="eyebrow">Marka</span><div class="price">Kampanya aç</div><p class="d">Ürününü Moonnect'in üretici ağıyla buluştur; başvuruları ve teslimleri tek panelden yönet.</p>
   <ul><li>Brief ve ödül tanımı</li><li>Başvuru ve skor görünümü</li><li>İçerik doğrulama</li><li>Ödeme takibi</li></ul>
   <a class="btn ghost" href="mailto:{SUPPORT}?subject=Influvia%20-%20Marka%20i%C5%9F%20birli%C4%9Fi">Bize yaz</a></div>
  <div class="plan hi rv d1"><span class="tag">Uygulama</span><span class="eyebrow">İçerik üreticisi</span><div class="price">Ücretsiz<small>her zaman</small></div><p class="d">Kampanyalara başvurmak, içerik teslim etmek ve büyümeni ölçmek için.</p>
   <ul><li>Açık kampanyalar</li><li>Tek dokunuşla başvuru</li><li>Influvia Skoru ve performans</li><li>İçerik analizi, hedefler, Akademi</li></ul>
   <a class="btn" href="{PLAY_URL}">Google Play'den indir</a></div>
  <div class="plan rv d2"><span class="eyebrow">Ajans</span><div class="price">Birlikte</div><p class="d">Birden fazla marka ya da üreticiyle çalışıyorsan sana özel kurgu için görüşelim.</p>
   <ul><li>Birden fazla marka</li><li>Sana özel kampanya kurgusu</li><li>Raporlama</li><li>Öncelikli iletişim</li></ul>
   <a class="btn ghost" href="mailto:{SUPPORT}?subject=Influvia%20-%20Ajans">Görüşelim</a></div>
 </div>
</section>

<section id="sss" class="wrap">
 <h2 class="h2 rv"><span class="l1">Sık sorulan</span><span class="l2">sorular</span></h2>
 <div class="faq rv d1">
  <details><summary>Instagram'ımı bağlamak zorunda mıyım?</summary><div class="a">Hayır. Bağlantı isteğe bağlıdır; bağlarsan Influvia Skoru ve performans ekranları çalışır. Şifren hiçbir zaman Influvia'ya iletilmez, yetkiyi Instagram'ın kendi ekranından verirsin.</div></details>
  <details><summary>Influvia Skoru nasıl hesaplanıyor?</summary><div class="a">Takipçi büyümen, izlenme gelişimin, paylaşım düzenin ve izlenme istikrarın gibi gerçek ölçüm verilerinden. Yeterli geçmiş birikene kadar "ön sonuç" olarak gösterilir.</div></details>
  <details><summary>Uygulama ücretli mi?</summary><div class="a">İçerik üreticileri için ücretsiz. Uygulama içi satın alma ya da reklam yok.</div></details>
  <details><summary>Ödemem ne zaman yapılır?</summary><div class="a">Teslim ettiğin içerik doğrulandıktan sonra ödeme süreci başlar; durumunu uygulamadaki Ödemeler / Bakiye ekranından görebilirsin.</div></details>
  <details><summary>iPhone sürümü ne zaman?</summary><div class="a">Önce Android ile başlıyoruz; App Store sürümü hazırlanıyor. Çıktığında buradan ve uygulama içi bildirimle duyuracağız.</div></details>
  <details><summary>Hesabımı nasıl silerim?</summary><div class="a">Profil ekranının altındaki "Hesabımı Sil" ile anında silebilirsin. Ayrıntılar için <a href="hesap-silme/">Hesap ve veri silme</a> sayfasına bak.</div></details>
 </div>
</section>
</div>

<section id="cta">
 <h2 class="h2 rv"><span class="l1">Bugün</span><span class="l2">başla</span></h2>
 <p class="rv d1">Hesap açmak bir dakika sürer. İlk kampanyana bugün başvur, gerisini uygulama takip etsin.</p>
 <div class="cta rv d2" style="justify-content:center"><a class="btn" href="{PLAY_URL}">Google Play'den indir</a><a class="btn ghost" href="mailto:{SUPPORT}?subject=Influvia%20iOS%20haber%20ver">iOS çıkınca haber ver</a></div>
</section>
"""

(ROOT / "index.html").write_text(shell("Influvia — Etki yarat, karşılığını al", INDEX, "İçerik üreticileri için kampanya ve performans uygulaması. Marka kampanyalarına başvur, içerik teslim et, ödemeni takip et, Instagram büyümeni ölç."), encoding="utf-8")

def doc_page(md_name, out_dir, title, desc):
    text = (ROOT / "content" / md_name).read_text(encoding="utf-8")
    text = text.replace("influvia.io", "influvia.app")
    html = markdown.markdown(text, extensions=["tables"])
    body = f'<main class="doc">{html}</main>'
    (ROOT / out_dir).mkdir(exist_ok=True)
    (ROOT / out_dir / "index.html").write_text(shell(f"{title} — Influvia", body, desc, "../", doc=True), encoding="utf-8")

doc_page("gizlilik-politikasi.md", "gizlilik", "Gizlilik Politikası", "Influvia gizlilik politikası: hangi verileri işliyoruz, neden, ne kadar süreyle; Instagram verileri; haklarınız.")
doc_page("hesap-silme.md", "hesap-silme", "Hesap ve Veri Silme", "Influvia hesabınızı ve verilerinizi uygulama içinden veya e-postayla nasıl silersiniz.")
doc_page("kullanim-kosullari.md", "kullanim-kosullari", "Kullanım Koşulları", "Influvia kullanım koşulları.")

DESTEK = f"""
<main class="doc">
<h1>Destek</h1>
<p>Bir sorun mu var, öneri mi? Bize <a href="mailto:{SUPPORT}">{SUPPORT}</a> adresinden yaz; iş günlerinde genellikle 24 saat içinde dönüyoruz.</p>
<h2>Sık sorulanlar</h2>
<h3>Instagram'ımı bağlamak zorunda mıyım?</h3><p>Hayır. Bağlantı isteğe bağlıdır; bağlarsan Influvia Skoru ve performans ekranları çalışır. Şifren hiçbir zaman Influvia'ya iletilmez, yetkiyi Instagram'ın kendi ekranından verirsin.</p>
<h3>Influvia Skorum nasıl hesaplanıyor?</h3><p>Takipçi büyümen, izlenme gelişimin, paylaşım düzenin ve izlenme istikrarın gibi gerçek ölçüm verilerinden. Yeterli geçmiş birikene kadar "ön sonuç" olarak gösterilir.</p>
<h3>Ödemem ne zaman yapılır?</h3><p>Teslim ettiğin içerik doğrulandıktan sonra ödeme süreci başlar; durumunu uygulamadaki Ödemeler / Bakiye ekranından görebilirsin.</p>
<h3>Hesabımı nasıl silerim?</h3><p>Profil ekranının altındaki "Hesabımı Sil" ile anında silebilirsin. Ayrıntılar: <a href="../hesap-silme/">Hesap ve veri silme</a>.</p>
<h2>Şirket</h2>
<p>Influvia, Moonnect Digital, LLC (30 N. Gould St., Sheridan, WY 82801, ABD; İstanbul, Türkiye) tarafından geliştirilir.</p>
</main>
"""
(ROOT / "destek").mkdir(exist_ok=True)
(ROOT / "destek" / "index.html").write_text(shell("Destek — Influvia", DESTEK, "Influvia destek ve sık sorulan sorular.", "../", doc=True), encoding="utf-8")

(ROOT / "404.html").write_text(shell("Sayfa bulunamadı — Influvia", '<main class="doc"><h1>Sayfa bulunamadı</h1><p><a href="/">Ana sayfaya dön</a></p></main>', "Sayfa bulunamadı", doc=True), encoding="utf-8")
(ROOT / ".nojekyll").write_text("")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{DOMAIN}/{p}</loc></url>" for p in ["", "gizlilik/", "hesap-silme/", "kullanim-kosullari/", "destek/"]) + "</urlset>")
print("built")
