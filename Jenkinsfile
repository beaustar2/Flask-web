pipeline {
    agent any

    environment {
        UBUNTU_SERVER = '172.31.42.221'
        AMAZON_LINUX_SERVER = '172.31.34.127'
        APP_PATH = '/path/to/your/app'
        APP_SERVICE = 'your-app-service'
        SSH_CREDENTIALS_ID = 'YOUR_SSH_CREDENTIALS_ID'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'source venv/bin/activate && python -m unittest discover'
                }
            }
        }

        stage('Deploy to Ubuntu Server') {
            steps {
                script {
                    ansibleDeploy(UBUNTU_SERVER)
                }
            }
        }

        stage('Deploy to Amazon Linux Server') {
            steps {
                script {
                    ansibleDeploy(AMAZON_LINUX_SERVER)
                }
            }
        }
    }
}

def ansibleDeploy(server) {
    withCredentials([sshUserPrivateKey(credentialsId: SSH_CREDENTIALS_ID, keyFileVariable: 'SSH_KEY')]) {
        sh """
            ansible-playbook -i "${server}," -e "app_path=${APP_PATH} app_service=${APP_SERVICE}" -u ec2-user --private-key=\$SSH_KEY -v ansible/deploy.yml
        """
    }
}
