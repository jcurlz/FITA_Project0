pipeline {
    agent any

    environment {
        PYTHON = "python"
        REPORT_PATH = "reports/behave_report.html"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }   
        }
        stage('Setup') {
            steps {
                echo 'Upgrading pip and installing dependencies...'
                bat "${env.PYTHON} -m pip install --upgrade pip"
                bat "${env.PYTHON} -m pip install -r requirements.txt"
            }
        }
        stage('Build') {
            steps {
                echo 'Building project (if needed)...'
                bat 'echo Build completed.'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Behave tests with HTML report...'
                bat """
                    set REPORT_PATH=${env.REPORT_PATH}
                    ${env.PYTHON} -m behave features/ -t "%TAGS%" --format behave_html_formatter:HTMLFormatter --out %REPORT_PATH% --no-skipped --no-capture -f plain
                """
            }
        }
        stage('Archive Results') {
            steps {
                echo 'Archiving Behave HTML report...'
                archiveArtifacts artifacts: "${env.REPORT_PATH}", allowEmptyArchive: true
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying project (placeholder)...'
                bat 'echo Deploy step completed.'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded!'
            emailext(
                to: 'jcurlz55@gmail.com',
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build succeeded! Check details at ${env.BUILD_URL}",
                from: 'jcurlz55@gmail.com',
                replyTo: 'jcurlz55@gmail.com',
                attachLog: true,
                smtpCredentialId: 'gtvf bwbr gljr hagt'  // replace with actual Jenkins credential ID
            )
        }
        failure {
            echo 'Pipeline failed!'
            emailext(
                to: 'jcurlz55@gmail.com',
                subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build failed! Check console output: ${env.BUILD_URL}",
                from: 'jcurlz55@gmail.com',
                replyTo: 'jcurlz55@gmail.com',
                attachLog: true,
                smtpCredentialId: 'gtvf bwbr gljr hagt'  // replace with actual Jenkins credential ID
            )
        }
    }
}
