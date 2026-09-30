import markdown, pathlib

ROOT = pathlib.Path(__file__).parent
SITE_NAME = "Influvia"
DOMAIN = "https://influvia.app"  # alan adı netleşince değişir
SUPPORT = "destek@moonnect.com"
PLAY_URL = "https://play.google.com/store/apps/details?id=com.moonnect.app"

exec((ROOT / "fontcss.txt").read_text())  # FONTCSS = """..."""

ARROW = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h9M8.5 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
NOISE = "data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E"

CSS = """
:root{--bg:#050507;--bg2:#0b0b10;--text:#F4F4F7;--dim:#A3A3AF;--dim2:#6E6E7A;--mint:#00CC88;--teal:#1FD1C2;--violet:#6D4AFF;--violet2:#8B6DFF;--line:rgba(255,255,255,.08);--line2:rgba(255,255,255,.16);--ease:cubic-bezier(.2,.7,.2,1)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}img,video{max-width:100%;display:block}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
::selection{background:rgba(109,74,255,.45)}
.grain{position:fixed;inset:-50%;width:200%;height:200%;z-index:60;pointer-events:none;opacity:.045;mix-blend-mode:overlay;background:url("NOISE_URI");animation:grain 1.2s steps(3) infinite}
@keyframes grain{0%{transform:translate(0,0)}33%{transform:translate(-2%,1%)}66%{transform:translate(1%,-2%)}100%{transform:translate(0,0)}}

/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:18px 32px;pointer-events:none}
.nav>*{pointer-events:auto;position:relative}
.nav:before{content:'';position:absolute;left:0;right:0;top:0;height:170%;background:linear-gradient(to bottom,rgba(5,5,7,.9),rgba(5,5,7,.5) 55%,rgba(5,5,7,0));pointer-events:none}
.logo{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:var(--text);font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:27px;letter-spacing:-.01em}
.logo img{width:30px;height:30px;border-radius:9px;box-shadow:0 0 0 1px rgba(255,255,255,.1),0 6px 18px rgba(0,0,0,.5)}
.pill{display:flex;gap:2px;padding:5px;border-radius:999px;background:rgba(16,16,22,.66);border:1px solid var(--line2);backdrop-filter:blur(16px) saturate(140%);-webkit-backdrop-filter:blur(16px) saturate(140%);box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 10px 30px -10px rgba(0,0,0,.8)}
.pill a{padding:9px 18px;border-radius:999px;font-size:14px;color:#CFCFD8;text-decoration:none;transition:background .25s,color .25s;white-space:nowrap}
.pill a:hover{color:#fff;background:rgba(255,255,255,.07)}
.pill a.on{background:#fff;color:#0b0b10;font-weight:500;box-shadow:0 2px 10px rgba(0,0,0,.35)}
.nav .right{justify-self:end}
.bnav{display:none}

/* buttons */
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;height:52px;padding:0 26px;border-radius:999px;font-weight:500;font-size:15px;letter-spacing:-.01em;text-decoration:none;color:#fff;border:0;cursor:pointer;font-family:inherit;white-space:nowrap;isolation:isolate;overflow:hidden;
 background:linear-gradient(180deg,#8F72FF 0%,#6D4AFF 52%,#5A39EE 100%);
 box-shadow:inset 0 1px 0 rgba(255,255,255,.32),inset 0 -1px 0 rgba(0,0,0,.28),0 1px 2px rgba(0,0,0,.6),0 16px 40px -10px rgba(109,74,255,.7);
 transition:transform .3s var(--ease),box-shadow .3s var(--ease),filter .3s}
.btn:before{content:"";position:absolute;inset:0;background:linear-gradient(105deg,transparent 35%,rgba(255,255,255,.28) 50%,transparent 65%);transform:translateX(-130%);transition:transform .8s var(--ease);z-index:-1}
.btn:hover{transform:translateY(-2px);filter:saturate(1.08) brightness(1.04);box-shadow:inset 0 1px 0 rgba(255,255,255,.36),inset 0 -1px 0 rgba(0,0,0,.28),0 2px 4px rgba(0,0,0,.6),0 22px 50px -10px rgba(109,74,255,.85)}
.btn:hover:before{transform:translateX(130%)}
.btn:active{transform:translateY(0);filter:brightness(.97)}
.btn svg{width:16px;height:16px;flex:none;transition:transform .3s var(--ease)}
.btn:hover svg{transform:translateX(3px)}
.btn.ghost{background:rgba(255,255,255,.035);color:var(--text);border:1px solid rgba(255,255,255,.14);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 1px 2px rgba(0,0,0,.4)}
.btn.ghost:hover{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.28);filter:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 12px 30px -12px rgba(0,0,0,.8)}
.btn.ghost:before{background:linear-gradient(105deg,transparent 35%,rgba(255,255,255,.12) 50%,transparent 65%)}
.btn.white{background:linear-gradient(180deg,#FFFFFF,#E6E6EE);color:#0b0b10;height:40px;padding:0 18px;font-size:14px;box-shadow:inset 0 1px 0 #fff,inset 0 -1px 0 rgba(0,0,0,.08),0 1px 2px rgba(0,0,0,.5),0 10px 26px -10px rgba(255,255,255,.35)}
.btn.white:hover{filter:none;box-shadow:inset 0 1px 0 #fff,0 2px 4px rgba(0,0,0,.5),0 14px 30px -10px rgba(255,255,255,.45)}
.btn.white:before{background:linear-gradient(105deg,transparent 35%,rgba(109,74,255,.16) 50%,transparent 65%)}
.btn.sm{height:46px;padding:0 22px;font-size:14px}
.btn.block{width:100%}

/* hero */
.hero{position:relative;z-index:1;min-height:100svh;display:flex;flex-direction:column;justify-content:space-between;padding:150px 0 40px;overflow:hidden;isolation:isolate}
.hero .bg{position:absolute;inset:0;z-index:-2;overflow:hidden}
.hero .bg .media{position:absolute;left:50%;top:8vh;width:190vw;max-width:none;transform:translate3d(-50%,0,0);will-change:transform}
.hero .bg .media img,.hero .bg .media video{width:100%;height:auto}
.hero .bg .media video{position:absolute;inset:0;height:100%;object-fit:cover;opacity:0;transition:opacity 1.2s}
.hero .bg .media video.ready{opacity:1}
.hero .bg:before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(5,5,7,.55) 0%,rgba(5,5,7,.15) 28%,rgba(5,5,7,0) 48%,rgba(5,5,7,0) 62%,rgba(5,5,7,.5) 84%,rgba(5,5,7,.96) 100%)}
.hero .stars{position:absolute;inset:0;z-index:-1;background-image:radial-gradient(1px 1px at 12% 22%,rgba(255,255,255,.55),transparent 60%),radial-gradient(1px 1px at 78% 14%,rgba(255,255,255,.45),transparent 60%),radial-gradient(1.5px 1.5px at 62% 34%,rgba(200,210,255,.55),transparent 60%),radial-gradient(1px 1px at 30% 48%,rgba(255,255,255,.4),transparent 60%),radial-gradient(1px 1px at 88% 52%,rgba(255,255,255,.35),transparent 60%),radial-gradient(1.2px 1.2px at 46% 12%,rgba(255,255,255,.5),transparent 60%),radial-gradient(1px 1px at 8% 70%,rgba(255,255,255,.3),transparent 60%),radial-gradient(1px 1px at 94% 80%,rgba(255,255,255,.3),transparent 60%)}
.hero .wrap{position:relative;z-index:1;display:flex;flex-direction:column;flex:1}
.hero h1{margin:0;text-align:center;line-height:.9;font-weight:400;font-size:clamp(56px,9.6vw,144px);letter-spacing:-.025em;text-shadow:0 10px 60px rgba(0,0,0,.6)}
.hero h1 .l1{display:block;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400}
.hero h1 .l2{display:block;font-family:Inter,sans-serif;font-weight:500;letter-spacing:-.05em;font-size:.9em;margin-top:.02em}
.hero .kicker{display:flex;justify-content:center;margin-bottom:26px}
.chip{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 14px 0 8px;border-radius:999px;font-size:12.5px;color:#D9D9E0;background:rgba(16,16,22,.6);border:1px solid var(--line2);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.chip b{display:inline-flex;align-items:center;height:20px;padding:0 8px;border-radius:999px;background:linear-gradient(90deg,var(--mint),var(--teal));color:#05231a;font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.hero .sub{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:end;margin-top:auto;padding-top:60px}
.hero .sub p{margin:0;max-width:380px;color:#DADAE2;font-size:16px;line-height:1.65;text-shadow:0 2px 20px rgba(0,0,0,.8)}
.hero .sub .r{justify-self:end;display:flex;flex-direction:column;align-items:flex-end;gap:20px}
.cta{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.soon{font-size:13px;color:var(--dim)}
.scrollhint{position:absolute;left:50%;bottom:18px;transform:translateX(-50%);width:46px;height:26px;border-radius:999px;border:1px solid var(--line2);background:rgba(16,16,22,.6);display:flex;align-items:center;justify-content:center;gap:3px;z-index:2}
.scrollhint i{display:block;width:2px;height:8px;background:#bbb;border-radius:2px;animation:eq 1.2s infinite ease-in-out}
.scrollhint i:nth-child(2){animation-delay:.2s;height:12px}.scrollhint i:nth-child(3){animation-delay:.4s}
@keyframes eq{0%,100%{transform:scaleY(.5)}50%{transform:scaleY(1.2)}}

/* sections */
#content{position:relative;z-index:1;background:var(--bg)}
section{padding:120px 0;position:relative}
.eyebrow{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--violet2);font-weight:600}
.eyebrow.c{display:block;text-align:center;margin-bottom:22px}
.h2{margin:0 0 18px;text-align:center;line-height:.95;font-weight:400;font-size:clamp(44px,6.4vw,88px);letter-spacing:-.025em}
.h2 .l1{display:block;font-family:"Instrument Serif",Georgia,serif;font-style:italic}
.h2 .l2{display:block;font-family:Inter,sans-serif;font-weight:500;letter-spacing:-.05em;font-size:.9em}
.lead{color:var(--dim);max-width:560px;margin:0 auto 64px;text-align:center;font-size:16px}

.stats{display:grid;grid-template-columns:repeat(4,1fr);text-align:center;padding:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{padding:44px 16px;border-right:1px solid var(--line)}.stats>div:last-child{border-right:0}
.stats b{display:block;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(52px,6.4vw,84px);line-height:1;letter-spacing:-.02em;background:linear-gradient(180deg,#fff 30%,rgba(255,255,255,.55));-webkit-background-clip:text;background-clip:text;color:transparent}
.stats span{display:block;margin-top:14px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim)}
.quote{max-width:860px;margin:110px auto 0;text-align:center;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:clamp(28px,3.6vw,44px);line-height:1.22;letter-spacing:-.01em}
.quote small{display:block;margin-top:24px;font-family:Inter,sans-serif;font-style:normal;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim2)}

.rows{border-top:1px solid var(--line);margin-top:10px}
.row{display:grid;grid-template-columns:70px 220px 1fr 120px;gap:28px;align-items:baseline;padding:32px 12px;border-bottom:1px solid var(--line);border-radius:14px;transition:background .3s}
.row:hover{background:rgba(255,255,255,.025)}
.row .i{font-size:12px;letter-spacing:.18em;color:var(--dim2);font-variant-numeric:tabular-nums}
.row .n{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:32px;letter-spacing:-.01em;line-height:1.1}
.row p{margin:0;color:var(--dim);font-size:15.5px;max-width:560px}
.row .t{text-align:right;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--violet2);font-weight:600}

.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{position:relative;border-radius:26px;overflow:hidden;background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.008));transition:transform .5s var(--ease),box-shadow .5s var(--ease)}
.card:before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;background:linear-gradient(180deg,rgba(255,255,255,.2),rgba(255,255,255,.05) 45%,rgba(109,74,255,.35));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;z-index:2}
.card .glow{position:absolute;inset:0;border-radius:inherit;background:radial-gradient(360px circle at var(--mx,50%) var(--my,30%),rgba(109,74,255,.18),transparent 62%);opacity:0;transition:opacity .4s;pointer-events:none;z-index:1}
.card:hover{transform:translateY(-4px);box-shadow:0 30px 80px -30px rgba(0,0,0,.9),0 0 80px -40px rgba(109,74,255,.5)}
.card:hover .glow{opacity:1}
.card .vis{position:relative;aspect-ratio:4/3;overflow:hidden;background:#000}
.card .vis img{width:100%;height:100%;object-fit:cover;transform:scale(1.03);transition:transform 1.1s var(--ease)}
.card:hover .vis img{transform:scale(1.09)}
.card .vis:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,5,7,.15) 0%,rgba(5,5,7,0) 30%,rgba(5,5,7,0) 55%,rgba(5,5,7,.92) 100%)}
.card .body{position:relative;padding:2px 28px 32px;z-index:1}
.card .eyebrow{display:block;margin-bottom:14px}
.card h3{margin:0 0 10px;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:34px;line-height:1.02;letter-spacing:-.01em}
.card p{margin:0;color:var(--dim);font-size:15px}

.shots{display:grid;grid-template-columns:repeat(5,1fr);gap:22px;margin-top:20px;perspective:1600px;align-items:end}
.shots figure{margin:0}
.phone{position:relative;border-radius:42px;padding:9px;background:linear-gradient(180deg,#2b2b34 0%,#121217 40%,#0a0a0e 100%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14),inset 0 -1px 0 rgba(255,255,255,.05),0 50px 100px -30px rgba(0,0,0,.95),0 0 90px -40px rgba(109,74,255,.45);transition:transform .7s var(--ease),box-shadow .7s var(--ease)}
.phone .scr{position:relative;border-radius:34px;overflow:hidden;background:#000;aspect-ratio:764/1712}
.phone .scr img{width:100%;height:100%;object-fit:cover}
.phone .isl{position:absolute;top:18px;left:50%;transform:translateX(-50%);width:26%;height:20px;border-radius:999px;background:#000;box-shadow:0 0 0 1px rgba(255,255,255,.05);z-index:2}
.phone .scr:after{content:"";position:absolute;inset:0;border-radius:inherit;box-shadow:inset 0 0 0 1px rgba(255,255,255,.06);background:linear-gradient(115deg,rgba(255,255,255,.07) 0%,rgba(255,255,255,0) 32%);pointer-events:none}
.shots figure:nth-child(1) .phone{transform:rotateY(14deg) translateY(28px)}
.shots figure:nth-child(2) .phone{transform:rotateY(7deg) translateY(12px)}
.shots figure:nth-child(3) .phone{transform:translateY(-14px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16),0 60px 120px -30px rgba(0,0,0,1),0 0 120px -30px rgba(109,74,255,.6)}
.shots figure:nth-child(4) .phone{transform:rotateY(-7deg) translateY(12px)}
.shots figure:nth-child(5) .phone{transform:rotateY(-14deg) translateY(28px)}
.shots figure:hover .phone{transform:translateY(-22px) rotateY(0)}
.shots figcaption{margin-top:34px;text-align:center;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim2)}

#kimler{background:radial-gradient(60% 50% at 50% 0%,rgba(109,74,255,.09),transparent 70%)}
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.plan{position:relative;border-radius:28px;padding:36px 32px 32px;display:flex;flex-direction:column;background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,.008))}
.plan:before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;background:linear-gradient(180deg,rgba(255,255,255,.16),rgba(255,255,255,.05));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
.plan.hi{background:radial-gradient(120% 90% at 50% 0%,rgba(109,74,255,.26),rgba(109,74,255,.05) 55%,rgba(255,255,255,.01));box-shadow:0 40px 100px -40px rgba(109,74,255,.5)}
.plan.hi:before{background:linear-gradient(180deg,rgba(139,109,255,.9),rgba(109,74,255,.25) 60%,rgba(109,74,255,.5))}
.plan .tag{position:absolute;top:-15px;left:50%;transform:translateX(-50%);background:linear-gradient(180deg,#8F72FF,#6D4AFF);color:#fff;font-size:11px;letter-spacing:.2em;text-transform:uppercase;font-weight:600;padding:8px 16px;border-radius:999px;white-space:nowrap;box-shadow:inset 0 1px 0 rgba(255,255,255,.3),0 10px 30px -8px rgba(109,74,255,.8)}
.plan .eyebrow{display:block;margin-bottom:26px}
.plan .price{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:58px;line-height:1;letter-spacing:-.02em}
.plan .price small{font-family:Inter,sans-serif;font-style:normal;font-size:15px;color:var(--dim);margin-left:8px;letter-spacing:0}
.plan .d{color:var(--dim);font-size:15px;margin:18px 0 22px;min-height:48px}
.plan ul{list-style:none;margin:0 0 32px;padding:0;display:grid;gap:12px;font-size:15px}
.plan li{display:flex;gap:14px}.plan li:before{content:"—";color:var(--violet2)}
.plan .btn{margin-top:auto;width:100%}

.faq{max-width:900px;margin:0 auto;border-top:1px solid var(--line)}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;padding:30px 48px 30px 0;position:relative;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:27px;letter-spacing:-.01em;line-height:1.2;transition:color .3s}
.faq summary:hover{color:#fff}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"";position:absolute;right:8px;top:50%;width:11px;height:11px;border-right:1.5px solid var(--dim);border-bottom:1.5px solid var(--dim);transform:translateY(-70%) rotate(45deg);transition:transform .3s var(--ease)}
.faq details[open] summary:after{transform:translateY(-30%) rotate(-135deg)}
.faq .a{padding:0 0 30px;color:var(--dim);font-size:16px;max-width:760px}
.faq .a a{color:var(--text)}

#cta{position:relative;z-index:1;min-height:96svh;display:flex;flex-direction:column;align-items:center;text-align:center;padding:170px 28px 0;overflow:hidden;isolation:isolate}
#cta .planet{position:absolute;left:50%;top:30%;width:170vw;max-width:none;transform:translateX(-50%);z-index:-2}
#cta:before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,var(--bg) 0%,rgba(5,5,7,.6) 30%,rgba(5,5,7,0) 60%,rgba(5,5,7,.2) 100%)}
#cta .h2{font-size:clamp(56px,8.6vw,128px)}
#cta p{color:#DADAE2;max-width:440px;margin:22px auto 36px;text-shadow:0 2px 20px rgba(0,0,0,.8)}

footer{position:relative;z-index:1;background:var(--bg);border-top:1px solid var(--line);padding:64px 0 0;font-size:14px;color:var(--dim);overflow:hidden}
footer .top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:32px}
footer h4{margin:0 0 16px;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--violet2);font-weight:600}
footer ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
footer a{color:var(--dim);text-decoration:none;transition:color .2s}footer a:hover{color:#fff}
footer .tag{margin-top:14px;max-width:280px;color:var(--dim2)}
footer .bottom{margin-top:48px;padding-top:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;color:var(--dim2);font-size:13px}
footer .mark{margin:30px 0 -.12em;text-align:center;font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-size:clamp(120px,24vw,360px);line-height:.78;letter-spacing:-.03em;background:linear-gradient(180deg,rgba(255,255,255,.14),rgba(255,255,255,0) 85%);-webkit-background-clip:text;background-clip:text;color:transparent;user-select:none;pointer-events:none}

/* docs */
.doc{position:relative;z-index:1;max-width:760px;margin:0 auto;padding:150px 24px 100px}
.doc h1{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(40px,6vw,64px);letter-spacing:-.02em;line-height:1;margin:0 0 10px}
.doc h2{font-size:22px;margin:40px 0 10px;font-weight:600;letter-spacing:-.02em}.doc h3{font-size:17px;margin:26px 0 8px;font-weight:600}
.doc p,.doc li{color:#CFCFD8;font-size:16px}.doc ul,.doc ol{padding-left:22px}
.doc table{border-collapse:collapse;width:100%;font-size:14px}.doc td,.doc th{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
.doc strong{color:var(--text)}.doc a{color:var(--text)}
.docbg{position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(60% 40% at 50% -10%,rgba(109,74,255,.16),transparent 70%)}

/* reveal */
.rv{opacity:0;transform:translateY(28px);filter:blur(6px);transition:opacity 1s var(--ease),transform 1s var(--ease),filter 1s var(--ease)}
.rv.in{opacity:1;transform:none;filter:none}
.rv.d1{transition-delay:.08s}.rv.d2{transition-delay:.16s}.rv.d3{transition-delay:.24s}.rv.d4{transition-delay:.32s}.rv.d5{transition-delay:.4s}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;filter:none;transition:none}.grain{animation:none}}

@media(max-width:1000px){
 .nav{grid-template-columns:1fr auto;padding:14px 18px}.pill{display:none}
 .bnav{display:flex;position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:40;gap:2px;padding:5px;border-radius:999px;background:rgba(16,16,22,.82);border:1px solid var(--line2);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:0 10px 30px -10px rgba(0,0,0,.9)}
 .bnav a{padding:9px 14px;border-radius:999px;font-size:13px;color:#D4D4DC;text-decoration:none;white-space:nowrap}.bnav a.on{background:#fff;color:#0b0b10}
 .hero{padding:120px 0 90px}.hero .bg .media{width:340vw;top:34vh}.hero .sub{grid-template-columns:1fr;gap:24px}.hero .sub .r{justify-self:start;align-items:flex-start}
 .stats{grid-template-columns:repeat(2,1fr)}.stats>div:nth-child(2){border-right:0}.stats>div:nth-child(-n+2){border-bottom:1px solid var(--line)}
 .row{grid-template-columns:1fr;gap:6px;padding:24px 4px}.row .t{text-align:left;order:-1}.row .i{display:none}
 .cards,.plans{grid-template-columns:1fr}
 .shots{grid-template-columns:repeat(5,74vw);overflow-x:auto;scroll-snap-type:x mandatory;padding:20px 0 12px;margin:0 -28px;padding-left:28px;scrollbar-width:none;perspective:none}
 .shots::-webkit-scrollbar{display:none}.shots figure{scroll-snap-align:start}.shots figure .phone{transform:none!important}
 footer .top{grid-template-columns:1fr 1fr}
 section{padding:84px 0}.faq summary{font-size:22px}
 footer{padding-bottom:70px}
 #cta{padding-top:120px;min-height:80svh}#cta .planet{width:300vw;top:40%}
}
""".replace("NOISE_URI", NOISE)

JS = """
(function(){
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.08});
 document.querySelectorAll('.rv').forEach(function(el){io.observe(el)});
 var links=[].slice.call(document.querySelectorAll('.pill a[href^="#"],.bnav a[href^="#"]'));
 var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))}).filter(Boolean);
 function setActive(){var y=window.scrollY+innerHeight*.4,cur=null;secs.forEach(function(s){if(s.offsetTop<=y)cur=s.id});links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+cur)})}
 addEventListener('scroll',setActive,{passive:true});setActive();
 var h=document.querySelector('.hero h1'),sub=document.querySelector('.hero .sub'),kick=document.querySelector('.hero .kicker'),media=document.querySelector('.hero .bg .media');
 var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 function fade(){var y=scrollY;if(h){var p=Math.min(1,y/(innerHeight*.55));h.style.opacity=1-p;h.style.transform='translateY('+(-y*.18)+'px)';h.style.filter='blur('+(p*10)+'px)'}
  if(kick){kick.style.opacity=1-Math.min(1,y/(innerHeight*.3))}
  if(sub){sub.style.opacity=1-Math.min(1,y/(innerHeight*.35))}
  if(media&&!reduce){media.style.transform='translate3d(-50%,'+(y*.22)+'px,0)'}}
 addEventListener('scroll',fade,{passive:true});fade();
 var v=document.querySelector('.hero video');if(v){v.addEventListener('canplay',function(){v.classList.add('ready')});if(v.readyState>=3)v.classList.add('ready');if(reduce){v.pause();v.remove()}}
 document.querySelectorAll('.card').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')})});
})();
"""

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
{'<div class="docbg"></div>' if doc else ''}
<div class="grain" aria-hidden="true"></div>
<nav class="nav">
 <a class="logo" href="{home or './'}"><img src="{path_prefix}assets/icon-192.png" alt="">Influvia</a>
 <div class="pill">{pill}</div>
 <div class="right"><a class="btn white" href="{PLAY_URL}">Google Play {ARROW}</a></div>
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
 <div class="mark" aria-hidden="true">Influvia</div>
</div></footer>
<script>{JS}</script>
</body></html>"""

def card(n, eyebrow, title, text, img):
    return f'<div class="card rv {n}"><div class="glow"></div><div class="vis"><img src="assets/{img}" alt="" loading="lazy"></div><div class="body"><span class="eyebrow">{eyebrow}</span><h3>{title}</h3><p>{text}</p></div></div>'

def phone(img, alt, cap, n):
    return f'<figure class="rv {n}"><div class="phone"><div class="scr"><div class="isl"></div><img src="assets/{img}" alt="{alt}" loading="lazy"></div></div><figcaption>{cap}</figcaption></figure>'

INDEX = f"""
<header class="hero">
 <div class="bg"><div class="media"><img src="assets/planet.jpg" alt="" fetchpriority="high"><video autoplay muted loop playsinline preload="auto" poster="assets/planet.jpg"><source src="assets/planet.mp4" type="video/mp4"></video></div></div>
 <div class="stars" aria-hidden="true"></div>
 <div class="wrap">
  <div class="kicker rv"><span class="chip"><b>Yeni</b> Android sürümü Google Play'de</span></div>
  <h1><span class="l1">Etki yarat,</span><span class="l2">karşılığını al.</span></h1>
  <div class="sub">
   <p class="rv d2">Influvia, içerik üreticileri için tek uygulama: sana açık marka kampanyalarını gör, tek dokunuşla başvur, içeriğini teslim et, ödemeni takip et.</p>
   <div class="r rv d3">
    <p>Instagram'ını bağla; büyümen gerçek verilerle ölçülsün, Influvia Skorun markaların önüne çıksın.</p>
    <div class="cta"><a class="btn" href="{PLAY_URL}">Google Play'den indir {ARROW}</a><span class="soon">App Store sürümü yakında</span></div>
   </div>
  </div>
 </div>
 <div class="scrollhint" aria-hidden="true"><i></i><i></i><i></i></div>
</header>

<div id="content">
<section id="uygulama" class="wrap" style="padding-top:110px">
 <div class="stats rv">
  <div><b>₺0</b><span>Üreticiler için ücret</span></div>
  <div><b>1</b><span>Dokunuşla başvuru</span></div>
  <div><b>3</b><span>Ödül türü · ürün, ödeme, ikisi</span></div>
  <div><b>100</b><span>Puanlık Influvia Skoru</span></div>
 </div>
 <p class="quote rv">"Markaya DM atıp günlerce cevap beklemek yok. Brief, teslim ve ödeme — hepsi tek yerde, hepsi takip edilebilir."<small>Influvia ne için var</small></p>
</section>

<section class="wrap">
 <span class="eyebrow c rv">— Özellikler</span>
 <h2 class="h2 rv"><span class="l1">Uygulamada</span><span class="l2">neler var</span></h2>
 <p class="lead rv d1">Bir markayla çalışmanın her adımı: keşiften ödemeye, tek ekranda.</p>
 <div class="cards">
  {card("", "01 — Keşif", "Kampanyalar", "Sana açık kampanyaları brief, ödül türü ve son teslim tarihiyle birlikte gör; tek dokunuşla başvur.", "f-kampanyalar.webp")}
  {card("d1", "02 — Süreç", "Teslim ve ödeme", "Kabul edilince bildirim al, içerik linkini gönder, doğrulama ve ödeme durumunu uygulamadan izle.", "f-odeme.webp")}
  {card("d2", "03 — Ölçüm", "Influvia Skoru", "Instagram'ını bağla; takipçi büyümen, izlenme gelişimin ve paylaşım düzenin gerçek verilerden ölçülsün.", "f-skor.webp")}
  {card("", "04 — Analiz", "Performans", "Reels performansını, en güçlü içeriklerini ve kitle dağılımını tek ekranda gör.", "f-performans.webp")}
  {card("d1", "05 — Yapay zekâ", "İçerik analizi", "Galerinden bir görsel ya da video seç, paylaşmadan önce yapay zekâ destekli geri bildirim al.", "f-analiz.webp")}
  {card("d2", "06 — Gelişim", "Hedefler ve Akademi", "Haftalık hedefler koy, görevlerini takip et, Akademi içerikleriyle gelişmeye devam et.", "f-hedef.webp")}
 </div>
</section>

<section id="nasil" class="wrap">
 <span class="eyebrow c rv">— Süreç</span>
 <h2 class="h2 rv"><span class="l1">Nasıl</span><span class="l2">çalışır</span></h2>
 <p class="lead rv d1">Altı adım, tek uygulama. Her adımda nerede olduğunu görürsün.</p>
 <div class="rows">
  <div class="row rv"><div class="i">01</div><div class="n">Keşfet</div><p>Sana açık kampanyaları brief, ödül türü ve son teslim tarihiyle gör.</p><div class="t">Kampanyalar</div></div>
  <div class="row rv"><div class="i">02</div><div class="n">Başvur</div><p>Uygunsa tek dokunuşla başvur; kabul kararı bildirimle gelir.</p><div class="t">Tek dokunuş</div></div>
  <div class="row rv"><div class="i">03</div><div class="n">Üret</div><p>Brief'e uygun içeriğini hazırla; istersen paylaşmadan önce analiz ettir.</p><div class="t">İçerik analizi</div></div>
  <div class="row rv"><div class="i">04</div><div class="n">Teslim et</div><p>Paylaştığın içeriğin linkini gönder; doğrulama başlasın.</p><div class="t">Doğrulama</div></div>
  <div class="row rv"><div class="i">05</div><div class="n">Ödemeni al</div><p>Doğrulama tamamlanınca ödeme süreci başlar; durumunu Bakiye ekranından izle.</p><div class="t">Bakiye</div></div>
  <div class="row rv"><div class="i">06</div><div class="n">Büyü</div><p>Influvia Skoru ve performans ekranlarıyla nerede güçlendiğini gör, sonraki kampanyaya daha güçlü gir.</p><div class="t">Skor</div></div>
 </div>
</section>

<section id="ekranlar" class="wrap">
 <span class="eyebrow c rv">— Uygulama</span>
 <h2 class="h2 rv"><span class="l1">Uygulamadan</span><span class="l2">ekranlar</span></h2>
 <p class="lead rv d1">Karanlık, sade, hızlı. Her şey başparmağının altında.</p>
 <div class="shots">
  {phone("01-kampanyalar.jpg", "Kampanya listesi", "Kampanyalar", "")}
  {phone("03-kampanya-detay.jpg", "Kampanya detayı", "Kampanya detayı", "d1")}
  {phone("02-anasayfa.jpg", "Influvia ana sayfa", "Ana sayfa", "d2")}
  {phone("05-performans.jpg", "Performans ve Influvia Skoru", "Performans", "d3")}
  {phone("04-gorevler.jpg", "Görevler", "Görevler", "d4")}
 </div>
</section>

<section id="kimler" class="wrap">
 <span class="eyebrow c rv">— Kimler için</span>
 <h2 class="h2 rv"><span class="l1">Herkese</span><span class="l2">bir yer var</span></h2>
 <p class="lead rv d1">Üreticiler için ücretsiz. Markalar ve ajanslar için birlikte kurguluyoruz.</p>
 <div class="plans">
  <div class="plan rv"><span class="eyebrow">Marka</span><div class="price">Kampanya aç</div><p class="d">Ürününü Moonnect'in üretici ağıyla buluştur; başvuruları ve teslimleri tek panelden yönet.</p>
   <ul><li>Brief ve ödül tanımı</li><li>Başvuru ve skor görünümü</li><li>İçerik doğrulama</li><li>Ödeme takibi</li></ul>
   <a class="btn ghost" href="mailto:{SUPPORT}?subject=Influvia%20-%20Marka%20i%C5%9F%20birli%C4%9Fi">Bize yaz {ARROW}</a></div>
  <div class="plan hi rv d1"><span class="tag">Uygulama</span><span class="eyebrow">İçerik üreticisi</span><div class="price">Ücretsiz<small>her zaman</small></div><p class="d">Kampanyalara başvurmak, içerik teslim etmek ve büyümeni ölçmek için.</p>
   <ul><li>Açık kampanyalar</li><li>Tek dokunuşla başvuru</li><li>Influvia Skoru ve performans</li><li>İçerik analizi, hedefler, Akademi</li></ul>
   <a class="btn" href="{PLAY_URL}">Google Play'den indir {ARROW}</a></div>
  <div class="plan rv d2"><span class="eyebrow">Ajans</span><div class="price">Birlikte</div><p class="d">Birden fazla marka ya da üreticiyle çalışıyorsan sana özel kurgu için görüşelim.</p>
   <ul><li>Birden fazla marka</li><li>Sana özel kampanya kurgusu</li><li>Raporlama</li><li>Öncelikli iletişim</li></ul>
   <a class="btn ghost" href="mailto:{SUPPORT}?subject=Influvia%20-%20Ajans">Görüşelim {ARROW}</a></div>
 </div>
</section>

<section id="sss" class="wrap">
 <span class="eyebrow c rv">— SSS</span>
 <h2 class="h2 rv"><span class="l1">Sık sorulan</span><span class="l2">sorular</span></h2>
 <div class="faq rv d1" style="margin-top:56px">
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
 <img class="planet" src="assets/planet-1200.jpg" alt="" loading="lazy">
 <span class="eyebrow c rv">— Başla</span>
 <h2 class="h2 rv"><span class="l1">Bugün</span><span class="l2">başla</span></h2>
 <p class="rv d1">Hesap açmak bir dakika sürer. İlk kampanyana bugün başvur, gerisini uygulama takip etsin.</p>
 <div class="cta rv d2" style="justify-content:center"><a class="btn" href="{PLAY_URL}">Google Play'den indir {ARROW}</a><a class="btn ghost" href="mailto:{SUPPORT}?subject=Influvia%20iOS%20haber%20ver">iOS çıkınca haber ver</a></div>
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

(ROOT / "404.html").write_text(shell("Sayfa bulunamadı — Influvia", '<main class="doc"><h1>Sayfa bulunamadı</h1><p><a href="./">Ana sayfaya dön</a></p></main>', "Sayfa bulunamadı", doc=True), encoding="utf-8")
(ROOT / ".nojekyll").write_text("")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{DOMAIN}/{p}</loc></url>" for p in ["", "gizlilik/", "hesap-silme/", "kullanim-kosullari/", "destek/"]) + "</urlset>")
print("built")
