pipeline{
    agent any
    environment{
        IMAGE_NAME = '$DOCKER_USER/blog-app:v1'

    }
    stages{
        stage('Login') {
            steps {
                git branch: 'main', url: 'https://github.com/KARTIKNAIK18/jenkins-pipeline.git'
                withCredentials([usernamePassword(credentials: docker-cred,
                usernameVariable: 'DOCKER_USER',
                passwordVarible: 'DOCKER_PASS')]){
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }
        stage('Build'){
            steps{
               sh '''
               docker build -t $IMAGE_NAME .
               '''
            }
        }
    }
}