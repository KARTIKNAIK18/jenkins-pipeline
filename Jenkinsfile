pipeline{
    agent any
    environment{
        IMAGE_NAME = '$DOCKER_USER/blog-app:v1'

    }
    stages{
        stage('Checkout'){ 
            steps {
                git branch: 'main', url: 'https://github.com/KARTIKNAIK18/jenkins-pipeline.git'
                sh 'tree'
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
                docker build -t $IMAGE_NAME .
                docker push $IMAGE_NAME
                '''
            }
         }
    }
}