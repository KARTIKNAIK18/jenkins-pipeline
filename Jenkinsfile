pipeline{
    agent any
    environment{
        IMAGE_TAG = 'v1'

    }
    stages{
        stage('Checkout'){ 
            steps {
                git branch: 'main', url: 'https://github.com/KARTIKNAIK18/jenkins-pipeline.git'
                sh 'ls -a'
            }
        }

        stage('Login'){
            steps{
                withCredentials([usernamePassword(
                credentialsId: 'docker-cred',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS')]){
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Build & Push'){
            steps{
                sh '''
                docker build -t $DOCKER_USER/blog-app:$IMAGE_TAG .
                docker push $DOCKER_USER/blog-app:$IMAGE_TAG
                '''
            }
         }
    }
}