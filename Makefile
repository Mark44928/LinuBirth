.PHONY: check start

check:
	python3 -c "import re,sys; h=open('index.html').read(); assert '<title>' in h, 'missing title'; assert 'Linus_Torvalds.jpeg' in h, 'missing linus image'; assert 'targetDate' in h or 'countdown' in h.lower(), 'missing countdown'; print('check: OK')"

start:
	python3 -m http.server 8080
