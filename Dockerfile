FROM jenkins/jenkins:alpine

LABEL maintainer="postarcr@gmail.com"

ARG gradlever=6.4

USER root
RUN wget https://services.gradle.org/distributions/gradle-${gradlever}-bin.zip -P /tmp
RUN mkdir /usr/local/bin/gradle
RUN unzip -d /usr/local/bin/gradle /tmp/gradle-${gradlever}-bin.zip
RUN rm -f /tmp/gradle-${gradlever}-bin.zip
RUN chmod 755 /usr/local/bin/gradle
RUN chmod 755 /usr/local/bin/gradle/gradle-${gradlever}
RUN chmod 755 /usr/local/bin/gradle/gradle-${gradlever}/bin

USER jenkins 
ENV PATH /usr/local/bin/gradle/gradle-${gradlever}/bin:${PATH}