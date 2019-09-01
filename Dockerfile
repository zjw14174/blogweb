FROM python:3.7

RUN sed -i "s/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list \
	&& sed -i "s/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list \
	&& apt-get update \
    && apt-get install -y --no-install-recommends \
	nginx \
    && rm -rf /var/lib/apt/lists/* && sed -i "/user/a\daemon off;" /etc/nginx/nginx.conf 
WORKDIR /usr/src/app
COPY . .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /usr/src/app/requirements.txt && mkdir uwsgi \
	&& mkdir -p /usr/src/app/uwsgi \
	&& chown -R www-data:www-data /usr/src/app/ \
	&& chmod -R 777 /usr/src/app \
	&& /bin/cp -af /usr/src/app/nginx.txt /etc/nginx/sites-available/default

EXPOSE 81
CMD nohup sh -c 'uwsgi --ini /usr/src/app/uwsgi.ini && nginx'
