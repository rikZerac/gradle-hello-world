ARG jenkinsVer=2.235
FROM jenkins/jenkins:${jenkinsVer}-alpine

LABEL maintainer="postarcr@gmail.com"

#Default global Gradle version
ARG gradleVer=6.4

#Jenkins plugins preinstallation
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
#Turn down Jenkins GUI initial master plugins installation offer
#WARN: this way Jenkins instance will be unsecured(no login required)
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

#Install Gradle binary distribution
USER root
RUN wget https://services.gradle.org/distributions/gradle-${gradleVer}-bin.zip -P /tmp
RUN mkdir /usr/local/bin/gradle
RUN unzip -d /usr/local/bin/gradle /tmp/gradle-${gradleVer}-bin.zip
RUN rm -f /tmp/gradle-${gradleVer}-bin.zip
RUN chmod 755 /usr/local/bin/gradle
RUN chmod 755 /usr/local/bin/gradle/gradle-${gradleVer}
RUN chmod 755 /usr/local/bin/gradle/gradle-${gradleVer}/bin

#gradle bash command available for jenkins user
USER jenkins 
ENV PATH /usr/local/bin/gradle/gradle-${gradleVer}/bin:${PATH}