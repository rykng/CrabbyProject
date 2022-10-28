
pipeline {
    agent any
    
    environment {
        HAPPY_CAT = 'cat #1'
    }

    stages {
        
        
        stage('Checkout') {
            steps {
                echo "Who is happy cat? => ${HAPPY_CAT}"
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '1a7f5656-8ced-46b4-a61c-0950fbf687c0', url: 'https://github.com/rykng/CrabbyProject.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '1a7f5656-8ced-46b4-a61c-0950fbf687c0', url: 'https://github.com/rykng/CrabbyProject.git'
                echo 'Activate venv from local'
                sh '''source /Users/rng/.virtualenvs/GundamProject/bin/activate'''
                sh '''pip install -r requirements.txt'''
                echo 'Run unittest'
                sh '''pytest --junit-xml=report.xml'''
            }
        
        }
        stage('View Envs') {
            steps {
                echo "See View Envs" 
                sh '''env | sort'''
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying ${ currentBuild.changeSets }  to dev"
            }
        }
        stage('e2e Test') {
            steps {
                echo "Going to run e2e Test vs ${ env.GIT_COMMIT } ${env.BUILD_NUMBER}"
            }
        }
        stage('GateKeeper') {
            steps {
                echo 'GateKeeper to check if other services pass e2e test'
            }
        }
        stage('Deploy to QA') {
            steps {
                echo "Deploying [ ${ env.GIT_COMMIT } ]to QA vs ${env.JOB_NAME}"
                sh '''env | sort'''
                sh '''deactivate'''
            }
        }
        
    }
}
