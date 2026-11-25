# Extra FAQ items and grouped FAQ page renderer for tools_build_site.py.
# Existing six FAQS entries (with blog posts) are kept and placed in these groups.

import re

EMAIL = 'contact@ibertrust.info'

FAQ_CSS = (
    '.faq-lead{max-width:720px;margin:0 0 12px;color:#44515f;font-size:17px;line-height:1.55}'
    '.faq-group{margin:8px 0 8px}'
    '.faq-group h2{font-size:22px;line-height:1.3;margin:32px 0 6px;color:#0b2545}'
    '.faq-group details p{margin:8px 0;line-height:1.55}'
    '@media(max-width:760px){.faq-lead{font-size:16px}.faq-group h2{font-size:20px;margin:24px 0 4px}'
    'details{padding:12px 0}summary{font-size:16px;line-height:1.35}'
    'details p{font-size:15px;line-height:1.55}}'
)

LEAD = {
    'en': 'Answers are grouped into tax compliance, product compliance, and fees and process. Open a question to read the short answer; some also have a longer article.',
    'es': 'Las respuestas están agrupadas en cumplimiento fiscal, cumplimiento de producto, y honorarios y proceso. Abra cada pregunta para leer la respuesta breve; algunas tienen también un artículo más largo.',
    'zh': '以下按稅務合規、產品合規、費用與流程三組排列。點開問題即可閱讀簡要解答；部分條目另有較詳細的說明文章。',
}

GROUP_TITLE = {
    'tax': {'en': 'Tax compliance', 'es': 'Cumplimiento fiscal', 'zh': '稅務合規'},
    'product': {'en': 'Product compliance', 'es': 'Cumplimiento de producto', 'zh': '產品合規'},
    'fees': {'en': 'Fees and process', 'es': 'Honorarios y proceso', 'zh': '費用與流程'},
}

# Short-answer overrides for existing FAQS slugs (FAQ page only; blog posts unchanged except where we also edit FAQS).
OVERRIDES = {
    'compliance-support-in-chinese-english-spanish': {
        'en': (
            'Which languages do you support?',
            'We work in English, Spanish and Cantonese. You can send documents, labels and questions in any of the three; written Chinese is in Traditional characters. Spanish authorities and collective schemes generally work in Spanish, so we handle that side and explain the outcome to you in your language. Labels and instructions must follow the language rules of each country where the product is sold.',
        ),
        'es': (
            '¿En qué idiomas atienden?',
            'Trabajamos en inglés, español y cantonés. Puede enviarnos documentos, etiquetas y consultas en cualquiera de los tres; el chino escrito se usa en caracteres tradicionales. Las autoridades españolas y los sistemas colectivos trabajan en español; nos ocupamos de esa parte y le explicamos el resultado en su idioma. Etiquetas e instrucciones deben cumplir las reglas de idioma de cada país de venta.',
        ),
        # zh already describes 粵語、英文、西班牙文
    },
}

def Q(en_q, en_a, es_q, es_a, zh_q, zh_a):
    return {'en': (en_q, en_a), 'es': (es_q, es_a), 'zh': (zh_q, zh_a)}

# Page order within each group. A string is an existing FAQS slug; a dict is a page-only Q&A.
GROUPS = {
    'tax': [
        Q(
            'Does a foreign company need a Spanish NIF to sell into Spain?',
            'Not in every case, but often yes when the activity has tax implications in Spain. A Spanish NIF is the company’s tax identification number (for a foreign legal entity it starts with N). You typically need one to register for Spanish VAT, to apply for an EORI in Spain, to register for OSS in Spain, or to complete Spain packaging EPR. Distance sales of goods to Spanish consumers can sometimes be declared through OSS in another Member State, but a Spanish NIF may still be required for a warehouse in Spain, for imports, or for packaging EPR. Tell us how you sell and we will say which formalities apply.',
            '¿Necesita una empresa extranjera un NIF español para vender en España?',
            'No en todos los casos, pero sí con frecuencia cuando la actividad tiene implicaciones fiscales en España. El NIF es el número de identificación fiscal de la empresa (en una entidad jurídica extranjera empieza por N). Suele hacer falta para darse de alta en el IVA español, solicitar un EORI en España, registrarse en OSS en España o completar el registro EPR de envases. Las ventas a distancia a consumidores en España a veces pueden declararse por OSS en otro Estado miembro, pero el NIF español puede seguir siendo necesario si hay un almacén en España, importaciones o EPR de envases. Díganos cómo vende y le indicaremos qué trámites aplican.',
            '外國公司向西班牙銷售，一定要有西班牙稅號（NIF）嗎？',
            '不一定每種情況都要，但如果在西班牙有稅務後果，通常需要。西班牙稅號是公司的稅務識別號碼（外國法人的號碼以 N 開頭）。辦理西班牙增值稅登記、在西班牙申請 EORI、在西班牙登記 OSS，或辦理西班牙包裝 EPR，一般都要先有稅號。向西班牙消費者做遠程銷售，有時可在另一個歐盟成員國透過 OSS 申報，但若在西班牙有倉庫、有進口，或要做包裝 EPR，仍然可能需要西班牙稅號。把銷售方式告訴我們，我們會說明要辦哪些手續。',
        ),
        Q(
            'What is the difference between a Spanish NIF, a VAT number, EORI and OSS?',
            'They are not the same thing. The NIF identifies the company for Spanish tax purposes. The NIF-IVA (VAT number, checked in VIES) is that same NIF used as a VAT identification number, usually written as ES plus the NIF, once the company is listed in the ROI. EORI is the customs identification number used in import and export declarations; having an EORI does not, by itself, allow intra-community VAT operations. OSS is an optional scheme for certain B2C services and distance sales, so that VAT can be declared in one Member State instead of registering in every country of consumption.',
            '¿Qué diferencia hay entre el NIF español, el número de IVA, el EORI y el OSS?',
            'No son lo mismo. El NIF identifica a la empresa a efectos fiscales en España. El NIF-IVA (número de IVA, comprobable en VIES) es ese mismo NIF usado como número de identificación a efectos de IVA, habitualmente ES más el NIF, una vez inscrita la empresa en el ROI. El EORI es el número de aduanas para declaraciones de importación y exportación; tener un EORI no habilita, por sí solo, las operaciones intracomunitarias de IVA. El OSS es un régimen opcional para determinados servicios B2C y ventas a distancia, que permite declarar el IVA en un solo Estado miembro en lugar de registrarse en cada país de consumo.',
            '西班牙稅號、增值稅號、EORI 和 OSS 有什麼分別？',
            '它們不是同一回事。NIF 是公司在西班牙的稅務識別號碼。NIF-IVA（增值稅號，可在 VIES 查核）是同一個稅號用作增值稅識別，通常寫成 ES 加 NIF，前提是公司已列入 ROI。EORI 是進出口報關用的海關識別號碼；有 EORI 本身並不代表可以做歐盟內部增值稅交易。OSS 是可選擇的制度，適用於部分 B2C 服務和遠程銷售，讓增值稅在一個成員國集中申報，而不必在每個消費國分別登記。',
        ),
        Q(
            'How long does a Spanish NIF take for a foreign company?',
            'In our experience the representative’s NIF and the company NIF are usually issued together in three to six weeks. There is no fixed statutory deadline; actual timing is set by the Spanish Tax Agency (AEAT). We state this as experience in the proposal and do not promise a fixed calendar date.',
            '¿Cuánto tarda el NIF español para una empresa extranjera?',
            'Según nuestra experiencia, el NIF del representante y el NIF de la empresa suelen expedirse juntos en tres a seis semanas. No hay un plazo legal fijo; el tiempo real lo determina la Agencia Tributaria (AEAT). Lo indicamos como experiencia en la propuesta y no prometemos una fecha concreta.',
            '外國公司申請西班牙稅號一般要多久？',
            '根據我們的經驗，代表人 NIF 與公司 NIF 通常一併在 3–6 周下達。沒有法定期限，實際時間由西班牙稅務局（AEAT）決定。我們會在方案中按經驗說明，不會承諾一個固定日期。',
        ),
        Q(
            'Do foreign companies need a fiscal representative in Spain?',
            'It depends on the activity — for example holding stock in Spain or certain VAT situations. Non-EU businesses with VAT obligations in Spain often need to appoint a fiscal representative (representante fiscal). We assess the case first and confirm in writing before you appoint us.',
            '¿Necesitan las empresas extranjeras un representante fiscal en España?',
            'Depende de la actividad —por ejemplo, tener stock en España o determinadas situaciones de IVA—. Las empresas de fuera de la UE con obligaciones de IVA en España suelen tener que nombrar un representante fiscal. Evaluamos el caso primero y lo confirmamos por escrito antes de que nos nombre.',
            '外國公司在西班牙一定要請財稅代表嗎？',
            '視業務而定，例如在西班牙存放庫存，或某些增值稅情形。在西班牙有增值稅義務的非歐盟企業，往往需要指定財稅代表（representante fiscal）。我們先評估，再書面確認，然後才辦理委任。',
        ),
        Q(
            'If I already use OSS, do I still need Spanish VAT registration?',
            'It depends what you do in Spain. OSS can cover certain B2C distance sales and services, declared in one Member State of identification. Holding stock in a Spanish warehouse usually means you must identify yourself for Spanish VAT even if some consumer sales are declared through OSS. Intra-community B2B supplies often require a NIF-IVA / ROI registration. We look at the sales model first and confirm in the written proposal which registrations you need.',
            'Si ya uso el OSS, ¿sigo necesitando el alta en el IVA español?',
            'Depende de lo que haga en España. El OSS puede cubrir determinadas ventas a distancia y servicios B2C, declarados en un solo Estado miembro de identificación. Tener stock en un almacén en España suele exigir identificarse a efectos de IVA español, aunque parte de las ventas a consumidores se declaren por OSS. Las entregas B2B intracomunitarias suelen requerir el NIF-IVA / ROI. Revisamos el modelo de venta y confirmamos en la propuesta qué registros necesita.',
            '已經用了 OSS，還要不要辦理西班牙增值稅登記？',
            '要看您在西班牙做什麼。OSS 可以涵蓋部分 B2C 遠程銷售和服務，在一個識別成員國集中申報。如果在西班牙倉庫存放庫存，即使部分對消費者的銷售已透過 OSS 申報，通常仍要做西班牙增值稅識別。歐盟內部 B2B 供貨往往還需要 NIF-IVA / ROI 登記。我們先看銷售模式，再在書面方案中確認要辦哪些登記。',
        ),
        Q(
            'Can a non-EU seller register for OSS in Spain?',
            'Yes. Spain can be the Member State of identification for OSS, including the non-Union scheme and, where it applies, the Import scheme (IOSS). To register in Spain you normally need a Spanish NIF first; Form 035 is a separate filing from the NIF/VAT census form (Modelo 036). OSS is optional. We can prepare the registration and, if you appoint us for it, the periodic OSS returns.',
            '¿Puede un vendedor de fuera de la UE registrarse en el OSS en España?',
            'Sí. España puede ser el Estado miembro de identificación del OSS, incluido el régimen de no establecidos en la Unión y, cuando proceda, el de importación (IOSS). Para registrarse en España normalmente hace falta un NIF español; el modelo 035 es un trámite distinto del censo NIF/IVA (modelo 036). El OSS es opcional. Podemos preparar el alta y, si nos lo encarga, las declaraciones periódicas.',
            '非歐盟賣家可以在西班牙登記 OSS 嗎？',
            '可以。西班牙可以作為 OSS 的識別成員國，包括非聯盟制度，以及適用時的進口制度（IOSS）。在西班牙登記通常要先有西班牙稅號；035 表是獨立手續，與稅號／增值稅普查表（036 表）分開遞交。OSS 是可選擇的。我們可以代為辦理登記；若您委任我們，也可以代為遞交定期 OSS 申報。',
        ),
        Q(
            'Do I need an EORI number?',
            'You need an EORI before you file customs declarations or apply for customs authorisations when importing into or exporting from the EU. In Spain the EORI is requested after the NIF has been assigned; for numbers starting with N, M, X or Y it is not issued automatically and must be requested in the AEAT electronic office. A Spanish EORI is usually ES followed by the NIF. An EORI is not a VAT number and does not replace VIES/ROI registration.',
            '¿Necesito un número EORI?',
            'El EORI hace falta antes de presentar declaraciones aduaneras o solicitar autorizaciones de aduanas al importar o exportar en la UE. En España se solicita después de asignado el NIF; si el NIF empieza por N, M, X o Y no se asigna automáticamente y hay que pedirlo en la sede electrónica de la AEAT. Un EORI español suele ser ES más el NIF. El EORI no es un número de IVA y no sustituye la inscripción en VIES/ROI.',
            '我需要 EORI 號碼嗎？',
            '如果要向歐盟進出口並辦理報關或申請海關授權，就需要先有 EORI。在西班牙，EORI 要在稅號下達之後申請；號碼以 N、M、X 或 Y 開頭的，不會自動獲配，必須在稅務局（AEAT）電子辦事處提出申請。西班牙 EORI 通常是 ES 加 NIF。EORI 不是增值稅號，也不能代替 VIES／ROI 登記。',
        ),
        Q(
            'Does Spain packaging EPR require a NIF? What about WEEE and batteries?',
            'Yes. Spain packaging EPR registration requires a Spanish NIF. WEEE and battery producer registrations in Spain do not. If you need packaging EPR, we usually obtain the NIF first (or prepare it together with the packaging file) and then complete the producer registration and scheme membership.',
            '¿El registro EPR de envases en España exige un NIF? ¿Y el RAEE o las pilas?',
            'Sí. El registro EPR de envases en España requiere un NIF español. Los registros de productor de RAEE y de pilas en España no lo exigen. Si necesita EPR de envases, normalmente obtenemos primero el NIF (o lo preparamos a la vez que el expediente de envases) y después completamos el registro de productor y la adhesión al sistema colectivo.',
            '西班牙包裝 EPR 一定要先有稅號嗎？WEEE 和電池呢？',
            '是。西班牙包裝 EPR 登記需要西班牙稅號；WEEE 和電池的生產者登記則不需要。如果您要辦包裝 EPR，我們通常會先取得稅號（或與包裝材料一併準備），再完成生產者登記和加入回收體系。',
        ),
        Q(
            'What do I need to sign for a Spanish NIF application?',
            'We draft the power of attorney and all application forms. In a typical case the director only signs the power of attorney before a notary and has it apostilled. We tell you in advance if company documents also need an apostille (companies in the EU, or with a VIES VAT number, are often exempt).',
            '¿Qué tengo que firmar para solicitar el NIF español?',
            'Redactamos el poder de representación y todos los formularios. En un caso habitual, el administrador solo firma el poder ante notario y lo apostilla. Le indicamos de antemano si los documentos societarios también necesitan apostilla (las empresas de la UE, o con un NIF-IVA en VIES, suelen estar exentas).',
            '申請西班牙稅號需要我簽什麼？',
            '授權書和全部申請表格由我們起草。通常只需董事在公證人面前簽署授權書並辦理海牙認證。若公司文件也需要海牙認證，我們會事先說明（歐盟公司或已有 VIES 增值稅號的公司，公司文件往往可免）。',
        ),
        Q(
            'If I only ask you to obtain a NIF, will you also file my VAT or OSS returns?',
            'No, not unless those filings are included in the proposal you accept. The NIF application covers obtaining the number, and VAT registration if you ask us to include it on the same census form. Quarterly VAT returns, OSS returns and fiscal representation are separate services. If you do not appoint us for them, we do not take on those ongoing tax filings.',
            'Si solo encargo el NIF, ¿también presentarán mis declaraciones de IVA o de OSS?',
            'No, salvo que esas declaraciones figuren en la propuesta que acepte. La solicitud de NIF cubre la obtención del número y, si lo pide, el alta en IVA en el mismo modelo censal. Las declaraciones trimestrales de IVA, las de OSS y la representación fiscal son servicios aparte. Si no nos las encarga, no asumimos esas obligaciones periódicas.',
            '如果只請你們辦理稅號，你們會一併申報增值稅或 OSS 嗎？',
            '不會，除非您接受的方案已包含這些申報。稅號申請只包括取得稅號；若您要求，也可以在同一張普查表一併辦理增值稅登記。季度增值稅申報、OSS 申報和財稅代表都是獨立服務。如果沒有委任我們，我們不會承擔這些後續稅務申報。',
        ),
    ],
    'product': [
        'do-i-need-eu-responsible-person-gpsr',
        Q(
            'Must the Responsible Person details appear on the online listing as well as on the label?',
            'Yes, for products covered by the General Product Safety Regulation (EU) 2023/988. Article 19 requires online offers to show the manufacturer’s details, the EU responsible person (when the manufacturer is not established in the EU), and product identification, together with the relevant warnings and safety information in the language of the country of sale. The details on the label, the packaging and the listing should match. A 2026 EU product-safety sweep found that many listings still missed one or more of these items.',
            '¿Los datos de la Persona Responsable deben aparecer también en el anuncio online, no solo en la etiqueta?',
            'Sí, en los productos cubiertos por el Reglamento (UE) 2023/988 (GPSR). El artículo 19 exige que las ofertas online indiquen los datos del fabricante, la persona responsable en la UE (si el fabricante no está establecido en la UE) y la identificación del producto, junto con las advertencias e información de seguridad en el idioma del país de venta. Los datos de la etiqueta, el envase y el anuncio deben coincidir. Un control de seguridad de productos de la UE en 2026 detectó que muchos anuncios seguían omitiendo alguno de estos elementos.',
            '歐盟負責人的資料，除了標籤，線上 listing 也要顯示嗎？',
            '要，適用《通用產品安全法規》（EU）2023/988（GPSR）的產品都要。第 19 條規定，線上銷售資料必須展示製造商資料、歐盟負責人（製造商不在歐盟境內時），以及產品識別資料，並附上銷售國語言的警示和安全說明。標籤、包裝和 listing 上的資料應保持一致。歐盟 2026 年產品安全抽查發現，不少 listing 仍缺少其中一項或幾項。',
        ),
        'gpsr-and-epr-one-provider',
        Q(
            'Who needs packaging EPR in Spain?',
            'If you place packaged products on the Spanish market — including by distance sales from another country — you are generally a packaging producer under Royal Decree 1055/2022, read together with the EU Packaging and Packaging Waste Regulation. You must register in the packaging section of the Registro de Productores de Producto, join a collective scheme and file periodic declarations. Businesses with no establishment in Spain normally appoint an authorised representative. A Spanish NIF is required for this registration.',
            '¿Quién tiene obligaciones EPR de envases en España?',
            'Si comercializa productos envasados en el mercado español —incluido por venta a distancia desde otro país— suele ser productor de envases según el Real Decreto 1055/2022, leído junto con el Reglamento europeo de envases y residuos de envases. Debe inscribirse en la sección de envases del Registro de Productores de Producto, adherirse a un sistema colectivo y presentar declaraciones periódicas. Quien no está establecido en España suele designar un representante autorizado. Este registro exige un NIF español.',
            '在西班牙，誰需要辦理包裝 EPR？',
            '如果您把帶包裝的產品投放西班牙市場——包括從其他國家做遠程銷售——根據皇家法令 1055/2022，並須同時參照歐盟包裝與包裝廢棄物法規，通常屬於包裝生產者。您必須在產品生產者登記系統（Registro de Productores de Producto）的包裝類別登記，加入回收體系，並做定期申報。在西班牙沒有設立實體的企業，一般要指定授權代表。這項登記需要西班牙稅號。',
        ),
        'weee-spain-authorised-representative-rii-aee',
        'battery-epr-built-in-batteries-spain',
        Q(
            'What is CPNP and who needs it?',
            'CPNP is the EU Cosmetic Products Notification Portal. Under Regulation (EC) No 1223/2009, a cosmetic product must be notified there before it is placed on the EU market, and it must have a responsible person established in the EU. We prepare and submit the CPNP notification from the product and formula information you provide. A safety assessment may also be required; we will tell you what the file must contain.',
            '¿Qué es el CPNP y quién lo necesita?',
            'CPNP es el Portal de Notificación de Productos Cosméticos de la UE. Según el Reglamento (CE) n.º 1223/2009, un cosmético debe notificarse allí antes de comercializarse en la UE, y debe tener una persona responsable establecida en la UE. Preparamos y presentamos la notificación CPNP a partir de la información del producto y de la fórmula que nos facilite. También puede ser necesario un informe de seguridad; le indicaremos qué debe incluir el expediente.',
            '什麼是 CPNP？哪些產品需要辦理？',
            'CPNP 是歐盟化妝品通報門戶。根據法規（EC）No 1223/2009，化妝品在投放歐盟市場前必須在該門戶通報，並須有一家設在歐盟的負責人。我們根據您提供的產品和配方資料，準備並提交 CPNP 通報。有時還需要安全評估；我們會說明檔案須包含哪些材料。',
        ),
        Q(
            'What is EPREL and which products need it?',
            'EPREL is the European Product Registry for Energy Labelling, set up under Regulation (EU) 2017/1369. Products that must carry an EU energy label — such as certain household appliances, lighting and electronic displays — have to be registered in EPREL before they are placed on the market or offered for sale online. We register the model and can act as the EU contact. The EPREL database itself does not charge an official fee.',
            '¿Qué es EPREL y qué productos lo necesitan?',
            'EPREL es el registro europeo de productos para el etiquetado energético, creado por el Reglamento (UE) 2017/1369. Los productos que deben llevar etiqueta energética de la UE —como determinados electrodomésticos, alumbrado y pantallas— tienen que registrarse en EPREL antes de comercializarse o anunciarse online. Registramos el modelo y podemos actuar como contacto en la UE. La base de datos EPREL no cobra una tasa oficial.',
            '什麼是 EPREL？哪些產品要登記？',
            'EPREL 是歐洲能源標籤產品登記庫，依據法規（EU）2017/1369 設立。必須附有歐盟能源標籤的產品——例如部分家電、照明和電子顯示設備——在投放市場或在線上出售前，都要先在 EPREL 登記。我們可以辦理型號登記，並擔任歐盟聯絡人。EPREL 資料庫本身不收取官方費用。',
        ),
        Q(
            'Do I need a separate UK Responsible Person if I already have one in the EU?',
            'Yes, if you sell in Great Britain and UK product rules require a UK-established responsible person or authorised representative. An EU Responsible Person under GPSR does not, by itself, cover Great Britain, because UK product law is a separate system. We can act as UK Responsible Person or authorised representative where that appointment is required. Northern Ireland follows specific arrangements; we confirm the scope in the proposal.',
            'Si ya tengo Persona Responsable en la UE, ¿necesito otra en el Reino Unido?',
            'Sí, si vende en Gran Bretaña y la normativa británica exige una persona responsable o un representante autorizado establecido en el Reino Unido. Una Persona Responsable en la UE conforme al GPSR no cubre, por sí sola, Gran Bretaña, porque el Derecho de producto del Reino Unido es un sistema distinto. Podemos actuar como persona responsable o representante autorizado en el Reino Unido cuando proceda. Irlanda del Norte tiene un régimen específico; confirmamos el alcance en la propuesta.',
            '已經有歐盟負責人，還需要另行指定英國負責人嗎？',
            '如果您在大不列顛銷售，而英國產品法規要求指定設在英國的負責人或授權代表，就需要另行委任。GPSR 下的歐盟負責人本身並不覆蓋大不列顛，因為英國產品法律是另一套制度。在需要這項委任時，我們可以擔任英國負責人或授權代表。北愛爾蘭有專門安排，範圍會在方案中確認。',
        ),
        Q(
            'Do you prepare the EU Declaration of Conformity?',
            'Yes, we can draft the EU Declaration of Conformity and the related mandates where the product falls under EU harmonisation legislation. You review the draft, then sign and stamp it; the manufacturer remains responsible for the product and for the accuracy of the technical documentation. A test report or a “CE certificate” from a laboratory is not a Declaration of Conformity. Marketplaces often ask the EU responsible person named on the listing to produce the DoC.',
            '¿Redactan la declaración UE de conformidad?',
            'Sí. Podemos redactar la declaración UE de conformidad y los mandatos relacionados cuando el producto está sujeto a la legislación de armonización de la Unión. Usted revisa el borrador y solo tiene que firmarlo y sellarlo; el fabricante sigue siendo responsable del producto y de la exactitud de la documentación técnica. Un informe de ensayo o un «certificado CE» de un laboratorio no es una declaración de conformidad. Los marketplaces suelen pedir la DoC a la persona responsable que figura en el anuncio.',
            '你們會代為起草歐盟符合性聲明（DoC）嗎？',
            '會。若產品屬歐盟協調立法範圍，我們可以起草歐盟符合性聲明及相關授權文件。您審閱草稿後只需簽字蓋章；產品本身和技術文件的準確性，仍由製造商負責。實驗室的測試報告或「CE 證書」並不是符合性聲明。平台常常會向 listing 上的歐盟負責人索取 DoC。',
        ),
    ],
    'fees': [
        'how-to-get-eu-compliance-quote',
        Q(
            'What documents do you need from me?',
            'It depends on the service, and we send a single checklist once you accept the proposal. We usually need your company details, a product list with photos and the current label or packaging artwork, the countries and marketplaces you sell in, and any existing certificates, test reports or registration numbers. For a Spanish NIF we tell you in advance which documents must be signed before a notary or apostilled. We review the file and flag any gaps before filing.',
            '¿Qué documentos necesitan de mí?',
            'Depende del servicio; enviamos una única lista de documentos cuando acepta la propuesta. Habitualmente necesitamos los datos de la empresa, un listado de productos con fotos y el arte actual de la etiqueta o el envase, los países y marketplaces de venta, y los certificados, informes de ensayo o números de registro que ya tenga. Para un NIF español le indicamos de antemano qué documentos deben firmarse ante notario o apostillarse. Revisamos el expediente y señalamos las lagunas antes de presentarlo.',
            '我需要準備哪些資料？',
            '視具體服務而定。您接受方案後，我們會一次過發出資料清單。通常需要公司資料、產品清單（最好附圖片和現用標籤或包裝圖稿）、銷售國家和平台，以及已有的證書、測試報告或登記號碼。辦理西班牙稅號時，我們會事先說明哪些文件須在公證人面前簽署或辦理海牙認證。遞交前我們會審核檔案並指出缺漏。',
        ),
        Q(
            'Who prepares the mandates, forms and the Declaration of Conformity?',
            'We draft the mandates, application forms, powers of attorney and, where applicable, the EU Declaration of Conformity. You review them and only need to sign and stamp. We ask for the information we need in one checklist so you are not chased piece by piece.',
            '¿Quién prepara los mandatos, los formularios y la declaración de conformidad?',
            'Redactamos los mandatos, los formularios, los poderes y, cuando proceda, la declaración UE de conformidad. Usted los revisa y solo tiene que firmar y sellar. Pedimos la información necesaria en una sola lista, para no ir pidiendo documentos uno a uno.',
            '授權書、申請表和符合性聲明由誰起草？',
            '授權書、申請表格、委託書，以及適用時的歐盟符合性聲明，都由我們起草。您審閱後只需簽字蓋章。我們會在一份清單裏一次問齊所需資料，避免反覆補件。',
        ),
        Q(
            'How long does the work take?',
            'It depends on the service and on the authority or collective scheme. In our experience a Spanish NIF for a foreign company is usually issued in three to six weeks; there is no fixed statutory deadline, and the Spanish Tax Agency (AEAT) sets the actual timing. We state the expected timing in the written proposal and do not promise a fixed calendar date.',
            '¿Cuánto tardan los trámites?',
            'Depende del servicio y de la autoridad o el sistema colectivo. Según nuestra experiencia, el NIF español de una empresa extranjera suele expedirse en tres a seis semanas; no hay un plazo legal fijo y el tiempo real lo determina la AEAT. Indicamos el plazo previsto en la propuesta escrita y no prometemos una fecha concreta.',
            '辦理一般要多久？',
            '視服務種類以及主管機構或回收體系而定。根據我們的經驗，外國公司的西班牙稅號通常在 3–6 周下達；沒有法定期限，實際時間由西班牙稅務局（AEAT）決定。我們會在書面方案中說明預計時間，不會承諾一個固定日期。',
        ),
        Q(
            'When do you invoice?',
            'Our service fee for a registration is invoiced once the registration is completed or while it is in progress. Official fees and collective-scheme contributions are charged by the authorities or schemes and are invoiced separately, at cost, after we have told you the amount.',
            '¿Cuándo facturan?',
            'Nuestros honorarios por un registro se facturan cuando el trámite ha concluido o está en curso. Las tasas oficiales y las aportaciones a los sistemas colectivos las cobran las autoridades o los sistemas, y se las facturamos aparte, a coste, después de indicarle el importe.',
            '什麼時候開票？',
            '登記類服務費在辦理完成或辦理中開票。官方費用和回收體系繳費由主管機構或體系收取，我們會先告知金額，再按實收另行開票。',
        ),
        Q(
            'Are official fees and scheme fees included in your service fee?',
            'No. The service fee is IberTrust’s fee for the work. Official fees and contributions to collective schemes (PROs) are charged by the authority or the scheme and passed on at cost; if they change, the amount we invoice for them changes too. We tell you those amounts before we charge them, and we do not add a separate administration charge on top of the agreed service fee.',
            '¿Las tasas oficiales y las aportaciones a los sistemas colectivos están incluidas en los honorarios?',
            'No. Los honorarios son la retribución de IberTrust por el trabajo. Las tasas oficiales y las aportaciones a los sistemas colectivos (SCRAP) las cobran la autoridad o el sistema y se repercuten a coste; si cambian, cambia también el importe facturado. Le indicamos esos importes antes de cobrarlos, y no añadimos un cargo administrativo aparte sobre los honorarios acordados.',
            '官方費用和回收體系費用包不包括在服務費裏？',
            '不包括。服務費是 IberTrust 的工作報酬。官方費用和回收體系（PRO）繳費由主管機構或體系收取，我們按實收轉給您；若官方調整，開票金額也隨之調整。收費前我們會先告知金額，也不會在已約定的服務費之外另收行政費。',
        ),
        'compliance-support-in-chinese-english-spanish',
        Q(
            'How experienced is your team?',
            'Our team members come from Spain and China. Since 2011 they have worked in cross-border import-export, online e-commerce trade and product compliance, and they have extensive experience in these areas. The team has handled 50,000+ ASIN-level EU Responsible Person requests via Amazon Compliance Central and has served 400+ cross-border e-commerce sellers.',
            '¿Qué experiencia tiene el equipo?',
            'Los miembros de nuestro equipo proceden de España y de China. Desde 2011 se dedican al comercio transfronterizo de importación y exportación, al e-commerce online y al cumplimiento de producto, y cuentan con una amplia experiencia en estos ámbitos. El equipo ha gestionado 50,000+ solicitudes de Persona Responsable en la UE a nivel de ASIN a través de Amazon Compliance Central, y ha dado servicio a 400+ vendedores de e-commerce transfronterizo.',
            '團隊有什麼經驗？',
            '團隊成員來自西班牙和中國，自 2011 年起從事跨境進出口、線上電商貿易和產品合規，經驗豐富。我們團隊已通過 Amazon Compliance Central 處理 50,000+ 條 ASIN 級歐盟負責人申請，並已為 400+ 跨境電商賣家提供服務。',
        ),
    ],
}

GROUP_ORDER = ('tax', 'product', 'fees')


def _plain(text):
    return re.sub(r'<[^>]+>', '', text)


def render(lang, prefix, faqs, more_label):
    """Return (html, faqpage_jsonld) for the FAQ page in one language."""
    by_slug = {slug: entry for slug, entry in faqs}
    items_for_ld = []
    parts = [f'<p class="faq-lead">{LEAD[lang]}</p>']
    for key in GROUP_ORDER:
        parts.append(f'<div class="faq-group" id="faq-{key}"><h2>{GROUP_TITLE[key][lang]}</h2>')
        for item in GROUPS[key]:
            if isinstance(item, str):
                entry = by_slug[item]
                q, a = entry[lang][0], entry[lang][1]
                if item in OVERRIDES and lang in OVERRIDES[item]:
                    q, a = OVERRIDES[item][lang]
                parts.append(
                    f'<details><summary>{q}</summary><p>{a}</p>'
                    f'<p><a href="{prefix}/blog/{item}.html">{more_label} →</a></p></details>'
                )
            else:
                q, a = item[lang]
                parts.append(f'<details><summary>{q}</summary><p>{a}</p></details>')
            items_for_ld.append((q, a))
        parts.append('</div>')
    html = ''.join(parts)
    ld = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': [
            {
                '@type': 'Question',
                'name': q,
                'acceptedAnswer': {'@type': 'Answer', 'text': _plain(a)},
            }
            for q, a in items_for_ld
        ],
    }
    return html, ld
