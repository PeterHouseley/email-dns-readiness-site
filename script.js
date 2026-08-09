document.querySelectorAll('a[href^="mailto:"]').forEach(a=>a.addEventListener('click',()=>document.body.dataset.intent='contact'));
