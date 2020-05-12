FROM jenkins/jenkins:2.235-alpine

LABEL maintainer="postarcr@gmail.com"

#Default global Gradle version
ARG gradlever=6.4

#Jenkins plugins preinstallation
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
#Turn down Jenkins GUI initial master plugins installation offer
ENV JAVA_OPTS -Djenkins.install.runsetupwizard=false
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

#Install Gradle binary distribution
USER root
RUN wget https://services.gradle.org/distributions/gradle-${gradlever}-bin.zip -P /tmp
RUN mkdir /usr/local/bin/gradle
RUN unzip -d /usr/local/bin/gradle /tmp/gradle-${gradlever}-bin.zip
RUN rm -f /tmp/gradle-${gradlever}-bin.zip
RUN chmod 755 /usr/local/bin/gradle
RUN chmod 755 /usr/local/bin/gradle/gradle-${gradlever}
RUN chmod 755 /usr/local/bin/gradle/gradle-${gradlever}/bin

#gradle bash command available for jenkins user
USER jenkins 
ENV PATH /usr/local/bin/gradle/gradle-${gradlever}/bin:${PATH}