pipeline {
  agent {
    docker {
      image 'px4io/px4-docs:2020-01-05'
    }
  }
  stages {

    stage('Build') {
      environment {
        HOME = "${WORKSPACE}"
      }

      steps {
        sh('export')
        checkout(scm)
        sh('gitbook install')
        sh('gitbook build')
        stash(includes: '_book/', name: 'gitbook')
        // publish html
        publishHTML(target: [
          reportTitles: 'Mavlink Dev Guide',
          allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: '_book',
          reportFiles: '*',
          reportName: 'Mavlink Dev Guide'
        ])
      }

    } // Build

    stage('Deploy') {
      environment {
        GIT_AUTHOR_EMAIL = "bot@px4.io"
        GIT_AUTHOR_NAME = "PX4BuildBot"
        GIT_COMMITTER_EMAIL = "bot@px4.io"
        GIT_COMMITTER_NAME = "PX4BuildBot"
      }

      steps {
        sh('export')
        unstash('gitbook')
        withCredentials([usernamePassword(credentialsId: 'px4buildbot_github_personal_token', passwordVariable: 'GIT_PASS', usernameVariable: 'GIT_USER')]) {
          sh('git clone https://${GIT_USER}:${GIT_PASS}@github.com/mavlink/mavlink.io.git')
          //sh('rm -rf mavlink.io/${BRANCH_NAME}')
          //sh('mkdir -p mavlink.io/${BRANCH_NAME}')
          //sh('cp -r _book/* mavlink.io/${BRANCH_NAME}/')
          //sh('cd mavlink.io; git add ${BRANCH_NAME}; git commit -a -m "gitbook build update `date`"')
          sh('cp -r _book/* mavlink.io/')
          sh('cd mavlink.io; git add .; git commit -a -m "gitbook build update `date`"')
          sh('cd mavlink.io; git push origin master')
          
        }
      }
      post {
        always {
          sh('rm -rf mavlink.io')
        }
      }
      when {
        anyOf {
          branch "master"
          branch "pr-jenkins"
        }
      }

    } // Deploy
  } // stages

  options {
    buildDiscarder(logRotator(numToKeepStr: '10', artifactDaysToKeepStr: '30'))
    skipDefaultCheckout()
    timeout(time: 60, unit: 'MINUTES')
  }

}
