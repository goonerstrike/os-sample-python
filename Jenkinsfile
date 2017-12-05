node('maven') {
  stage('Build') {
    git url: "https://github.com/goonerstrike/os-sample-python.git"
  }
  stage('Test') {
  }
  stage('Build Image') {
    unstash name:"jar"
    sh "oc start-build os-sample-ython"
  }
  stage('Deploy') {
    openshiftDeploy depCfg: 'cart'
    openshiftVerifyDeployment depCfg: 'os-sample-python', replicaCount: 1, verifyReplicaCount: true
  }
  stage('System Test') {
    echo "BLEH"
  }
}

