pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Eman-gul457/devops-automation-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo .'
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                sh 'ansible-playbook ansible/playbook.yml --connection=local --extra-vars "ansible-become-pass=kali"'
            }
        }
    }
}
