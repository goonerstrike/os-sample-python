node('') {
    stage('Build') {
      git url: "https://github.com/goonerstrike/os-sample-python.git"
    }
    stage('Test') {
    }
    stage('Build Image') {
      sh "oc start-build os-sample-python"
    }
    stage('Deploy') {
      openshiftDeploy depCfg: 'os-sample-python'
      openshiftVerifyDeployment depCfg: 'os-sample-python', replicaCount: 1, verifyReplicaCount: true
    }
    stage('System Test') {
      sh "python tests/test.py"
    }
}

