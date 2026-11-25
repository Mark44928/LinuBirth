.PHONY: check start

check:
	python3 -c "import re,sys,os; h=open('index.html').read(); assert '<title>' in h, 'missing title'; assert 'Linus_Torvalds.jpeg' in h, 'missing linus image'; assert 'targetDate' in h or 'countdown' in h.lower(), 'missing countdown'; assert 'og:title' in h, 'missing og:title'; assert 'twitter:card' in h, 'missing twitter:card'; assert h.count('class=\"tux\"') == 4, 'expected 4 Tuxes, got %d' % h.count('class=\"tux\"'); [os.path.isfile('assets/fonts/'+f) or sys.exit('missing font: '+f) for f in ('comic-neue-400.woff2','comic-neue-700.woff2','patrick-hand-400.woff2')]; [os.path.isfile(f) or sys.exit('missing file: '+f) for f in ('favicon.svg','robots.txt','sitemap.xml','docs/screenshot.png','linubirth.py')]; print('check: OK')"
	python3 -c "import py_compile; py_compile.compile('linubirth.py', doraise=True); print('cli: OK')"
	python3 linubirth.py --once --no-color > /dev/null && echo "cli-run: OK"

start:
	python3 -m http.server 8080
