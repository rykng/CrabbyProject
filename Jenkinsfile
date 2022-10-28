pipeline {
  agent any
  stages {
    stage('dev-build') {
      parallel {
        stage('dev-build') {
          steps {
            git(url: 'https://github.com/rykng/CrabbyProject.git', branch: '*/main', credentialsId: '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')
          }
        }

        stage('Setup Venv') {
          steps {
            sh 'source /Users/rng/.virtualenvs/GundamProject/bin/activate'
            sh '/Users/rng/.virtualenvs/GundamProject/bin/pip install -r requirements.txt'
          }
        }

      }
    }

    stage('dev-unit-test') {
      steps {
        sh 'pytest --junit-xml=report.xml'
      }
    }

    stage('dev-deploy') {
      steps {
        echo 'Deploying to dev...'
      }
    }

    stage('dev e2e test') {
      steps {
        build 'playwight-demo'
      }
    }

    stage('gatekeeper') {
      steps {
        echo 'Dummy for now'
      }
    }

    stage('Deploy to Stage') {
      steps {
        echo 'Deploying to Stage'
      }
    }

  }
}