# # From https://tailwindcss.com/docs/installation/tailwind-cli
# install-bin-linux:
# 	wget https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 
# 	mv tailwindcss-linux-x64 venv/bin/tailwindcss
# 	chmod +x venv/bin/tailwindcss

# From https://tailwindcss.com/docs/installation/tailwind-cli
install:
	cd ../.. && npm install tailwindcss @tailwindcss/cli

init:
	make install

# From https://tailwindcss.com/docs/installation/tailwind-cli
compile:
	npx @tailwindcss/cli -i ./src/input.css -o ../static/css/tailwind.css -m

# tailwind-compilemax:
# 	npx @tailwindcss/cli -i ./gdvoisins/tailwind/input.css -o ./gdvoisins/static/css/gdvoisins/tailwind.css 

watch:
	npx @tailwindcss/cli -i ./src/input.css -o ../static/css/tailwind.css --watch

