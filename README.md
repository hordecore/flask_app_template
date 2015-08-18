Flask + Metro UI app template

# install

	PROG=название_программы
	git clone git@github.com:hordecore/flask_app_template.git /opt/$PROG
	
## virtualenv

	cd /opt/$PROG
	virtualenv venv/
	. venv/bin/activate
	pip install -r requirements.txt
	deactivate
	
## init

	sed -e "s/__PROG__/$PROG/g" contrib/init-script > /etc/rc.d/init.d/$PROG
	chmod a+x /etc/rc.d/init.d/$PROG
	chkconfig --level 345 $PROG on
	service $PROG restart

## nginx

Config example:

	upstream flask {
		server 127.0.0.1:8085;
	}

	# Configuration for Nginx
	server {
		listen 80;

		location = /favico.ico  {
			root /app/favico.ico;
		}

		location / {
			proxy_set_header X-Real-IP  $remote_addr;
			proxy_set_header X-Forwarded-For $remote_addr;
			proxy_set_header Host $host;
			proxy_pass http://127.0.0.1:8085;
		}
	}

Don't forget about service nginx restart
