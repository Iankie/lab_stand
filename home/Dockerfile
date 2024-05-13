#Import OS
FROM alpine:3.1

#Install packets
RUN apk update && \
        apk upgrade --available && \
        apk add --no-cache \
        openssl ca-certificates \
        curl sudo openssh openrc

#Configure SSH
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

#Create user
RUN adduser -D user
RUN echo "user:P@ssw0rd" | chpasswd 

#Copy flag
COPY secret2.txt /home/user/      

#SSH daemon server run 
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /
RUN chmod +x -v entrypoint.sh
