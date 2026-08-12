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

(OUT / "dns-routing-map.svg").write_text(svg, encoding="utf-8")
(OUT / "auth-stack-meter.svg").write_text(meter_svg, encoding="utf-8")
(OUT / "resolver-verification-receipt.svg").write_text(resolver_svg, encoding="utf-8")
(OUT / "email-trust-incident-drill.svg").write_text(incident_svg, encoding="utf-8")
print(OUT / "dns-routing-map.svg")
print(OUT / "auth-stack-meter.svg")
print(OUT / "resolver-verification-receipt.svg")
print(OUT / "email-trust-incident-drill.svg")
