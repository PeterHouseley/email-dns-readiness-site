from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1120' height='740' viewBox='0 0 1120 740' role='img' aria-labelledby='title desc'>
  <title id='title'>Email DNS readiness routing map</title>
  <desc id='desc'>A stylised infrastructure map showing domain DNS records flowing through SPF, DKIM and DMARC checks before mail reaches customer inboxes.</desc>
  <defs>
    <filter id='shadow' x='-20%' y='-20%' width='140%' height='150%'>
      <feDropShadow dx='0' dy='22' stdDeviation='18' flood-color='#101827' flood-opacity='.18'/>
    </filter>
    <pattern id='grid' width='42' height='42' patternUnits='userSpaceOnUse'>
      <path d='M42 0H0v42' fill='none' stroke='#1d3557' stroke-opacity='.09' stroke-width='1'/>
    </pattern>
    <linearGradient id='paper' x1='0' x2='1' y1='0' y2='1'>
      <stop offset='0' stop-color='#fbfaf4'/><stop offset='1' stop-color='#e9efe9'/>
    </linearGradient>
    <linearGradient id='ink' x1='0' x2='1'>
      <stop offset='0' stop-color='#173047'/><stop offset='1' stop-color='#376b5a'/>
    </linearGradient>
  </defs>
  <rect width='1120' height='740' rx='42' fill='#eef2ec'/>
  <rect x='28' y='28' width='1064' height='684' rx='34' fill='url(#grid)'/>
  <g filter='url(#shadow)'>
    <rect x='72' y='84' width='294' height='520' rx='28' fill='url(#paper)' stroke='#162238' stroke-opacity='.18'/>
    <rect x='412' y='84' width='294' height='520' rx='28' fill='url(#paper)' stroke='#162238' stroke-opacity='.18'/>
    <rect x='752' y='84' width='294' height='520' rx='28' fill='url(#paper)' stroke='#162238' stroke-opacity='.18'/>
  </g>
  <text x='96' y='132' font-family='Georgia,serif' font-size='31' font-weight='700' fill='#142033'>public DNS</text>
  <text x='436' y='132' font-family='Georgia,serif' font-size='31' font-weight='700' fill='#142033'>authentication</text>
  <text x='776' y='132' font-family='Georgia,serif' font-size='31' font-weight='700' fill='#142033'>trust handoff</text>
  <g font-family='ui-monospace, Menlo, Consolas, monospace' font-size='22' fill='#21334a'>
    <rect x='100' y='176' width='232' height='70' rx='16' fill='#fffdf7' stroke='#2f4d69' stroke-opacity='.22'/>
    <text x='122' y='219'>TXT  SPF</text>
    <rect x='100' y='274' width='232' height='70' rx='16' fill='#fffdf7' stroke='#2f4d69' stroke-opacity='.22'/>
    <text x='122' y='317'>CNAME  DKIM</text>
    <rect x='100' y='372' width='232' height='70' rx='16' fill='#fffdf7' stroke='#2f4d69' stroke-opacity='.22'/>
    <text x='122' y='415'>TXT  DMARC</text>
    <rect x='100' y='470' width='232' height='70' rx='16' fill='#fffdf7' stroke='#2f4d69' stroke-opacity='.22'/>
    <text x='122' y='513'>MX  provider</text>
  </g>
  <g stroke='url(#ink)' stroke-width='5' fill='none' stroke-linecap='round' stroke-linejoin='round'>
    <path d='M348 211 C386 211 389 211 427 211'/>
    <path d='M348 309 C386 309 389 309 427 309'/>
    <path d='M348 407 C386 407 389 407 427 407'/>
    <path d='M688 309 C723 309 735 309 770 309'/>
  </g>
  <g font-family='ui-sans-serif, system-ui, sans-serif' font-size='21' fill='#15243a'>
    <circle cx='559' cy='214' r='46' fill='#d9eadf' stroke='#1e6b4e' stroke-width='4'/><text x='533' y='221' font-weight='800'>SPF</text>
    <circle cx='559' cy='329' r='46' fill='#e8e1c7' stroke='#8b6d18' stroke-width='4'/><text x='529' y='336' font-weight='800'>DKIM</text>
    <circle cx='559' cy='444' r='46' fill='#f0d9d2' stroke='#9a4537' stroke-width='4'/><text x='520' y='451' font-weight='800'>DMARC</text>
  </g>
  <g font-family='Georgia,serif' fill='#142033'>
    <path d='M835 194h142v246c0 37-24 70-71 98-47-28-71-61-71-98z' fill='#fffdf7' stroke='#173047' stroke-width='5'/>
    <path d='M872 342l31 31 68-91' stroke='#2f745d' stroke-width='14' fill='none' stroke-linecap='round' stroke-linejoin='round'/>
    <text x='817' y='546' font-size='28' font-weight='700'>clear fix list</text>
  </g>
  <g font-family='ui-monospace, Menlo, Consolas, monospace' font-size='17' fill='#536172'>
    <text x='95' y='645'>lookup evidence, no passwords</text>
    <text x='435' y='645'>red / amber / green scoring</text>
    <text x='774' y='645'>safe notes for DNS editor</text>
  </g>
</svg>
"""

meter_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='560' viewBox='0 0 1180 560' role='img' aria-labelledby='meterTitle meterDesc'>
  <title id='meterTitle'>Email authentication readiness meter</title>
  <desc id='meterDesc'>A premium operational trust board showing SPF, DKIM, DMARC and provider alignment as a staged readiness ladder.</desc>
  <defs>
    <filter id='soft' x='-15%' y='-20%' width='130%' height='145%'><feDropShadow dx='0' dy='18' stdDeviation='16' flood-color='#0f1f2d' flood-opacity='.16'/></filter>
    <pattern id='mesh' width='36' height='36' patternUnits='userSpaceOnUse'><path d='M36 0H0v36' fill='none' stroke='#173047' stroke-opacity='.07'/></pattern>
    <linearGradient id='brass' x1='0' x2='1'><stop offset='0' stop-color='#d7b75d'/><stop offset='1' stop-color='#9c7a28'/></linearGradient>
  </defs>
  <rect width='1180' height='560' rx='40' fill='#f4f1e6'/>
  <rect x='24' y='24' width='1132' height='512' rx='32' fill='url(#mesh)'/>
  <g filter='url(#soft)'>
    <rect x='70' y='70' width='1040' height='410' rx='30' fill='#fffdf7' stroke='#173047' stroke-opacity='.16'/>
  </g>
  <g font-family='Georgia,serif' fill='#132338'>
    <text x='104' y='124' font-size='38' font-weight='700'>authentication readiness board</text>
    <text x='104' y='162' font-size='20' fill='#536172'>public record evidence translated into one safe operating decision</text>
  </g>
  <g transform='translate(104 218)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <line x1='0' y1='88' x2='888' y2='88' stroke='#d8d4c3' stroke-width='18' stroke-linecap='round'/>
    <line x1='0' y1='88' x2='628' y2='88' stroke='#2f745d' stroke-width='18' stroke-linecap='round'/>
    <g fill='#fffdf7' stroke-width='5'>
      <circle cx='0' cy='88' r='44' stroke='#2f745d'/>
      <circle cx='296' cy='88' r='44' stroke='#2f745d'/>
      <circle cx='592' cy='88' r='44' stroke='#c89d2c'/>
      <circle cx='888' cy='88' r='44' stroke='#9a4537'/>
    </g>
    <g fill='#132338' font-weight='900' font-size='18' text-anchor='middle'>
      <text x='0' y='95'>SPF</text><text x='296' y='95'>DKIM</text><text x='592' y='95'>DMARC</text><text x='888' y='95'>ALIGN</text>
    </g>
    <g fill='#536172' font-size='17' text-anchor='middle'>
      <text x='0' y='166'>who can send</text><text x='296' y='166'>message signature</text><text x='592' y='166'>domain policy</text><text x='888' y='166'>safe rollout</text>
    </g>
  </g>
  <g transform='translate(826 92)' font-family='ui-monospace, Menlo, Consolas, monospace'>
    <rect x='0' y='0' width='250' height='90' rx='18' fill='#173047'/>
    <text x='24' y='36' fill='#9fcbb9' font-size='18'>STATUS: AMBER</text>
    <text x='24' y='66' fill='#fffdf7' font-size='16'>actionable, not urgent panic</text>
  </g>
  <g font-family='ui-sans-serif, system-ui, sans-serif' font-size='18' fill='#132338'>
    <rect x='104' y='405' width='304' height='42' rx='21' fill='#edf5ef' stroke='#2f745d' stroke-opacity='.24'/><text x='126' y='432'>no logins requested</text>
    <rect x='438' y='405' width='304' height='42' rx='21' fill='#f5efd8' stroke='url(#brass)' stroke-opacity='.38'/><text x='460' y='432'>DNS editor handoff note</text>
    <rect x='772' y='405' width='304' height='42' rx='21' fill='#f2e2dc' stroke='#9a4537' stroke-opacity='.24'/><text x='794' y='432'>change risk called out</text>
  </g>
</svg>
"""

resolver_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='650' viewBox='0 0 1180 650' role='img' aria-labelledby='resolverTitle resolverDesc'>
  <title id='resolverTitle'>Public resolver verification receipt</title>
  <desc id='resolverDesc'>A professional DNS verification receipt showing SPF, DKIM and DMARC records checked across Google, Cloudflare and authoritative DNS before a client handoff.</desc>
  <defs>
    <filter id='receiptShadow' x='-18%' y='-20%' width='136%' height='145%'><feDropShadow dx='0' dy='20' stdDeviation='18' flood-color='#0b1f2a' flood-opacity='.22'/></filter>
    <pattern id='resolverGrid' width='38' height='38' patternUnits='userSpaceOnUse'><path d='M38 0H0v38' fill='none' stroke='#d6e3dd' stroke-opacity='.18'/></pattern>
    <linearGradient id='resolverInk' x1='0' x2='1'><stop offset='0' stop-color='#163348'/><stop offset='1' stop-color='#2f745d'/></linearGradient>
  </defs>
  <rect width='1180' height='650' rx='44' fill='#081a22'/>
  <rect x='28' y='28' width='1124' height='594' rx='34' fill='url(#resolverGrid)' stroke='#9ed9ca' stroke-opacity='.15'/>
  <g filter='url(#receiptShadow)'>
    <rect x='78' y='72' width='1024' height='506' rx='32' fill='#fffdf7'/>
  </g>
  <g font-family='Georgia,serif' fill='#132338'>
    <text x='118' y='132' font-size='40' font-weight='700'>resolver verification receipt</text>
    <text x='118' y='170' font-size='20' fill='#596879'>evidence that the fix list was checked outside the client inbox thread</text>
  </g>
  <g transform='translate(118 218)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <rect width='944' height='64' rx='16' fill='url(#resolverInk)'/>
    <g fill='#e9fbf8' font-size='15' font-weight='900' letter-spacing='.08em'>
      <text x='24' y='40'>CHECK</text><text x='258' y='40'>GOOGLE 8.8.8.8</text><text x='504' y='40'>CLOUDFLARE 1.1.1.1</text><text x='756' y='40'>AUTHORITATIVE</text>
    </g>
    <g font-size='18' fill='#132338'>
      <g transform='translate(0 86)'>
        <rect width='944' height='58' rx='14' fill='#eef6f1'/><text x='24' y='36' font-weight='900'>SPF TXT</text><text x='278' y='36'>single record</text><text x='526' y='36'>single record</text><text x='784' y='36' fill='#2f745d' font-weight='900'>PASS</text>
      </g>
      <g transform='translate(0 158)'>
        <rect width='944' height='58' rx='14' fill='#f7efd7'/><text x='24' y='36' font-weight='900'>DKIM selector</text><text x='278' y='36'>provider clue</text><text x='526' y='36'>needs confirm</text><text x='784' y='36' fill='#9c721d' font-weight='900'>AMBER</text>
      </g>
      <g transform='translate(0 230)'>
        <rect width='944' height='58' rx='14' fill='#f1ded8'/><text x='24' y='36' font-weight='900'>DMARC TXT</text><text x='278' y='36'>p=none</text><text x='526' y='36'>p=none</text><text x='784' y='36' fill='#98493b' font-weight='900'>POLICY GAP</text>
      </g>
    </g>
    <g transform='translate(0 330)' font-family='ui-monospace, Menlo, Consolas, monospace'>
      <rect width='944' height='70' rx='18' fill='#173047'/>
      <text x='24' y='30' fill='#a7d8ca' font-size='16'>HANDOFF NOTE</text>
      <text x='24' y='52' fill='#fffdf7' font-size='17'>No DNS credentials requested · owner approves edits · after-change receipt included</text>
    </g>
  </g>
</svg>
"""

incident_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='650' viewBox='0 0 1180 650' role='img' aria-labelledby='incidentTitle incidentDesc'>
  <title id='incidentTitle'>Email trust incident drill</title>
  <desc id='incidentDesc'>A dark infrastructure-style incident drill showing quiet leads, DNS evidence, resolver checks and a safe repair order for email authentication.</desc>
  <defs>
    <filter id='glow' x='-20%' y='-20%' width='140%' height='150%'><feDropShadow dx='0' dy='18' stdDeviation='16' flood-color='#000814' flood-opacity='.34'/></filter>
    <pattern id='rack' width='46' height='46' patternUnits='userSpaceOnUse'><path d='M46 0H0v46' fill='none' stroke='#9ed9ca' stroke-opacity='.08'/></pattern>
    <linearGradient id='amber' x1='0' x2='1'><stop offset='0' stop-color='#ffd36e'/><stop offset='1' stop-color='#b77a24'/></linearGradient>
    <linearGradient id='green' x1='0' x2='1'><stop offset='0' stop-color='#72e2a3'/><stop offset='1' stop-color='#2f745d'/></linearGradient>
  </defs>
  <rect width='1180' height='650' rx='44' fill='#06161d'/>
  <rect x='28' y='28' width='1124' height='594' rx='34' fill='url(#rack)' stroke='#9ed9ca' stroke-opacity='.16'/>
  <g font-family='Georgia,serif' fill='#e9fbf8'>
    <text x='72' y='92' font-size='38' font-weight='700'>email trust incident drill</text>
    <text x='72' y='130' font-size='20' fill='#a7d8ca'>when replies go quiet, public records become the first evidence room</text>
  </g>
  <g filter='url(#glow)'>
    <rect x='72' y='174' width='250' height='338' rx='28' fill='#102f38' stroke='#9ed9ca' stroke-opacity='.22'/>
    <rect x='374' y='174' width='432' height='338' rx='28' fill='#fffdf7'/>
    <rect x='858' y='174' width='250' height='338' rx='28' fill='#102f38' stroke='#9ed9ca' stroke-opacity='.22'/>
  </g>
  <g font-family='ui-monospace, Menlo, Consolas, monospace' font-size='17' font-weight='900'>
    <text x='100' y='222' fill='#ffd36e'>SYMPTOM</text>
    <text x='402' y='222' fill='#173047'>PUBLIC EVIDENCE</text>
    <text x='886' y='222' fill='#72e2a3'>REPAIR ORDER</text>
  </g>
  <g font-family='ui-sans-serif, system-ui, sans-serif'>
    <g fill='#e9fbf8' font-size='24' font-weight='800'>
      <text x='100' y='282'>quotes silent</text><text x='100' y='336'>invoice concern</text><text x='100' y='390'>platform change</text>
    </g>
    <g fill='#a7d8ca' font-size='16'><text x='100' y='462'>no inbox access required</text></g>
    <g transform='translate(402 258)' font-size='18' fill='#132338'>
      <rect width='376' height='56' rx='15' fill='#eef6f1'/><text x='22' y='36' font-weight='900'>SPF</text><text x='132' y='36'>single sender chain?</text>
      <rect y='74' width='376' height='56' rx='15' fill='#f7efd7'/><text x='22' y='110' font-weight='900'>DKIM</text><text x='132' y='110'>selector evidence?</text>
      <rect y='148' width='376' height='56' rx='15' fill='#f1ded8'/><text x='22' y='184' font-weight='900'>DMARC</text><text x='132' y='184'>policy and reports?</text>
    </g>
    <g fill='none' stroke-width='5' stroke-linecap='round'>
      <path d='M322 342 C350 342 346 342 374 342' stroke='url(#amber)'/>
      <path d='M806 342 C834 342 830 342 858 342' stroke='url(#green)'/>
    </g>
    <g transform='translate(886 268)' font-size='19' fill='#e9fbf8' font-weight='850'>
      <text y='0'>1. freeze assumptions</text>
      <text y='54'>2. verify resolvers</text>
      <text y='108'>3. rank DNS edits</text>
      <text y='162'>4. issue receipt</text>
    </g>
  </g>
  <g font-family='ui-monospace, Menlo, Consolas, monospace'>
    <rect x='72' y='546' width='1036' height='54' rx='18' fill='#0c2730' stroke='#9ed9ca' stroke-opacity='.2'/>
    <text x='100' y='580' font-size='17' fill='#a7d8ca'>OWNER-SAFE: domain name + known sender platforms only · no passwords · no DNS edits without approval</text>
  </g>
</svg>
"""


tls_seal_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='700' viewBox='0 0 1180 700' role='img' aria-labelledby='sealTitle sealDesc'>
  <title id='sealTitle'>Email domain trust seal and sending lane chart</title>
  <desc id='sealDesc'>A premium infrastructure-style email trust seal showing SPF, DKIM, DMARC, MX and resolver evidence flowing into a client-safe handoff pack.</desc>
  <defs>
    <filter id='deepShadow' x='-18%' y='-18%' width='136%' height='140%'><feDropShadow dx='0' dy='24' stdDeviation='20' flood-color='#04131a' flood-opacity='.32'/></filter>
    <filter id='stampBlur'><feGaussianBlur stdDeviation='10'/></filter>
    <pattern id='tinyGrid' width='30' height='30' patternUnits='userSpaceOnUse'><path d='M30 0H0v30' fill='none' stroke='#94d8c9' stroke-opacity='.12'/></pattern>
    <linearGradient id='lane' x1='0' x2='1'><stop offset='0' stop-color='#72e2a3'/><stop offset='.55' stop-color='#ffd36e'/><stop offset='1' stop-color='#ff8f83'/></linearGradient>
    <linearGradient id='slate' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#0a1d25'/><stop offset='1' stop-color='#163d39'/></linearGradient>
  </defs>
  <rect width='1180' height='700' rx='46' fill='#071a22'/>
  <rect x='28' y='28' width='1124' height='644' rx='34' fill='url(#tinyGrid)' stroke='#9ed9ca' stroke-opacity='.16'/>
  <circle cx='900' cy='120' r='180' fill='#46d6b1' opacity='.14' filter='url(#stampBlur)'/>
  <g filter='url(#deepShadow)'>
    <rect x='70' y='70' width='1040' height='560' rx='34' fill='url(#slate)' stroke='#9ed9ca' stroke-opacity='.22'/>
  </g>
  <g font-family='Georgia,serif'>
    <text x='112' y='134' fill='#e9fbf8' font-size='44' font-weight='700'>domain trust seal</text>
    <text x='112' y='174' fill='#a8d8ce' font-size='21'>a client-readable proof pack for authentication, routing and safe change control</text>
  </g>
  <g transform='translate(112 226)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <rect x='0' y='0' width='956' height='104' rx='26' fill='#ffffff' fill-opacity='.07' stroke='#9ed9ca' stroke-opacity='.22'/>
    <path d='M64 52H884' stroke='url(#lane)' stroke-width='10' stroke-linecap='round'/>
    <g font-weight='950' font-size='16' text-anchor='middle'>
      <g transform='translate(64 52)'><circle r='31' fill='#0d2a2a' stroke='#72e2a3' stroke-width='5'/><text y='6' fill='#e9fbf8'>SPF</text></g>
      <g transform='translate(269 52)'><circle r='31' fill='#0d2a2a' stroke='#72e2a3' stroke-width='5'/><text y='6' fill='#e9fbf8'>MX</text></g>
      <g transform='translate(474 52)'><circle r='31' fill='#0d2a2a' stroke='#ffd36e' stroke-width='5'/><text y='6' fill='#e9fbf8'>DKIM</text></g>
      <g transform='translate(679 52)'><circle r='31' fill='#0d2a2a' stroke='#ffd36e' stroke-width='5'/><text y='6' fill='#e9fbf8'>DMARC</text></g>
      <g transform='translate(884 52)'><circle r='31' fill='#0d2a2a' stroke='#ff8f83' stroke-width='5'/><text y='6' fill='#e9fbf8'>ALIGN</text></g>
    </g>
  </g>
  <g transform='translate(112 382)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <g>
      <rect width='292' height='138' rx='24' fill='#fffdf7'/>
      <text x='24' y='38' font-size='15' font-weight='950' letter-spacing='.12em' fill='#2f745d'>EVIDENCE</text>
      <text x='24' y='76' font-size='25' font-weight='900' fill='#132338'>public records only</text>
      <text x='24' y='108' font-size='17' fill='#536172'>No DNS login, no mailbox access.</text>
    </g>
    <g transform='translate(332 0)'>
      <rect width='292' height='138' rx='24' fill='#fff7de'/>
      <text x='24' y='38' font-size='15' font-weight='950' letter-spacing='.12em' fill='#9c721d'>CHANGE ORDER</text>
      <text x='24' y='76' font-size='25' font-weight='900' fill='#132338'>safe edit sequence</text>
      <text x='24' y='108' font-size='17' fill='#6f5a2a'>Risk called out before action.</text>
    </g>
    <g transform='translate(664 0)'>
      <rect width='292' height='138' rx='24' fill='#eaf7f2'/>
      <text x='24' y='38' font-size='15' font-weight='950' letter-spacing='.12em' fill='#2f745d'>RECEIPT</text>
      <text x='24' y='76' font-size='25' font-weight='900' fill='#132338'>resolver readback</text>
      <text x='24' y='108' font-size='17' fill='#536172'>Google, Cloudflare, authoritative.</text>
    </g>
  </g>
  <g transform='translate(830 96) rotate(-8)' font-family='ui-monospace, Menlo, Consolas, monospace'>
    <circle cx='110' cy='110' r='92' fill='none' stroke='#ffd36e' stroke-width='5' stroke-dasharray='8 7'/>
    <circle cx='110' cy='110' r='68' fill='#ffd36e' fill-opacity='.08' stroke='#ffd36e' stroke-width='2'/>
    <text x='110' y='96' text-anchor='middle' fill='#ffd36e' font-size='16' font-weight='950'>CLIENT SAFE</text>
    <text x='110' y='122' text-anchor='middle' fill='#e9fbf8' font-size='24' font-weight='950'>HANDOFF</text>
    <text x='110' y='148' text-anchor='middle' fill='#a8d8ce' font-size='13' font-weight='900'>NO PASSWORDS</text>
  </g>
  <g transform='translate(112 558)' font-family='ui-monospace, Menlo, Consolas, monospace'>
    <rect width='956' height='42' rx='21' fill='#ffffff' fill-opacity='.08' stroke='#9ed9ca' stroke-opacity='.18'/>
    <text x='26' y='27' fill='#a8d8ce' font-size='16'>trust route: lookup → diagnose → owner approves → DNS editor changes → resolver receipt</text>
  </g>
</svg>
"""
sender_inventory_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='700' viewBox='0 0 1180 700' role='img' aria-labelledby='inventoryTitle inventoryDesc'>
  <title id='inventoryTitle'>Sender inventory manifest</title>
  <desc id='inventoryDesc'>A professional infrastructure manifest showing business email senders checked against SPF, DKIM, DMARC and owner-approved DNS changes.</desc>
  <defs>
    <filter id='manifestShadow' x='-18%' y='-18%' width='136%' height='140%'><feDropShadow dx='0' dy='26' stdDeviation='22' flood-color='#06141b' flood-opacity='.28'/></filter>
    <pattern id='ledgerGrid' width='34' height='34' patternUnits='userSpaceOnUse'><path d='M34 0H0v34' fill='none' stroke='#173047' stroke-opacity='.065'/></pattern>
    <linearGradient id='laneGreen' x1='0' x2='1'><stop offset='0' stop-color='#2f745d'/><stop offset='1' stop-color='#8fd7b2'/></linearGradient>
    <linearGradient id='laneAmber' x1='0' x2='1'><stop offset='0' stop-color='#b98221'/><stop offset='1' stop-color='#f2cf78'/></linearGradient>
  </defs>
  <rect width='1180' height='700' rx='46' fill='#eef2ec'/>
  <rect x='28' y='28' width='1124' height='644' rx='34' fill='url(#ledgerGrid)'/>
  <g filter='url(#manifestShadow)'>
    <rect x='72' y='64' width='1036' height='568' rx='34' fill='#fffdf7' stroke='#173047' stroke-opacity='.16'/>
  </g>
  <g font-family='Georgia,serif' fill='#132338'>
    <text x='112' y='130' font-size='44' font-weight='700'>sender inventory manifest</text>
    <text x='112' y='170' font-size='21' fill='#536172'>every system allowed to send as the domain, logged before DNS is touched</text>
  </g>
  <g transform='translate(112 220)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <rect width='956' height='72' rx='20' fill='#173047'/>
    <g fill='#e9fbf8' font-size='15' font-weight='950' letter-spacing='.09em'>
      <text x='24' y='44'>SENDER</text><text x='290' y='44'>ROLE</text><text x='516' y='44'>DNS CLUE</text><text x='760' y='44'>ACTION</text>
    </g>
    <g font-size='18' fill='#132338'>
      <g transform='translate(0 94)'>
        <rect width='956' height='64' rx='18' fill='#eef6f1'/><rect width='8' height='64' rx='4' fill='url(#laneGreen)'/>
        <text x='24' y='40' font-weight='950'>Microsoft 365</text><text x='290' y='40'>staff mail</text><text x='516' y='40'>spf.protection.outlook.com</text><text x='760' y='40' fill='#2f745d' font-weight='950'>keep</text>
      </g>
      <g transform='translate(0 174)'>
        <rect width='956' height='64' rx='18' fill='#fff4d8'/><rect width='8' height='64' rx='4' fill='url(#laneAmber)'/>
        <text x='24' y='40' font-weight='950'>Mailchimp</text><text x='290' y='40'>newsletter</text><text x='516' y='40'>DKIM selector clue</text><text x='760' y='40' fill='#9c721d' font-weight='950'>confirm</text>
      </g>
      <g transform='translate(0 254)'>
        <rect width='956' height='64' rx='18' fill='#eef6f1'/><rect width='8' height='64' rx='4' fill='url(#laneGreen)'/>
        <text x='24' y='40' font-weight='950'>Website forms</text><text x='290' y='40'>quotes / bookings</text><text x='516' y='40'>SMTP provider</text><text x='760' y='40' fill='#2f745d' font-weight='950'>document</text>
      </g>
      <g transform='translate(0 334)'>
        <rect width='956' height='64' rx='18' fill='#f1ded8'/><rect width='8' height='64' rx='4' fill='#9a4537'/>
        <text x='24' y='40' font-weight='950'>Old CRM</text><text x='290' y='40'>unknown</text><text x='516' y='40'>obsolete include?</text><text x='760' y='40' fill='#98493b' font-weight='950'>remove only if approved</text>
      </g>
    </g>
  </g>
  <g transform='translate(112 580)' font-family='ui-monospace, Menlo, Consolas, monospace'>
    <rect width='956' height='42' rx='21' fill='#173047'/>
    <text x='26' y='27' fill='#a8d8ce' font-size='16'>fix rule: no SPF simplification until the sending inventory is signed off by the owner</text>
  </g>
</svg>
"""



mail_auth_change_lab_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='720' viewBox='0 0 1180 720' role='img' aria-labelledby='labTitle labDesc'>
  <title id='labTitle'>Email authentication change lab</title>
  <desc id='labDesc'>A controlled infrastructure change lab showing current mail DNS evidence, proposed edits, owner approval, resolver readback and rollback notes.</desc>
  <defs>
    <filter id='labShadow' x='-14%' y='-18%' width='128%' height='145%'><feDropShadow dx='0' dy='24' stdDeviation='20' flood-color='#0b1f2a' flood-opacity='.20'/></filter>
    <pattern id='benchGrid' width='42' height='42' patternUnits='userSpaceOnUse'><path d='M42 0H0v42' fill='none' stroke='#173047' stroke-opacity='.065'/></pattern>
    <linearGradient id='safeLane' x1='0' x2='1'><stop offset='0' stop-color='#2f745d'/><stop offset='1' stop-color='#72d7a2'/></linearGradient>
    <linearGradient id='amberLane' x1='0' x2='1'><stop offset='0' stop-color='#d7ad4f'/><stop offset='1' stop-color='#f3d57b'/></linearGradient>
  </defs>
  <rect width='1180' height='720' rx='46' fill='#eef2ec'/>
  <rect x='28' y='28' width='1124' height='664' rx='34' fill='url(#benchGrid)' stroke='#173047' stroke-opacity='.10'/>
  <g font-family='Georgia,serif' fill='#132338'>
    <text x='70' y='96' font-size='42' font-weight='700'>mail authentication change lab</text>
    <text x='70' y='136' font-size='20' fill='#536172'>current evidence, proposed DNS edits, owner approval and resolver readback in one controlled ticket</text>
  </g>
  <g transform='translate(70 184)' filter='url(#labShadow)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <rect width='1040' height='416' rx='32' fill='#fffdf7' stroke='#173047' stroke-opacity='.14'/>
    <g transform='translate(34 34)'>
      <rect width='276' height='326' rx='24' fill='#f0f6f1' stroke='#173047' stroke-opacity='.12'/>
      <text x='22' y='42' font-family='ui-monospace, Menlo, monospace' font-size='14' font-weight='950' letter-spacing='.12em' fill='#2f745d'>BEFORE SNAPSHOT</text>
      <g font-size='18' fill='#132338' font-weight='850'>
        <rect x='22' y='76' width='220' height='46' rx='14' fill='#fffdf7'/><text x='40' y='105'>SPF: one record</text>
        <rect x='22' y='140' width='220' height='46' rx='14' fill='#fffdf7'/><text x='40' y='169'>DKIM: selector clue</text>
        <rect x='22' y='204' width='220' height='46' rx='14' fill='#fff4d8'/><text x='40' y='233'>DMARC: p=none</text>
      </g>
      <text x='22' y='292' font-size='15' fill='#536172' font-weight='800'>Public evidence only. No logins.</text>
    </g>
    <g transform='translate(382 34)'>
      <rect width='276' height='326' rx='24' fill='#102f38' stroke='#9ed9ca' stroke-opacity='.18'/>
      <text x='22' y='42' font-family='ui-monospace, Menlo, monospace' font-size='14' font-weight='950' letter-spacing='.12em' fill='#a8d8ce'>PROPOSED EDITS</text>
      <g font-size='17' fill='#e9fbf8' font-weight='850'>
        <rect x='22' y='76' width='224' height='52' rx='14' fill='rgba(255,255,255,.08)' stroke='#9ed9ca' stroke-opacity='.18'/><text x='40' y='108'>remove obsolete include?</text>
        <rect x='22' y='146' width='224' height='52' rx='14' fill='rgba(255,255,255,.08)' stroke='#9ed9ca' stroke-opacity='.18'/><text x='40' y='178'>confirm DKIM selector</text>
        <rect x='22' y='216' width='224' height='52' rx='14' fill='rgba(255,255,255,.08)' stroke='#9ed9ca' stroke-opacity='.18'/><text x='40' y='248'>stage DMARC policy path</text>
      </g>
      <rect x='22' y='288' width='190' height='28' rx='14' fill='url(#amberLane)'/><text x='42' y='307' font-family='ui-monospace, Menlo, monospace' font-size='13' font-weight='950' fill='#173047'>OWNER APPROVAL GATE</text>
    </g>
    <g transform='translate(730 34)'>
      <rect width='276' height='326' rx='24' fill='#f3f8f4' stroke='#173047' stroke-opacity='.12'/>
      <text x='22' y='42' font-family='ui-monospace, Menlo, monospace' font-size='14' font-weight='950' letter-spacing='.12em' fill='#2f745d'>READBACK RECEIPT</text>
      <g font-size='17' fill='#132338' font-weight='850'>
        <rect x='22' y='76' width='224' height='46' rx='14' fill='#fffdf7'/><text x='40' y='105'>Google resolver</text>
        <rect x='22' y='140' width='224' height='46' rx='14' fill='#fffdf7'/><text x='40' y='169'>Cloudflare resolver</text>
        <rect x='22' y='204' width='224' height='46' rx='14' fill='#fffdf7'/><text x='40' y='233'>authoritative check</text>
      </g>
      <rect x='22' y='288' width='190' height='28' rx='14' fill='url(#safeLane)'/><text x='42' y='307' font-family='ui-monospace, Menlo, monospace' font-size='13' font-weight='950' fill='#fffdf7'>CLOSE OR ROLLBACK</text>
    </g>
    <g stroke-width='5' stroke-linecap='round' fill='none'>
      <path d='M310 198 C340 198 352 198 382 198' stroke='url(#safeLane)' stroke-dasharray='10 10'/>
      <path d='M658 198 C688 198 700 198 730 198' stroke='url(#safeLane)' stroke-dasharray='10 10'/>
    </g>
  </g>
  <g transform='translate(70 636)' font-family='ui-monospace, Menlo, monospace'>
    <rect width='1040' height='42' rx='21' fill='#173047'/>
    <text x='26' y='27' fill='#a8d8ce' font-size='16'>safe-change rule: diagnose publicly, stage edits, get owner approval, verify externally, keep rollback notes</text>
  </g>
</svg>"""
(OUT / "mail-auth-change-lab.svg").write_text(mail_auth_change_lab_svg, encoding="utf-8")
print(OUT / "mail-auth-change-lab.svg")

(OUT / "dns-routing-map.svg").write_text(svg, encoding="utf-8")
(OUT / "auth-stack-meter.svg").write_text(meter_svg, encoding="utf-8")
(OUT / "resolver-verification-receipt.svg").write_text(resolver_svg, encoding="utf-8")
(OUT / "email-trust-incident-drill.svg").write_text(incident_svg, encoding="utf-8")
(OUT / "domain-trust-seal.svg").write_text(tls_seal_svg, encoding="utf-8")
(OUT / "sender-inventory-manifest.svg").write_text(sender_inventory_svg, encoding="utf-8")
dmarc_drift_digest_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1180' height='700' viewBox='0 0 1180 700' role='img' aria-labelledby='driftTitle driftDesc'>
  <title id='driftTitle'>DMARC drift digest</title>
  <desc id='driftDesc'>A premium operational digest showing baseline mail authentication records, live DNS drift, sender lane evidence and an owner action receipt.</desc>
  <defs>
    <filter id='shadow' x='-16%' y='-18%' width='132%' height='142%'><feDropShadow dx='0' dy='26' stdDeviation='22' flood-color='#020f16' flood-opacity='.34'/></filter>
    <pattern id='grid' width='38' height='38' patternUnits='userSpaceOnUse'><path d='M38 0H0v38' fill='none' stroke='#9ed9ca' stroke-opacity='.09'/></pattern>
    <linearGradient id='lane' x1='0' x2='1'><stop offset='0' stop-color='#72e2a3'/><stop offset='.58' stop-color='#ffd36e'/><stop offset='1' stop-color='#ff8f83'/></linearGradient>
    <linearGradient id='panel' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#fffdf7'/><stop offset='1' stop-color='#e6f1ec'/></linearGradient>
  </defs>
  <rect width='1180' height='700' rx='46' fill='#06161d'/>
  <rect x='28' y='28' width='1124' height='644' rx='34' fill='url(#grid)' stroke='#9ed9ca' stroke-opacity='.16'/>
  <g font-family='Georgia,serif' fill='#e9fbf8'>
    <text x='74' y='100' font-size='44' font-weight='700'>DMARC drift digest</text>
    <text x='74' y='140' font-size='20' fill='#a8d8ce'>monthly public-DNS readback translated into one owner action receipt</text>
  </g>
  <g transform='translate(74 190)' filter='url(#shadow)' font-family='ui-sans-serif, system-ui, sans-serif'>
    <rect width='1032' height='404' rx='34' fill='url(#panel)'/>
    <g transform='translate(34 34)'>
      <rect width='276' height='286' rx='24' fill='#102f38'/>
      <text x='22' y='42' font-family='ui-monospace, Menlo, monospace' font-size='14' font-weight='950' letter-spacing='.12em' fill='#a8d8ce'>BASELINE</text>
      <text x='22' y='92' fill='#e9fbf8' font-size='28' font-weight='900'>known-good map</text>
      <g fill='#e9fbf8' font-size='17' font-weight='850'>
        <text x='22' y='148'>SPF: owner-approved</text><text x='22' y='194'>DKIM: selector logged</text><text x='22' y='240'>DMARC: p=none watched</text>
      </g>
    </g>
    <g transform='translate(378 34)'>
      <rect width='276' height='286' rx='24' fill='#fff6dd' stroke='#d7ad4f' stroke-opacity='.28'/>
      <text x='22' y='42' font-family='ui-monospace, Menlo, monospace' font-size='14' font-weight='950' letter-spacing='.12em' fill='#9c721d'>LIVE DRIFT</text>
      <text x='22' y='92' fill='#132338' font-size='28' font-weight='900'>what changed?</text>
      <g fill='#132338' font-size='17' font-weight='850'>
        <text x='22' y='148'>new CRM include found</text><text x='22' y='194'>selector mismatch amber</text><text x='22' y='240'>resolver readback pending</text>
      </g>
    </g>
    <g transform='translate(722 34)'>
      <rect width='276' height='286' rx='24' fill='#eaf7f2' stroke='#2f745d' stroke-opacity='.22'/>
      <text x='22' y='42' font-family='ui-monospace, Menlo, monospace' font-size='14' font-weight='950' letter-spacing='.12em' fill='#2f745d'>OWNER RECEIPT</text>
      <text x='22' y='92' fill='#132338' font-size='28' font-weight='900'>action note</text>
      <g fill='#132338' font-size='17' font-weight='850'>
        <text x='22' y='148'>confirm sender owner</text><text x='22' y='194'>approve or rollback</text><text x='22' y='240'>file monthly receipt</text>
      </g>
    </g>
    <path d='M310 178 C340 178 348 178 378 178 M654 178 C684 178 692 178 722 178' stroke='url(#lane)' stroke-width='7' fill='none' stroke-linecap='round' stroke-dasharray='12 12'/>
  </g>
  <g transform='translate(74 626)' font-family='ui-monospace, Menlo, monospace'>
    <rect width='1032' height='46' rx='23' fill='#0c2730' stroke='#9ed9ca' stroke-opacity='.18'/>
    <text x='26' y='30' fill='#a8d8ce' font-size='16'>monitoring rule: compare baseline, identify sender lane, verify public resolvers, send a short owner-safe action receipt</text>
  </g>
</svg>"""
(OUT / "dmarc-drift-digest.svg").write_text(dmarc_drift_digest_svg, encoding="utf-8")

for name in ["dns-routing-map.svg", "auth-stack-meter.svg", "resolver-verification-receipt.svg", "email-trust-incident-drill.svg", "domain-trust-seal.svg", "sender-inventory-manifest.svg", "dmarc-drift-digest.svg"]:
    print(OUT / name)
