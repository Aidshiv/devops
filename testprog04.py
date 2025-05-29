
#1Jenkins Pipeline Script (Maven)
#file name  "Jenkins" 

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


#2 Jenkins Pipeline Script (Maven)
#file name  "Jenkins" 

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
