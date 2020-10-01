init:
	rm -rf .venv
	virtualenv --always-copy .venv
	( \
    . .venv/bin/activate; \
    python3 -m pip install -r requirements.txt; \
    )

run:
	( \
	. .venv/bin/activate; \
	python3 rtm_test.py; \
	)

python-test: 
	( \
    . .venv/bin/activate; \
    python3 -m pytest --cov-report term --cov-report html:cov_html --cov-report xml:cov.xml --cov=discord-tft-bot discord-tft-bot/test/; \
    )

lint: python-build