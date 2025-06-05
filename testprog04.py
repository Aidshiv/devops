CONTINUOUS INTEGRATION WITH JENKINS (UBUNTU + MAVEN/GRADLE)

───────────────────────────────────────────────
🔧 STEP 1: INSTALL JENKINS, MAVEN & GRADLE
───────────────────────────────────────────────
sudo apt update
sudo apt install openjdk-17-jdk -y
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo apt install maven -y
sudo apt install gradle -y
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

───────────────────────────────────────────────
🛠️ STEP 2: CREATE FREESTYLE JOB - MAVEN
───────────────────────────────────────────────
1. Visit: http://localhost:8080 → Login
2. New Item → Name: Maven-CI → Freestyle Project → OK
3. Source Code Management:
   - Select "Git"
   - Repo URL: https://github.com/yourusername/your-maven-project.git
4. Build:
   - Add build step → "Invoke top-level Maven targets"
   - Goals: clean package
5. Post-build Actions:
   - Add "Publish JUnit test result report"
   - Test report XMLs: **/target/surefire-reports/*.xml
6. Save → Build Now → Console Output

───────────────────────────────────────────────
🛠️ STEP 3: CREATE FREESTYLE JOB - GRADLE
───────────────────────────────────────────────
1. New Item → Name: Gradle-CI → Freestyle Project → OK
2. Source Code Management:
   - Git URL: https://github.com/yourusername/your-gradle-project.git
3. Build:
   - Add build step → "Invoke Gradle script"
   - Tasks: clean build
4. Post-build Actions:
   - Add "Publish JUnit test result report"
   - Test report XMLs: **/build/test-results/test/*.xml
5. Save → Build Now → Console Output

───────────────────────────────────────────────
⚙️ STEP 4: CREATE PIPELINE JOB (MAVEN)
───────────────────────────────────────────────
1. New Item → Name: Pipeline-CI → Pipeline → OK
2. Scroll to "Pipeline" → Select: Pipeline script → Paste:

pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/yourusername/your-maven-project.git', branch: 'main'
      }
    }
    stage('Build') {
      steps {
        sh 'mvn clean package'
      }
    }
    stage('Test') {
      steps {
        sh 'mvn test'
      }
    }
  }
  post {
    always {
      junit '**/target/surefire-reports/*.xml'
    }
    success {
      echo 'Build and tests succeeded!'
    }
    failure {
      echo 'Build or tests failed.'
    }
  }
}

───────────────────────────────────────────────
⚙️ STEP 5: CREATE PIPELINE JOB (GRADLE)
───────────────────────────────────────────────
1. New Item → Name: Gradle-Pipeline → Pipeline → OK
2. Pipeline script → Paste:

pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/yourusername/your-gradle-project.git', branch: 'main'
      }
    }
    stage('Build') {
      steps {
        sh './gradlew clean build'
      }
    }
    stage('Test') {
      steps {
        sh './gradlew test'
      }
    }
  }
  post {
    always {
      junit '**/build/test-results/test/*.xml'
    }
    success {
      echo 'Build and tests succeeded!'
    }
    failure {
      echo 'Build or tests failed.'
    }
  }
}

───────────────────────────────────────────────
🧰 EXTRA JENKINS COMMANDS (OPTIONAL)
───────────────────────────────────────────────
sudo systemctl restart jenkins
sudo systemctl status jenkins
chmod +x gradlew       # Make Gradle wrapper executable
mvn clean              # Clean Maven project
./gradlew clean        # Clean Gradle project
