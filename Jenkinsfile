node {
    stage('Clean up Workspace'){
        echo "Deleting the existing files in the workspace and starting fresh"
        cleanWs()
    }
    stage('SCM Checkout') {
        echo 'Getting code from git..'
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Krishna-dubey/test-jenkins.git']]])
    }
    stage('Build')
       {
           echo "In Build Stage"
           if (fileExists('requirements.txt')) {
               sh """
                   python3 -m venv env
                   source env/bin/activate
                   pip3 install -r requirements.txt
                """
            }
       }
       stage('Unit test')
       {
           echo "In Unit Testing Stage"
           sh "source env/bin/activate"
           sh "python3 -m unittest test_circle_area.py"
           sh "/var/lib/jenkins/workspace/MytestPipeline/env/bin/pylint circle_area.py"
           
       }
      stage('Deploy'){
          echo "In Deployment Stage"
        sh "sudo scp -i  '/var/lib/jenkins/20904_Krishna.pem' -o StrictHostKeyChecking=no -r circle_area.py ec2-user@18.212.130.209:/home/ec2-user"
        sh "sudo scp -i  '/var/lib/jenkins/20904_Krishna.pem' -o StrictHostKeyChecking=no -r test_circle_area.py ec2-user@18.212.130.209:/home/ec2-user"
        sh '''sudo ssh -T -i "/var/lib/jenkins/20904_Krishna.pem" -o StrictHostKeyChecking=no ec2-user@18.212.130.209 
                sudo yum install python3
                python3 -m venv env
                source env/bin/activate
                python3 -m unittest test_circle_area.py
                <<EOT'''
                
      }
}
