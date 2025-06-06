-------------------------------
basic for all program 
-------------------------------
sudo apt remove Openjdk-17-* -y
sudo apt remove Openjdk-11-* -y
sudo apt remove Openjdk-21-* -y
sudo apt autoremove --purge -y

sudo apt install openjdk-11-jdk -y (for prg2 , cannot work in java version 17, it requires 11)
sudo apt install openjdk-17-jdk -y (for other program)

sudo apt install maven
sudo apt install gradle
mvn -version
gradle -version


-------------------------------
install jenkins
-------------------------------
sudo apt update
sudo apt install Jenkins
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install Jenkins
sudo systemctl start jenkins
sudo systemctl status Jenkins

-------------------------------
program 02 my maven app
-------------------------------


cd
ls
rm -rf ~/MyMavenApp //removes the existing project



mvn archetype:generate -DgroupId=com.example -DartifactId=MyMavenApp -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd MyMavenApp
tree
nano pom.xml (make changes using gpt)
mvn compile
mvn test
mvn package
mvn clean


-------------------------------
program 02 gradle project
-------------------------------

cd
ls
sudo rn -rf /opt/gradle
nano ~/.bashrc
	remove "export PATH=/opt/gradle/gradle-8.7/bin:$PATH" which will be at the top. if nothing is there ignore
source ~/.bashrc
(close and open the terminal again)

rm -rf ~/HelloGradle //removes existing project if exists

mkdir HelloGradle
cd HelloGradle
gradle init --type java-application
tree
gedit build.gradle
plugins {
    id 'java'
    id 'application'
}

group = 'com.example'
version = '1.0'

repositories {
    mavenCentral()
}

dependencies {
    testImplementation 'junit:junit:4.13.2'
}

application {
    mainClass = 'com.example.App'
}

task hello {
    doLast {
        println 'Hello, Gradle!'
    }
}

mkdir -p src/main/java/com/example/App.java
nano src/main/java/com/example/App.java
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Gradle Java application running");
    }
}
ctrl s -> ctrl X

rm -rf gradle gradlew gradlew.bat
wget https://services.gradle.org/distributions/gradle-8.7-bin.zip
sudo unzip gradle-8.7-bin.zip -d/opt/gradle
nano ~/.bashrc
	export PATH=/opt/gradle/gradle-8.7/bin:$PATH // add this to the top of the file
source ~/.bashrc
gradle -v // make sure its 8.7
cd ~/HelloGradle
ls src/main/java //make sure the output comes as App.java
mkdir -p src/main/java/com/example/
nano src/main/java/com/example/App.java
package com.example;

public class App {
    public String getGreeting() {
        return "Hello, Gradle!";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
gradle init --type java-application
gradle wrapper
ls ./gradlew //makesure output is ./gradlew
./gradlew build
./gradlew run
./gradlew hello
./gradlew run



-------------------------------
program 04  maven to gradle
-------------------------------

rm -rf ~/HelloMavenGradle
rm -rf ~/HelloMaven


mvn archetype:generate -DgroupId=com.example -DartifactId=HelloMaven -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd helloMaven
tree
(change the pom file )
mvn package
java -cp target/HelloMaven-1.0-SNAPSHOT.jar.com.example.App

//in new terminal create a gradle project

mkdir HelloMavenGradle
cd HelloMavenGradle
gradle init --type java-applications
tree
mkdir -p src/main/java/com/example
cp../HelloMaven/src/main/java/com/example/App.java src/main/java/com/example
nano build.gradle (make changes here)
gradle build
gradle run


-------------------------------
program 06 Jenkins pipeline
-------------------------------

new item -> Maven-Freestyle -> freestyle project -> OK
sourcecode management ->git -> https://github.com/devops-ds/your-maven-project.git -> main
build -> build setup -> execute shell ->/usr/bin/mvn clean install
post build actions  ->add post build actions -> publish Junit result report -> **/target/surefire-reports/*.xml
save 
build now
under build history click console output to check the result


new item -> Maven-pipeline -> pipeline -> OK
pipeline -> pipeline script  (for maven)

pipeline {
    agent any // Or specify a specific agent label

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your GitHub repository
                git url: 'https://github.com/devops-ds/your-maven-project.git', branch: 'main' // Replace with your repo URL if different, adjust branch name if needed
                // If your repository is private, you'll need to add credentials here, e.g.:
                // git url: 'https://github.com/devops-ds/your-maven-project.git', branch: 'main', credentialsId: 'your-credential-id'
            }
        }

        stage('Build') {
            steps {
                // Execute Maven build using the 'mvn' command with the full path
                // To find the full path to your 'mvn' executable on Linux/macOS, open your terminal and run:
                // which mvn
                sh '/usr/bin/mvn clean package' // Replace with actual path
            }
        }

        stage('Test') {
            steps {
                // Optionally, separate test execution if needed
                // This step is often not strictly necessary if 'mvn clean package' already runs tests
                // sh '/path/to/your/maven/bin/mvn test' // Replace with actual path
                echo 'Tests are typically run during the Build stage with Maven.'
            }
        }
    }
    post {
        always {
            // Archive test reports
            junit '*/target/surefire-reports/.xml'
        }
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Build or tests failed.'
        }
        // Add other post conditions like 'unstable', 'changed' as needed
    }
}

save
build now
console output 


-------------------------------
program 07 ansible 
-------------------------------

sudo apt update
sudo apt upgrade -y
sudo apt install ansible -y
ansible --version

nano hosts.ini
[loacl]
localhost ansible_connection=local

nano setup.yml
---
- name: Basic Localhost Setup
  hosts: local
  become: yes
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install curl
      apt:
        name: curl
        state: present
sudo ansible-playbook -I hosts.ini setup.yml

-------------------------------
program 07 Jenkins ansible 
-------------------------------
in Jenkins,
new project -> HelloMaven-CI -> freestyle project -> OK
sourcecode management -> git -> https://github.com/devops-ds/your-maven-project.git -> main
build -> execute cell -> /usr/bin/mvn clean install
build -> execute cell -> ansible-playbook -I hosts.ini deploy.yml
postbuild actions -> archive the artifacts -> target/*.jar
save
build now

in command prompt:- ls -l /var/lib/Jenkins/deployment/
