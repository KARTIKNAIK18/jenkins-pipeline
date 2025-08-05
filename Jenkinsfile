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

            stage('Build & Push'){
                steps{
                    withCredentials([usernamePassword(
                    credentialsId: 'docker-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS')]){
                        sh '''
                        docker build -t $DOCKER_USER/blog-app:$IMAGE_TAG .
                        docker images
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_USER/blog-app:$IMAGE_TAG
                        '''
                    }
                }
            }
            // stage('Scan'){
            //     steps{
            //         withCredentials([usernamePassword(
            //             credentialsId: 'docker-cred',
            //             usernameVariable: 'DOCKER_USER',
            //             passwordVariable: 'DOCKER_PASS')]){
            //                     sh '''
            //                     docker run aquasec/trivy image\
            //                     docker.io/$DOCKER_USER/blog-app:$IMAGE_TAG
            //                     '''
            //             }
                            
            //     }
            // }

        stage('Deploy'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'docker-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS')]){
                        sh '''
                        docker pull $DOCKER_USER/blog-app:$IMAGE_TAG
                        docker run -d --name blog_app -p 5000:5000 $DOCKER_USER/blog-app:$IMAGE_TAG
                        sleep 20
                        docker stop blog_app
                        '''
                }
            }
        }


    }
    }