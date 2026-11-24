.PHONY: check start

check:
	python3 -c "import re,sys,os; h=open('index.html').read(); assert '<title>' in h, 'missing title'; assert 'Linus_Torvalds.jpeg' in h, 'missing linus image'; assert 'targetDate' in h or 'countdown' in h.lower(), 'missing countdown'; [os.path.isfile('assets/fonts/'+f) or sys.exit('missing font: '+f) for f in ('comic-neue-400.woff2','comic-neue-700.woff2','patrick-hand-400.woff2')]; print('check: OK')"

start:
	python3 -m http.server 8080
