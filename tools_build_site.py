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

ZH_S={ # slug: (title, short, bullets)
'gpsr-eu-responsible-person':('欧盟负责人（GPSR）','根据《通用产品安全法规》（EU）2023/988，我们作为设在欧盟境内的经济经营者，为欧盟以外的工厂和跨境卖家担任欧盟负责人。',
 ['提供可印在产品标签和平台 listing 上的欧盟地址','作为市场监管机构的对接联系人','保管技术文件和产品安全信息','按 GPSR 要求审核标签和随附文件','协助处理整改、下架和召回']),
'epr-packaging-spain':('西班牙包装 EPR（皇家法令 1055/2022）','为投放西班牙市场的包装办理生产者注册，并担任授权代表。',
 ['在西班牙包装生产者登记系统完成注册','为未在西班牙设立实体的生产者担任授权代表','协助加入集体 EPR 回收体系（SCRAP）','定期申报包装数据','解读包装标识要求及欧盟新包装法规（PPWR）变化']),
'weee':('WEEE / 电子电气设备 EPR','为电子电气设备办理生产者注册、授权代表和申报。',
 ['生产者注册（西班牙 RII-AEE 登记）','为未在当地设立实体的生产者担任授权代表','加入集体回收体系并按期申报','产品标识与标签指导']),
'batteries':('电池 EPR（法规（EU）2023/1542）','协助履行电池投放欧盟及西班牙市场的生产者义务。',
 ['电池生产者注册','为未在当地设立实体的生产者担任授权代表','加入回收体系并按期申报','标签和文件要求指导']),
'cpnp-cosmetics':('化妆品欧盟负责人与 CPNP 通报','依据化妆品法规（EC）1223/2009，提供欧盟负责人服务和 CPNP 通报。',
 ['担任化妆品欧盟负责人','CPNP 通报','产品信息档案（PIF）的保管与审核','标签审核']),
'eprel-energy-label':('EPREL 能效标签注册','在欧盟 EPREL 数据库中为能源相关产品完成注册。',
 ['在 EPREL 中登记产品','开通供应商账户','能效标签和产品信息表指导']),
'eudr':('EUDR 尽职调查支持','协助应对《欧盟零毁林法规》的尽职调查声明和供应链溯源要求。',
 ['判断产品是否属于相关商品范围','协助准备尽职调查声明','收集供应商信息']),
'spain-nif-vat':('西班牙税号（NIF）与增值税代理','为外国公司申请西班牙税号（NIF），并提供增值税税务代表服务。',
 ['为非居民公司申请 NIF','增值税登记和税务代表','对接西班牙税务局（AEAT）']),
'customs-import-export':('清关与进出口支持','在清关和跨境贸易单证方面提供实操支持。',
 ['进出口单证指导','对接报关行','进口环节的经营者义务说明']),
}
FAQ_ZH=[('欧盟以外的卖家需要欧盟负责人吗？','需要。GPSR 实施后，投放欧盟市场的大多数消费品都必须有一家设在欧盟境内的经济经营者，其名称和联系方式要标注在产品、包装或随附文件上。'),
('GPSR 和 EPR 能交给同一家服务商吗？','可以。IberTrust Global 同时提供欧盟负责人、西班牙包装 EPR、WEEE、电池和化妆品 CPNP 服务，您只需对接一个窗口。'),
('你们支持哪些语言？','中文、英文和西班牙语。'),
('怎么获取报价方案？','请发邮件至 '+EMAIL+'，说明您的产品类别、目标市场和销售渠道，我们会根据情况给出定制方案。')]
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
@media(max-width:760px){.nav ul{display:none}.nav>a>b{display:none}.nav .btn{padding:8px 12px;font-size:13px;white-space:nowrap}.nav>span{display:flex;align-items:center;gap:8px;white-space:nowrap}.nav .lang a{margin-left:4px;font-size:13px}.hero h1{font-size:32px}}"""
T={'en':dict(home='Home',services='Services',about='About',faq='FAQ',blog='Insights',contact='Contact',quote='Get a quote',all='All services',
 tag='EU product compliance for global sellers',h1='Your EU Responsible Person and EPR partner in Spain',
 lead='IberTrust Global S.L. helps non-EU manufacturers and e-commerce sellers meet GPSR, EPR, packaging, WEEE, batteries and CPNP obligations — with one point of contact.',
 based='Based in Madrid, Spain',why='Why IberTrust',inc='What is included',ready='Ready to sell in the EU with confidence?',readyp='Tell us your products, markets and sales channels. We reply with a tailored proposal.'),
 'es':dict(home='Inicio',services='Servicios',about='Nosotros',faq='Preguntas',blog='Blog',contact='Contacto',quote='Pedir presupuesto',all='Todos los servicios',
 tag='Cumplimiento de producto en la UE para vendedores globales',h1='Su Persona Responsable en la UE y socio EPR en España',
 lead='IberTrust Global S.L. ayuda a fabricantes y vendedores online de fuera de la UE a cumplir GPSR, EPR, envases, RAEE, pilas y CPNP — con un único interlocutor.',
 based='Con sede en Madrid, España',why='Por qué IberTrust',inc='Qué incluye',ready='¿Listo para vender en la UE con tranquilidad?',readyp='Indíquenos productos, mercados y canales de venta y le enviaremos una propuesta a medida.'),
 'zh':dict(home='首页',services='服务',about='关于我们',faq='常见问题',blog='合规资讯',contact='联系我们',quote='获取方案',all='全部服务',
 tag='为跨境卖家提供欧盟产品合规服务',h1='您在西班牙的欧盟负责人与 EPR 合规伙伴',
 lead='IberTrust Global S.L. 帮助欧盟以外的工厂和跨境电商卖家满足 GPSR、EPR、包装、WEEE、电池和化妆品 CPNP 等合规要求——一个窗口，全程对接。',
 based='公司位于西班牙马德里',why='为什么选择 IberTrust',inc='服务内容',ready='想安心把产品卖进欧盟？',readyp='告诉我们您的产品、目标市场和销售渠道，我们会给出定制方案。')}
PFX={'en':'','es':'/es','zh':'/zh'}; HL={'en':'en','es':'es','zh':'zh-Hans'}
def L(s,lang):  # title, short, bullets for a service tuple
  return (s[1],s[2],s[3]) if lang=='en' else (s[4],s[5],s[6]) if lang=='es' else ZH_S[s[0]]
ORG={"@context":"https://schema.org","@type":"ProfessionalService","name":"IberTrust Global S.L.","url":D+"/","logo":D+"/logo.png","email":EMAIL,"telephone":"+34600256836","vatID":"B21813506",
 "address":{"@type":"PostalAddress","addressLocality":"Madrid","addressCountry":"ES"},"areaServed":"EU","knowsLanguage":["en","es","zh"]}
def page(lang,path,title,desc,body,extra_ld=None):
  t=T[lang]; p=PFX[lang]
  alt_en=D+'/'+path; alt_es=D+'/es/'+path; alt_zh=D+'/zh/'+path; me=D+p+'/'+path
  ld=[ORG]+(extra_ld or [])
  nav=''.join(f'<li><a href="{p}/{h}">{n}</a></li>' for h,n in [('services/',t['services']),('about.html',t['about']),('faq.html',t['faq']),('blog/',t['blog']),('contact.html',t['contact'])])
  html=f"""<!doctype html><html lang="{HL[lang]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{me}">
<link rel="alternate" hreflang="en" href="{alt_en}"><link rel="alternate" hreflang="es" href="{alt_es}"><link rel="alternate" hreflang="zh-Hans" href="{alt_zh}"><link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{me}"><meta property="og:image" content="{D}/logo.png"><meta name="twitter:card" content="summary">
<link rel="icon" href="/logo.png"><link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body>
<header><div class="wrap nav"><a href="{p}/" style="text-decoration:none;color:inherit"><img src="/logo.png" alt="IberTrust Global logo"><b>IberTrust Global</b></a><ul>{nav}</ul>
<span><a class="btn" href="mailto:{EMAIL}">{t['quote']}</a><span class="lang"><a href="/{path}">EN</a><a href="/es/{path}">ES</a><a href="/zh/{path}">中文</a></span></span></div></header>
<main>{body}</main>
<footer><div class="wrap grid"><div><b style="color:#fff">IberTrust Global S.L.</b><br>CIF B21813506<br>{t['based']}<br><a href="mailto:{EMAIL}">{EMAIL}</a> · +34 600 256 836</div>
<div>{''.join(f'<a href="{p}/services/{s[0]}.html">{L(s,lang)[0]}</a><br>' for s in S[:6])}</div>
<div><a href="/privacy.html">{'隐私政策' if lang=='zh' else 'Privacy'}</a><br><a href="/terms.html">{'使用条款' if lang=='zh' else 'Terms'}</a><br>© {datetime.date.today().year} IberTrust Global S.L.</div></div></footer></body></html>"""
  out=os.path.join(R,(p[1:]+'/' if p else '')+path)
  if out.endswith('/'): out+='index.html'
  os.makedirs(os.path.dirname(out),exist_ok=True); open(out,'w').write(html)
  return me
# BLOG: add new articles here; every article needs 'en','es','zh' = (title, html body). Optional 'date'.
POSTS=[('gpsr-responsible-person-guide',{
 'en':('What an EU Responsible Person does under GPSR','<p>Since 13 December 2024, Regulation (EU) 2023/988 (GPSR) requires that most consumer products sold in the EU have an economic operator established in the Union. Its name, postal and electronic address must appear on the product, packaging or accompanying documents, and in online listings.</p><h2>Main tasks</h2><ul><li>Verify technical documentation and the EU declaration where applicable</li><li>Cooperate with market surveillance authorities</li><li>Inform authorities about risks and support corrective actions</li></ul><h2>Next step</h2><p>Write to '+EMAIL+' for a review of your labels and documentation.</p>'),
 'es':('Qué hace una Persona Responsable con el GPSR','<p>Desde el 13 de diciembre de 2024, el Reglamento (UE) 2023/988 (GPSR) exige que la mayoría de productos de consumo vendidos en la UE tengan un operador económico establecido en la Unión, cuyos datos figuren en el producto, el envase o la documentación y en los anuncios online.</p><h2>Tareas principales</h2><ul><li>Verificar la documentación técnica</li><li>Cooperar con las autoridades de vigilancia del mercado</li><li>Informar de riesgos y apoyar acciones correctoras</li></ul><p>Escriba a '+EMAIL+' para revisar su etiquetado.</p>'),
 'zh':('GPSR 下的欧盟负责人到底做什么？','<p>自 2024 年 12 月 13 日起，《通用产品安全法规》（EU）2023/988（GPSR）要求：在欧盟销售的大多数消费品，都必须有一家设在欧盟境内的经济经营者。它的名称、邮寄地址和电子联系方式，需要标注在产品、包装或随附文件上，线上 listing 中也要展示。</p><p>对中国跨境卖家来说，这意味着光有中国工厂地址已经不够，产品上市前就要把欧盟负责人的信息准备好。</p><h2>欧盟负责人的主要职责</h2><ul><li>核查技术文件，以及适用时的欧盟符合性声明</li><li>配合市场监管机构的问询和检查</li><li>发现风险时通报主管机构，并协助整改</li></ul><h2>下一步</h2><p>欢迎发邮件至 '+EMAIL+'，我们可以帮您审核标签和相关文件。</p>')})]
urls=[]
for lang in ['en','es','zh']:
  t=T[lang]; p=PFX[lang]
  cards=''.join(f'<div class="card"><h3>{L(s,lang)[0]}</h3><p>{L(s,lang)[1]}</p><a href="{p}/services/{s[0]}.html">→</a></div>' for s in S)
  faq={'en':FAQ_EN,'es':FAQ_ES,'zh':FAQ_ZH}[lang]
  faqhtml=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
  faqld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
  why_en=['One contact for GPSR, EPR, packaging, WEEE, batteries and CPNP','Spanish company (CIF B21813506) with EU establishment','Support in English, Spanish and Mandarin Chinese','Hands-on experience with e-commerce and marketplace requirements','Clear onboarding: mandate, documents, label review, registration']
  why_es=['Un interlocutor para GPSR, EPR, envases, RAEE, pilas y CPNP','Empresa española (CIF B21813506) establecida en la UE','Atención en inglés, español y chino mandarín','Experiencia práctica con e-commerce y marketplaces','Alta clara: mandato, documentos, revisión de etiquetas, registro']
  why_zh=['GPSR、EPR、包装、WEEE、电池、CPNP 一个窗口统一对接','西班牙注册公司（CIF B21813506），在欧盟境内设有实体','中文、英文、西班牙语沟通，无语言障碍','熟悉跨境电商和各大平台的合规要求','流程清晰：签署委托、收集资料、审核标签、完成注册']
  why=''.join(f'<div class="card">✔ {w}</div>' for w in {'en':why_en,'es':why_es,'zh':why_zh}[lang])
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
    title,short,bul=L(s,lang)
    sld={"@context":"https://schema.org","@type":"Service","name":title,"description":short,"provider":{"@type":"Organization","name":"IberTrust Global S.L."},"areaServed":"EU"}
    body=f'<div class="hero"><div class="wrap"><h1>{title}</h1><p>{short}</p><a class="btn" href="mailto:{EMAIL}?subject={title}">{t["quote"]}</a></div></div><section><div class="wrap"><h2>{t["inc"]}</h2><ul>'+''.join(f'<li>{b}</li>' for b in bul)+f'</ul><p><a href="{p}/faq.html">{t["faq"]}</a> · <a href="{p}/services/">{t["all"]}</a></p></div></section>{cta}'
    urls.append(page(lang,f'services/{s[0]}.html',title+' | IberTrust Global',short,body,[sld]))
  about_en='<p>IberTrust Global S.L. is a Spanish company (CIF B21813506) providing EU product compliance services to manufacturers and online sellers from outside the EU. We act as EU Responsible Person, EPR authorised representative and regulatory contact, and help with Spanish NIF/VAT and cosmetics notifications.</p><p>Our team supports clients in English, Spanish and Mandarin Chinese and works with local environmental compliance partners in Spain.</p>'
  about_es='<p>IberTrust Global S.L. es una empresa española (CIF B21813506) que presta servicios de cumplimiento de producto en la UE a fabricantes y vendedores online de fuera de la UE: Persona Responsable, representante autorizado EPR, NIF/IVA y notificaciones de cosméticos.</p><p>Atendemos en inglés, español y chino mandarín y colaboramos con socios locales de cumplimiento ambiental en España.</p>'
  about_zh='<p>IberTrust Global S.L. 是一家西班牙公司（CIF B21813506），专为欧盟以外的工厂和跨境电商卖家提供欧盟产品合规服务。我们可以担任欧盟负责人、EPR 授权代表和监管对接人，并协助办理西班牙税号（NIF）/增值税以及化妆品通报。</p><p>团队可用中文、英文和西班牙语服务客户，并与西班牙本地的环保合规伙伴合作。</p>'
  urls.append(page(lang,'about.html',t['about']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["about"]}</h1>{ {"en":about_en,"es":about_es,"zh":about_zh}[lang] }<p>{t["based"]}.</p></div></section>{cta}'))
  urls.append(page(lang,'faq.html',t['faq']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["faq"]}</h1>{faqhtml}</div></section>{cta}',[faqld]))
  ct=f'<section><div class="wrap"><h1>{t["contact"]}</h1><div class="grid"><div class="card"><h3>{'邮箱' if lang=='zh' else 'Email'}</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div><div class="card"><h3>{'电话 / WhatsApp' if lang=='zh' else 'Tel / WhatsApp'}</h3>+34 600 256 836</div><div class="card"><h3>IberTrust Global S.L.</h3>CIF B21813506<br>{t["based"]}</div></div><p>{t["readyp"]}</p></div></section>'
  urls.append(page(lang,'contact.html',t['contact']+' | IberTrust Global',t['readyp'],ct))
  posts=[(sl,P[lang][0]) for sl,P in POSTS]
  lst=''.join(f'<div class="card"><h3><a href="{p}/blog/{sl}.html">{ti}</a></h3></div>' for sl,ti in posts)
  urls.append(page(lang,'blog/',t['blog']+' | IberTrust Global',t['lead'],f'<section><div class="wrap"><h1>{t["blog"]}</h1><div class="grid">{lst}</div></div></section>'))
  for sl,P in POSTS:
    ti,txt=P[lang]; pub=P.get('date',TODAY)
    art={"@context":"https://schema.org","@type":"Article","headline":ti,"inLanguage":HL[lang],"datePublished":pub,"author":{"@type":"Organization","name":"IberTrust Global S.L."},"publisher":{"@type":"Organization","name":"IberTrust Global S.L."}}
    urls.append(page(lang,f'blog/{sl}.html',ti+' | IberTrust Global',ti,f'<section><div class="wrap"><article><h1>{ti}</h1><p><small>{pub} · IberTrust Global</small></p>{txt}</article></div></section>',[art]))
os.makedirs(R+'/assets',exist_ok=True); open(R+'/assets/style.css','w').write(CSS)
open(R+'/blog/_post-template.html','w').write('<!-- Copy blog/gpsr-responsible-person-guide.html, change <title>, meta description, og:*, canonical/hreflang, Article JSON-LD (headline, datePublished), <h1> and body; or better: add the post (en/es/zh) to POSTS in /workspace/build_site.py and rerun it — it regenerates /, /es/, /zh/, blog indexes and sitemap.xml. -->\n')
urls+= [D+'/privacy.html',D+'/terms.html']
open(R+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls)+'</urlset>\n')
open(R+'/robots.txt','w').write(f'User-agent: *\nAllow: /\nDisallow: /legacy/\nSitemap: {D}/sitemap.xml\n')
print(len(urls),'urls')
