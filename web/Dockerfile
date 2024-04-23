#Import OS
FROM alpine:3.19

#Create user 
RUN adduser -D web-admin
RUN echo "web-admin:P@ssw0rd_2024!" | chpasswd

#Set workdir 
WORKDIR /home/web-admin/

#Copy reqs
COPY requirements.txt /home/web-admin/

#Install need packets 
RUN apk update && \
        apk upgrade --available && \
        apk add --no-cache \
        openssl \
        ca-certificates \
        curl \
        sudo

RUN apk add python3 py3-pip python3-dev openssh && \
    pip3 install -r requirements.txt --break-system-packages

#Copy app.py files to container 
COPY app.py flag1.txt note.txt /home/web-admin/
RUN mkdir templates
COPY templates/index.html templates/

RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config

#SSH daemon server run 
ENTRYPOINT ["./entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /home/web-admin/
RUN chmod +x -v entrypoint.sh

