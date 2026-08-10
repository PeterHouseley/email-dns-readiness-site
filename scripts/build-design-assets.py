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

(OUT / "dns-routing-map.svg").write_text(svg, encoding="utf-8")
print(OUT / "dns-routing-map.svg")
