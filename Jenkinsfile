pipeline{
    agent any
    stages{
        stage('Execute Ansibleplaybook'){
            steps{
                sh 'python dynamicparameters.py  ${ipaddress} ${username} ${password}'
              sh 'ansible-playbook -i hosts job.yml'
            }
        }
    }
}
