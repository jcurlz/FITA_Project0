pipeline {
    agent any

    environment {
        PYTHON = "python"
        REPORT_PATH = "behave_report.html"
    }

    stages {
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
                // Replace '%TAGS%' with your desired tag expression if needed
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
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
