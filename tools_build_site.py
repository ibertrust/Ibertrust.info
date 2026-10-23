import os, json, datetime
R='/workspace/ibertrust-site'; D='https://ibertrust.info'; TODAY=datetime.date.today().isoformat()
EMAIL='contact@ibertrust.info'
S=[ # slug, EN title, EN short, EN body bullets, ES title, ES short, ES bullets
('gpsr-eu-responsible-person','EU Responsible Person (GPSR)','Act as your EU-established economic operator under Regulation (EU) 2023/988 for non-EU manufacturers and e-commerce sellers.',
 ['EU address for product labels and marketplace listings','Point of contact for market surveillance authorities','Custody of technical documentation and safety information','Label and documentation review against GPSR requirements','Support with corrective actions, withdrawals and recalls'],
 'Persona Responsable en la UE (GPSR)','Actuamos como operador económico establecido en la UE según el Reglamento (UE) 2023/988 para fabricantes y vendedores de fuera de la UE.',
 ['Dirección en la UE para etiquetas y marketplaces','Punto de contacto con las autoridades de vigilancia del mercado','Custodia de la documentación técnica','Revisión de etiquetado y documentación GPSR','Apoyo en acciones correctoras, retiradas y recuperaciones']),
('epr-packaging-spain','Spain Packaging EPR (Royal Decree 1055/2022)','Producer registration and authorised representation for packaging placed on the Spanish market.',
 ['Registration in the Spanish producer register for packaging','Authorised representative for producers not established in Spain','Joining a collective EPR scheme (SCRAP)','Periodic packaging declarations','Guidance on labelling and PPWR changes'],
 'EPR de envases en España (RD 1055/2022)','Registro de productores y representación autorizada para envases puestos en el mercado español.',
 ['Inscripción en el registro de productores de envases','Representante autorizado para productores no establecidos en España','Adhesión a un sistema colectivo (SCRAP)','Declaraciones periódicas de envases','Orientación sobre etiquetado y el nuevo PPWR']),
('weee','WEEE / Electrical & Electronic Equipment EPR','Registration, authorised representation and reporting for electrical and electronic equipment.',
 ['Producer registration (RII-AEE in Spain)','Authorised representative for non-established producers','Collective scheme membership and reporting','Marking and labelling guidance'],
 'RAEE / EPR de aparatos eléctricos y electrónicos','Registro, representación autorizada y declaraciones para aparatos eléctricos y electrónicos.',
 ['Inscripción de productor (RII-AEE)','Representante autorizado para productores no establecidos','Adhesión a sistema colectivo y declaraciones','Orientación sobre marcado y etiquetado']),
('batteries','Batteries EPR (Regulation (EU) 2023/1542)','Producer obligations for batteries placed on the EU and Spanish market.',
 ['Producer registration for batteries','Authorised representative for non-established producers','Take-back scheme membership and reporting','Labelling and documentation guidance'],
 'EPR de pilas y baterías (Reglamento (UE) 2023/1542)','Obligaciones de productor para pilas y baterías en la UE y en España.',
 ['Registro de productor de pilas y baterías','Representante autorizado','Adhesión a sistema de recogida y declaraciones','Orientación sobre etiquetado y documentación']),
('cpnp-cosmetics','Cosmetics Responsible Person & CPNP','Responsible Person services and CPNP notification for cosmetic products (Regulation (EC) 1223/2009).',
 ['EU Responsible Person for cosmetics','CPNP notification','Product Information File (PIF) custody and review','Label review'],
 'Persona Responsable de cosméticos y CPNP','Persona Responsable y notificación CPNP para productos cosméticos (Reglamento (CE) 1223/2009).',
 ['Persona Responsable en la UE para cosméticos','Notificación en el CPNP','Custodia y revisión del PIF','Revisión de etiquetado']),
('eprel-energy-label','EPREL Energy Label Registration','Registration of energy-related products in the EU EPREL database.',
 ['Product registration in EPREL','Supplier account setup','Energy label and product information sheet guidance'],
 'Registro EPREL de etiqueta energética','Registro de productos relacionados con la energía en la base de datos EPREL.',
 ['Registro de productos en EPREL','Alta de cuenta de proveedor','Orientación sobre etiqueta energética y ficha']),
('eudr','EUDR Due Diligence Support','Assistance with EU Deforestation Regulation due diligence statements and sourcing transparency.',
 ['Scope check for relevant commodities','Due diligence statement support','Supplier information collection'],
 'Apoyo EUDR (deforestación)','Asistencia con las declaraciones de diligencia debida del Reglamento de Deforestación.',
 ['Análisis de alcance','Apoyo en la declaración de diligencia debida','Recogida de información de proveedores']),
('spain-nif-vat','Spanish NIF & VAT Representation','Spanish tax identification (NIF) for foreign companies and VAT representative services.',
 ['NIF application for non-resident companies','VAT registration and fiscal representation','Liaison with the Spanish Tax Agency (AEAT)'],
 'NIF y representación de IVA en España','NIF para empresas extranjeras y servicios de representante fiscal de IVA.',
 ['Solicitud de NIF para empresas no residentes','Alta en IVA y representación fiscal','Gestión ante la AEAT']),
('customs-import-export','Customs, Import & Export Support','Practical support with customs clearance and cross-border trade documentation.',
 ['Import/export documentation guidance','Coordination with customs brokers','Economic operator obligations at import'],
 'Aduanas, importación y exportación','Apoyo práctico en despacho aduanero y documentación de comercio exterior.',
 ['Orientación documental de importación/exportación','Coordinación con agentes de aduanas','Obligaciones del operador en la importación']),
]
FAQ_EN=[('Do non-EU sellers need an EU Responsible Person?','Yes, under GPSR most consumer products placed on the EU market need an economic operator established in the EU, whose name and contact details appear on the product, packaging or accompanying documents.'),
('Can one provider cover GPSR and EPR?','Yes. IberTrust Global handles EU Responsible Person, Spain packaging EPR, WEEE, batteries and CPNP so you have one point of contact.'),
('Which languages do you support?','English, Spanish and Mandarin Chinese.'),
('How do I get a quote?','Email '+EMAIL+' with your products, markets and sales channels. We reply with a tailored proposal.')]
FAQ_ES=[('¿Necesita un vendedor de fuera de la UE una Persona Responsable?','Sí. Con el GPSR, la mayoría de productos de consumo necesitan un operador económico establecido en la UE, cuyos datos figuren en el producto, el envase o la documentación.'),
('¿Puede un solo proveedor cubrir GPSR y EPR?','Sí. IberTrust Global gestiona Persona Responsable, EPR de envases, RAEE, pilas y CPNP con un único interlocutor.'),
('¿En qué idiomas atienden?','Inglés, español y chino mandarín.'),
('¿Cómo pido presupuesto?','Escriba a '+EMAIL+' indicando productos, mercados y canales de venta.')]
CSS="""*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,Arial,sans-serif;color:#1b2430;line-height:1.6}a{color:#0b5cad}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}header{border-bottom:1px solid #e5e9f0;background:#fff;position:sticky;top:0;z-index:5}
.nav{display:flex;align-items:center;justify-content:space-between;height:68px}.nav img{height:38px;vertical-align:middle}.nav b{margin-left:8px}
.nav ul{display:flex;gap:22px;list-style:none;margin:0;padding:0}.nav ul a{text-decoration:none;color:#1b2430;font-weight:500}
.btn{display:inline-block;background:#0b5cad;color:#fff!important;padding:11px 20px;border-radius:8px;text-decoration:none;font-weight:600}.btn.alt{background:#fff;color:#0b5cad!important;border:1px solid #0b5cad}
.hero{background:linear-gradient(135deg,#0b2545,#0b5cad);color:#fff;padding:80px 0}.hero h1{font-size:44px;line-height:1.15;margin:0 0 16px}.hero p{font-size:19px;max-width:720px;opacity:.92}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}.card{border:1px solid #e5e9f0;border-radius:12px;padding:22px;background:#fff}.card h3{margin-top:0}
section{padding:56px 0}.muted{background:#f5f7fa}.trust{display:flex;flex-wrap:wrap;gap:12px}.trust span{background:rgba(255,255,255,.15);color:#fff;border-radius:20px;padding:6px 14px;font-size:14px}
details{border-bottom:1px solid #e5e9f0;padding:14px 0}summary{font-weight:600;cursor:pointer}footer{background:#0b2545;color:#cfd8e3;padding:40px 0;font-size:14px}footer a{color:#fff}
.lang a{margin-left:8px;font-size:14px}.cta{background:#0b2545;color:#fff;border-radius:14px;padding:36px;text-align:center}
@media(max-width:760px){.nav ul{display:none}.hero h1{font-size:32px}}"""
T={'en':dict(home='Home',services='Services',about='About',faq='FAQ',blog='Insights',contact='Contact',quote='Get a quote',all='All services',
 tag='EU product compliance for global sellers',h1='Your EU Responsible Person and EPR partner in Spain',
 lead='IberTrust Global S.L. helps non-EU manufacturers and e-commerce sellers meet GPSR, EPR, packaging, WEEE, batteries and CPNP obligations — with one point of contact.',
 based='Based in Madrid, Spain',why='Why IberTrust',inc='What is included',ready='Ready to sell in the EU with confidence?',readyp='Tell us your products, markets and sales channels. We reply with a tailored proposal.'),
 'es':dict(home='Inicio',services='Servicios',about='Nosotros',faq='Preguntas',blog='Blog',contact='Contacto',quote='Pedir presupuesto',all='Todos los servicios',
 tag='Cumplimiento de producto en la UE para vendedores globales',h1='Su Persona Responsable en la UE y socio EPR en España',
 lead='IberTrust Global S.L. ayuda a fabricantes y vendedores online de fuera de la UE a cumplir GPSR, EPR, envases, RAEE, pilas y CPNP — con un único interlocutor.',
 based='Con sede en Madrid, España',why='Por qué IberTrust',inc='Qué incluye',ready='¿Listo para vender en la UE con tranquilidad?',readyp='Indíquenos productos, mercados y canales de venta y le enviaremos una propuesta a medida.')}
ORG={"@context":"https://schema.org","@type":"ProfessionalService","name":"IberTrust Global S.L.","url":D+"/","logo":D+"/logo.png","email":EMAIL,"telephone":"+34600256836","vatID":"B21813506",
 "address":{"@type":"PostalAddress","addressLocality":"Madrid","addressCountry":"ES"},"areaServed":"EU","knowsLanguage":["en","es","zh"]}
def page(lang,path,title,desc,body,extra_ld=None):
  t=T[lang]; p='' if lang=='en' else '/es'
  alt_en=D+'/'+path; alt_es=D+'/es/'+path
  ld=[ORG]+(extra_ld or [])
  nav=''.join(f'<li><a href="{p}/{h}">{n}</a></li>' for h,n in [('services/',t['services']),('about.html',t['about']),('faq.html',t['faq']),('blog/',t['blog']),('contact.html',t['contact'])])
  html=f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{alt_en if lang=='en' else alt_es}">
<link rel="alternate" hreflang="en" href="{alt_en}"><link rel="alternate" hreflang="es" href="{alt_es}"><link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{alt_en if lang=='en' else alt_es}"><meta property="og:image" content="{D}/logo.png"><meta name="twitter:card" content="summary">
<link rel="icon" href="/logo.png"><link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body>
<header><div class="wrap nav"><a href="{p}/" style="text-decoration:none;color:inherit"><img src="/logo.png" alt="IberTrust Global logo"><b>IberTrust Global</b></a><ul>{nav}</ul>
<span><a class="btn" href="mailto:{EMAIL}">{t['quote']}</a><span class="lang"><a href="/{path}">EN</a><a href="/es/{path}">ES</a></span></span></div></header>
<main>{body}</main>
<footer><div class="wrap grid"><div><b style="color:#fff">IberTrust Global S.L.</b><br>CIF B21813506<br>{t['based']}<br><a href="mailto:{EMAIL}">{EMAIL}</a> · +34 600 256 836</div>
<div>{''.join(f'<a href="{p}/services/{s[0]}.html">{s[1] if lang=="en" else s[4]}</a><br>' for s in S[:6])}</div>
<div><a href="/privacy.html">Privacy</a><br><a href="/terms.html">Terms</a><br>© {datetime.date.today().year} IberTrust Global S.L.</div></div></footer></body></html>"""
  out=os.path.join(R,('' if lang=='en' else 'es/')+path)
  if out.endswith('/'): out+='index.html'
  os.makedirs(os.path.dirname(out),exist_ok=True); open(out,'w').write(html)
  return (alt_en if lang=='en' else alt_es)
urls=[]
for lang in ['en','es']:
  t=T[lang]; p='' if lang=='en' else '/es'; ix=1 if lang=='en' else 4
  cards=''.join(f'<div class="card"><h3>{s[ix]}</h3><p>{s[ix+1]}</p><a href="{p}/services/{s[0]}.html">→</a></div>' for s in S)
  faq=FAQ_EN if lang=='en' else FAQ_ES
  faqhtml=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
  faqld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
  why_en=['One contact for GPSR, EPR, packaging, WEEE, batteries and CPNP','Spanish company (CIF B21813506) with EU establishment','Support in English, Spanish and Mandarin Chinese','Hands-on experience with e-commerce and marketplace requirements','Clear onboarding: mandate, documents, label review, registration']
  why_es=['Un interlocutor para GPSR, EPR, envases, RAEE, pilas y CPNP','Empresa española (CIF B21813506) establecida en la UE','Atención en inglés, español y chino mandarín','Experiencia práctica con e-commerce y marketplaces','Alta clara: mandato, documentos, revisión de etiquetas, registro']
  why=''.join(f'<div class="card">✔ {w}</div>' for w in (why_en if lang=='en' else why_es))
  cta=f'<section><div class="wrap"><div class="cta"><h2>{t["ready"]}</h2><p>{t["readyp"]}</p><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a></div></div></section>'
  home=f"""<div class="hero"><div class="wrap"><p>{t['tag']}</p><h1>{t['h1']}</h1><p>{t['lead']}</p>
<p><a class="btn" href="mailto:{EMAIL}">{t['quote']}</a> <a class="btn alt" href="{p}/services/">{t['all']}</a></p>
<div class="trust"><span>GPSR (EU) 2023/988</span><span>RD 1055/2022</span><span>WEEE</span><span>(EU) 2023/1542</span><span>CPNP</span><span>EN · ES · 中文</span></div></div></div>
<section><div class="wrap"><h2>{t['services']}</h2><div class="grid">{cards}</div></div></section>
<section class="muted"><div class="wrap"><h2>{t['why']}</h2><div class="grid">{why}</div></div></section>
<section><div class="wrap"><h2>{t['faq']}</h2>{faqhtml}</div></section>{cta}"""
  urls.append(page(lang,'',('IberTrust Global | EU Responsible Person, GPSR & EPR in Spain' if lang=='en' else 'IberTrust Global | Persona Responsable UE, GPSR y EPR en España'),t['lead'],home,[faqld]))
  urls.append(page(lang,'services/',t['services']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["services"]}</h1><div class="grid">{cards}</div></div></section>{cta}'))
  for s in S:
    title,short,bul=(s[1],s[2],s[3]) if lang=='en' else (s[4],s[5],s[6])
    sld={"@context":"https://schema.org","@type":"Service","name":title,"description":short,"provider":{"@type":"Organization","name":"IberTrust Global S.L."},"areaServed":"EU"}
    body=f'<div class="hero"><div class="wrap"><h1>{title}</h1><p>{short}</p><a class="btn" href="mailto:{EMAIL}?subject={title}">{t["quote"]}</a></div></div><section><div class="wrap"><h2>{t["inc"]}</h2><ul>'+''.join(f'<li>{b}</li>' for b in bul)+f'</ul><p><a href="{p}/faq.html">{t["faq"]}</a> · <a href="{p}/services/">{t["all"]}</a></p></div></section>{cta}'
    urls.append(page(lang,f'services/{s[0]}.html',title+' | IberTrust Global',short,body,[sld]))
  about_en='<p>IberTrust Global S.L. is a Spanish company (CIF B21813506) providing EU product compliance services to manufacturers and online sellers from outside the EU. We act as EU Responsible Person, EPR authorised representative and regulatory contact, and help with Spanish NIF/VAT and cosmetics notifications.</p><p>Our team supports clients in English, Spanish and Mandarin Chinese and works with local environmental compliance partners in Spain.</p>'
  about_es='<p>IberTrust Global S.L. es una empresa española (CIF B21813506) que presta servicios de cumplimiento de producto en la UE a fabricantes y vendedores online de fuera de la UE: Persona Responsable, representante autorizado EPR, NIF/IVA y notificaciones de cosméticos.</p><p>Atendemos en inglés, español y chino mandarín y colaboramos con socios locales de cumplimiento ambiental en España.</p>'
  urls.append(page(lang,'about.html',t['about']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["about"]}</h1>{about_en if lang=="en" else about_es}<p>{t["based"]}.</p></div></section>{cta}'))
  urls.append(page(lang,'faq.html',t['faq']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["faq"]}</h1>{faqhtml}</div></section>{cta}',[faqld]))
  ct=f'<section><div class="wrap"><h1>{t["contact"]}</h1><div class="grid"><div class="card"><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div><div class="card"><h3>Tel / WhatsApp</h3>+34 600 256 836</div><div class="card"><h3>IberTrust Global S.L.</h3>CIF B21813506<br>{t["based"]}</div></div><p>{t["readyp"]}</p></div></section>'
  urls.append(page(lang,'contact.html',t['contact']+' | IberTrust Global',t['readyp'],ct))
  posts=[('gpsr-responsible-person-guide','What an EU Responsible Person does under GPSR' if lang=='en' else 'Qué hace una Persona Responsable con el GPSR')]
  lst=''.join(f'<div class="card"><h3><a href="{p}/blog/{sl}.html">{ti}</a></h3></div>' for sl,ti in posts)
  urls.append(page(lang,'blog/',t['blog']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["blog"]}</h1><div class="grid">{lst}</div></div></section>'))
  for sl,ti in posts:
    art={"@context":"https://schema.org","@type":"Article","headline":ti,"datePublished":TODAY,"author":{"@type":"Organization","name":"IberTrust Global S.L."},"publisher":{"@type":"Organization","name":"IberTrust Global S.L."}}
    txt=('<p>Since 13 December 2024, Regulation (EU) 2023/988 (GPSR) requires that most consumer products sold in the EU have an economic operator established in the Union. Its name, postal and electronic address must appear on the product, packaging or accompanying documents, and in online listings.</p><h2>Main tasks</h2><ul><li>Verify technical documentation and the EU declaration where applicable</li><li>Cooperate with market surveillance authorities</li><li>Inform authorities about risks and support corrective actions</li></ul><h2>Next step</h2><p>Write to '+EMAIL+' for a review of your labels and documentation.</p>') if lang=='en' else ('<p>Desde el 13 de diciembre de 2024, el Reglamento (UE) 2023/988 (GPSR) exige que la mayoría de productos de consumo vendidos en la UE tengan un operador económico establecido en la Unión, cuyos datos figuren en el producto, el envase o la documentación y en los anuncios online.</p><h2>Tareas principales</h2><ul><li>Verificar la documentación técnica</li><li>Cooperar con las autoridades de vigilancia del mercado</li><li>Informar de riesgos y apoyar acciones correctoras</li></ul><p>Escriba a '+EMAIL+' para revisar su etiquetado.</p>')
    urls.append(page(lang,f'blog/{sl}.html',ti+' | IberTrust Global',ti,f'<section><div class="wrap"><article><h1>{ti}</h1><p><small>{TODAY} · IberTrust Global</small></p>{txt}</article></div></section>',[art]))
os.makedirs(R+'/assets',exist_ok=True); open(R+'/assets/style.css','w').write(CSS)
open(R+'/blog/_post-template.html','w').write('<!-- Copy blog/gpsr-responsible-person-guide.html, change <title>, meta description, og:*, canonical/hreflang, Article JSON-LD (headline, datePublished), <h1> and body; then add the post to blog/index.html, es/blog/ and sitemap.xml (or rerun /workspace/build_site.py after adding to posts). -->\n')
urls+= [D+'/privacy.html',D+'/terms.html']
open(R+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls)+'</urlset>\n')
open(R+'/robots.txt','w').write(f'User-agent: *\nAllow: /\nDisallow: /legacy/\nSitemap: {D}/sitemap.xml\n')
print(len(urls),'urls')
