env:
	source env/bin/activate
run:
	python3 parser_avito.py
test:
	curl -v "https://www.avito.ru/moskovskaya_oblast_krasnogorsk/mototsikly_i_mototehnika/honda_cb400sf_1994_4098010592" /
